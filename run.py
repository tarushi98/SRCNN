import cv2 
import numpy as np
from keras.models import Sequential,load_model
from keras.layers import Conv2D
from keras.optimizers import Adam

print("Hello")

def build_model():
    srcnn=Sequential()
    srcnn.add(Conv2D(filters=128, kernel_size = (9, 9), kernel_initializer='glorot_uniform',
                 activation='relu', padding='valid', use_bias=True, input_shape=(None,None,1)))
    srcnn.add(Conv2D(filters=64, kernel_size = (3, 3), kernel_initializer='glorot_uniform',
                     activation='relu', padding='same', use_bias=True))
    srcnn.add(Conv2D(filters=1, kernel_size = (5, 5), kernel_initializer='glorot_uniform',
                     activation='linear', padding='valid', use_bias=True))
    adam = Adam(lr=0.0001)
    srcnn.compile(optimizer=adam, loss='mean_squared_error', metrics=['mean_squared_error'])
    return srcnn

def predict_image(path):
    srcnn=build_model()
    srcnn.load_weights("model-weights/srcnn2.h5")
    img = cv2.cvtColor(path, cv2.COLOR_BGR2YCrCb)
    shape = img.shape
    Y_img = cv2.resize(img[:, :, 0], (int(shape[1] / 2), int(shape[0] /2)), cv2.INTER_CUBIC)
    Y_img = cv2.resize(Y_img, (shape[1], shape[0]), cv2.INTER_CUBIC)
    img[:, :, 0] = Y_img
    img = cv2.cvtColor(img, cv2.COLOR_YCrCb2BGR)

    Y = np.zeros((1, img.shape[0], img.shape[1], 1), dtype=float)
    Y[0, :, :, 0] = Y_img.astype(float) / 255.
    pre = srcnn.predict(Y, batch_size=1) * 255.
    pre[pre[:] > 255] = 255
    pre[pre[:] < 0] = 0
    pre = pre.astype(np.uint8)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    img[6: -6, 6: -6, 0] = pre[0, :, :, 0]
    img = cv2.cvtColor(img, cv2.COLOR_YCrCb2BGR)
    return img
