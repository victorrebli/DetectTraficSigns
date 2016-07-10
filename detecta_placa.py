"""
Created on Sun Jun  5 19:31:31 2016

@author: root
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
import imutils
import os

def sliding_window(image, stepSize, windowSize):
	# slide a window across the image
	for y in range(0, image.shape[0], stepSize):
		for x in range(0, image.shape[1], stepSize):
			# yield the current window
			yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])
   
   
def pyramid(image, scale=1.5, minSize=(30, 30)):
	# yield the original image
	yield image
 
	# keep looping over the pyramid
	while True:
		# compute the new dimensions of the image and resize it
		w = int(image.shape[1] / scale)
		image = imutils.resize(image, width=w)
 
		# if the resized image does not meet the supplied minimum
		# size, then stop constructing the pyramid
		if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
			break
 
		# yield the next image in the pyramid
		yield image


plt.rcParams['figure.figsize'] = (10, 10)        
plt.rcParams['image.interpolation'] = 'nearest'  
plt.rcParams['image.cmap'] = 'gray'
import caffe 
caffe.set_mode_cpu()
model_def = 'path/to/caffe/models/meu_modelo/deploy.prototxt'
model_weights = 'path/to/caffe/models/meu_modelo/teste/train_iter_12000.caffemodel'
net = caffe.Net(model_def,      # defines the structure of the model
                model_weights,  # contains the trained weights
                caffe.TEST)     # use test mode (e.g., don't perform dropout)
mu = np.load('path/to/caffe/python/caffe/imagenet/ilsvrc_2012_mean.npy')
mu = mu.mean(1).mean(1)                
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))  # move image channels to outermost dimension
transformer.set_mean('data', mu)            # subtract the dataset-mean value in each channel
transformer.set_raw_scale('data', 255)      # rescale from [0, 1] to [0, 255]
transformer.set_channel_swap('data', (2,1,0))  # swap channels from RGB to BGR
net.blobs['data'].reshape(50,        # batch size
                          3,         # 3-channel (BGR) images
                          227, 227)  # image size is 227x227
                             
path1 = "path/to/teste_jpg/"
dirs = os.listdir(path1)
p = 0
for i in range(0,len(dirs)):
  name = "path/to/teste_jpg/" + dirs[i] 
  image = caffe.io.load_image(name)
  img = cv2.imread(name)
  c = 0
  t=0
  (winW, winH) = (70, 70)
  tel = dict()

  m = 0
  
  for resized in pyramid(image, scale=1.5):
    m = m + 1  
    for(x,y,window) in sliding_window(resized,stepSize=32,windowSize=(winW,winH)):
        if window.shape[0] != winH or window.shape[1] != winW:
            continue
        
        clone = resized.copy()
        box = clone[y:(y+winH), x:(x+winW)]
        
        transformed_image = transformer.preprocess('data', box)
        net.blobs['data'].data[...] = transformed_image
        output = net.forward()
        output_prob = output['prob'][0]
        if output_prob.argmax() == 0:
            c = c + 1
            tel[c] = [y,(y+winH),x,(x+winW),resized.shape,m]
        print('predicted class is:', output_prob.argmax())
    
   
  for i in range(1,len(tel)+1):
       cor = tel[i]
    
       for j in range(1,cor[5]):
         if cor[5] != 1: 
          cor[2] = cor[2] * 1.5
          cor[2] = int(cor[2])
          cor[0] = cor[0] * 1.5
          cor[0] = int(cor[0])
          cor[3] = cor[3] * 1.5
          cor[3] = int(cor[3])
          cor[1] = cor[1] * 1.5
          cor[1] = int(cor[1])
      
       cv2.rectangle(img, (cor[2],cor[0]), (cor[3],cor[1]), (0,255,0), 2)
       name_1 = "path/to/teste_jpg/" + str(p) + ".jpg"
       cv2.imwrite(name_1,img)
       p = p + 1
