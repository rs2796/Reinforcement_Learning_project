import os
os.environ['PATH'] += ":"+"/usr/local/bin"
import graphviz, pydot

from keras.utils import plot_model
plot_model('pong_model.h5',show_shapes=True, to_file='model.png')

##from PIL import Image
##import numpy as np
##
##w, h = 512, 512
##data = np.zeros((h, w, 3), dtype=np.uint8)
##data[256, 256] = [255, 0, 0]
##img = Image.fromarray(data, 'RGB')
###img.save('my.png')
img.show()