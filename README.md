This is pytorch implementation for paper **[Perceptual Losses for Real-Time Style Transfer and Super-Resolution](http://cs.stanford.edu/people/jcjohns/eccv16/)**

I have test several upsampling layer. "pixelshuffle"， “nearest”. It seems the type of upsampling does not matter.

---
Content Image & Style Image
<div align='center'>
      <img src='https://raw.githubusercontent.com/martinambition/fast-neural-style-pytorch/master/in/trump.jpeg' height="300px" width="300px"/>
      <img src='https://raw.githubusercontent.com/martinambition/fast-neural-style-pytorch/master/images/style-images/candy.jpg' height="300px" width="300px"/>
</div>


---
Nearest Upsampling

<img src='https://raw.githubusercontent.com/martinambition/fast-neural-style-pytorch/master/out/nearest.jpg' height="300px" width="300px"/>

Pixelshuffle Upsampling

<img src='https://raw.githubusercontent.com/martinambition/fast-neural-style-pytorch/master/out/pixelshuffle.jpg' height="300px" width="300px"/>


---
Loss 
![image](https://raw.githubusercontent.com/martinambition/fast-neural-style-pytorch/master/loss.png)