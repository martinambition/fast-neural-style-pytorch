
class Args(object):
    pass

args = Args()
args.epochs =2
args.batch_size =2
args.dataset ="D:\\MachineLearning\\Datas\\VOCdevkit\\VOC2007"
args.style_image ="D:\\MachineLearning\\SourceCode\\pytorch-examples\\fast_neural_style\\images\\style-images\\candy.jpg"
args.save_model_dir ="model"
args.image_size=256
args.style_size=None
args.cuda=1
args.seed=42
args.content_weight=1e5
args.style_weight=1e10
args.lr=1e-3
args.log_interval=20
args.checkpoint_interval=500
args.upsampling="pixelshuffle"





from neural_style import neural_style as nn
from IPython.display import Image
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import os
import time

fig, ax = plt.subplots()

args.upsampling="pixelshuffle"
loss_pixelshuffle = nn.train(args)
loss_pixelshuffle = np.array(loss_pixelshuffle)
ax.plot(loss_pixelshuffle[:,0], loss_pixelshuffle[:,1], label=args.upsampling)

args.upsampling="nearest"
loss_nearest = nn.train(args)
loss_nearest = np.array(loss_nearest)
ax.plot(loss_nearest[:,0], loss_nearest[:,1], label=args.upsampling)

ax.legend(loc=2); # upper left corner
ax.set_title('Loss');
plt.show()