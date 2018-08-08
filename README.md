This is pytorch implementation for paper **[Perceptual Losses for Real-Time Style Transfer and Super-Resolution](http://cs.stanford.edu/people/jcjohns/eccv16/)**

I have test several upsampling layer. "pixelshuffle",“nearest”. It seems the type of upsampling does not matter during the training.

---
#### Content Image & Style Image
<div>
      <img src='https://raw.githubusercontent.com/martinambition/fast-neural-style-pytorch/master/in/trump.jpeg' height="300px" width="300px"/>
      <img src='https://raw.githubusercontent.com/martinambition/fast-neural-style-pytorch/master/images/style-images/candy.jpg' height="300px" width="300px"/>
</div>


---
#### Nearest Upsampling

<img src='https://raw.githubusercontent.com/martinambition/fast-neural-style-pytorch/master/out/nearest.jpg' height="300px" width="300px"/>

#### Pixelshuffle Upsampling

<img src='https://raw.githubusercontent.com/martinambition/fast-neural-style-pytorch/master/out/pixelshuffle.jpg' height="300px" width="300px"/>


---
#### Loss with different upsampling

![image](https://raw.githubusercontent.com/martinambition/fast-neural-style-pytorch/master/loss.png)


