
<p align="center">
<a href="https://dscommunity.in">
	<img src="https://github.com/Data-Science-Community-SRM/template/blob/master/Header.png?raw=true" width=80%/>
</a>
	<h2 align="center"> Super Resolution Convolutional Neural Network  </h2>
	<img src="/images/Screenshot from 2020-11-05 15-41-18.png"/>
	<h4 align="center"> **This is the original abstract from the paper whose code I have tried to realise.** <h4>
<h4 style="font-weight:400">
We propose a deep learning method for single image super-resolution (SR). Our method directly learns an end-to-end mapping between the low/high-resolution images. The mapping is represented as a deep convolutional neural network (CNN) that takes the low-resolution image as the input and outputs the high-resolution one. We further show that traditional sparse-coding-based SR methods can also be viewed as a deep convolutional network. But unlike traditional methods that handle each component separately, our method jointly optimizes all layers. Our deep CNN has a lightweight structure, yet demonstrates state-of-the-art restoration quality, and achieves fast speed for practical on-line usage. We explore different network structures and parameter settings to achieve trade-offs between performance and speed. Moreover, we extend our network to cope with three color channels simultaneously, and show better overall reconstruction quality. 

Find the paper [here](https://arxiv.org/abs/1501.00092).</h4>
</p>

---
[![DOCS](https://img.shields.io/badge/Documentation-see%20docs-green?style=flat-square&logo=appveyor)](Documentation.md) 
  [![UI ](https://img.shields.io/badge/User%20Interface-Link%20to%20UI-orange?style=flat-square&logo=appveyor)](Images/web_app.png)

## Results 

<h3> Before Image : </h3>
<img src="/images/index.png" />
<h3> After Implementing SRCNN : </h3>
<img src="/images/index2.png" />

## Instruction to run

1. Run the following command:
```bash
pip install streamlit
```
2. Download the zip file and open the location of the file in your terminal to run the following command
```bash
streamlit run stream.py
```

## Contributors
<h4> Tarushi Pathak </h4>
<img src="https://media-exp1.licdn.com/dms/image/C5103AQEZiMZveCVrzg/profile-displayphoto-shrink_200_200/0?e=1609372800&v=beta&t=CTvf0yJcFJJgQHx85231szmrAibAG1wv0Xfakm_E7mg" style="height=50%;weight=50%"/>
<a href="https://github.com/tarushi98"><img src="https://img.icons8.com/material-sharp/24/000000/github.png"/></a>
<a href="https://www.linkedin.com/in/tarushi-pathak-6b7b5b177/"><img src="https://img.icons8.com/windows/32/000000/linkedin-2.png"/></a>




## License
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

<p align="center">
	Made with :heart: by the <a href="https://dscommunity.in">DS Community SRM</a>
</p>
