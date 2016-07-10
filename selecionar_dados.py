# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 12:33:16 2016

@author: victor
"""

import cv2
import os
from random import randint


def sliding_window(image, stepSize, windowSize):
	# slide a window across the image
	for y in range(0, image.shape[0], stepSize):
		for x in range(0, image.shape[1], stepSize):
			# yield the current window
			yield (x, y, image[y:y + windowSize[1], x:x + windowSize[0]])

#O trecho de código abaixo é responsável por retirar amostras de testes do GTSRB
path1 = "path/to/GTSRB_Final_Test_Images/GTSRB/Final_Test/Images/"  
dirs = os.listdir(path1)

p = 51000;

for i in range(0,3500):
    random = randint(0,(len(dirs)-1))
    path10 = path1 + dirs[random]
    image = cv2.imread(path10)
    image = cv2.cvtColor( image, cv2.COLOR_RGB2GRAY )
    name = "path/to/folder/test_limpo_positivos/"+ str(p) + '.jpg'
    cv2.imwrite(name,image)
    p = p+1
    
#o Trecho de código é responsável por recortas as 600 imagens do conjunto de treinamento para servir de exemplos negativos    
p = 3000   
path = "path/to/onde_econtra-setodas as 600 imagens de treinamento" 
dirs = os.listdir(path) 
(winW, winH) = (80, 80)   
for i in enumerate(dirs):
    
    path2 = path + '/' + i[1]
    print(path2)
    image = cv2.imread(path2)

    for(x,y,window) in sliding_window(image,stepSize=128,windowSize=(winW,winH)):
        if window.shape[0] != winH or window.shape[1] != winW:
            continue
        
        clone = image.copy()
        box = clone[y:(y+winH), x:(x+winW)]
        box = cv2.cvtColor( box, cv2.COLOR_RGB2GRAY )
        name = "path/to/folder/train_limpo_negativos_colorido/"+ str(p) + '.jpg'
        cv2.imwrite(name,box)
        p = p+1  
        
# O trecho de código abaixo é responsável por retirar do GTSRB os exemplos positivos
path1 = "path/to/GTSRB_Final_Training_Images/GTSRB/Final_Training/Images/"  
dirs = os.listdir(path1)
p = 85000
for i in enumerate(dirs):
    path = path1 + i[1] + '/'
    dirs11 = os.listdir(path)
    random = randint(0,(len(dirs11)-1))
    print("teste")
    for j in range(0,random):
        dirs1 = os.listdir(path)
        random_2 = randint(0,(len(dirs1)-1))
        path10 = path + dirs1[random_2]
        image = cv2.imread(path10)
        image = cv2.cvtColor( image, cv2.COLOR_RGB2GRAY )
        name = "path/to/folder/train_limpo_positivos_colorido/"+ str(p) + '.jpg'
        cv2.imwrite(name,image)
        os.remove(path10)
        p = p+1
        
# O trecho abaixo é responsável por retirar do conjunto que foi criado para o treinamento para compor  o conjunto que servirá para o teste.      
path_10 = "path/to/TrainIJCNN2013/exemplos/train_limpo_negativos_colorido/"
p = 150000
for i in range(0,9800):
    dirs_10 = os.listdir(path_10)
    random = randint(0,(len(dirs_10)-1))
    path10 = path_10 + dirs_10[random]
    image = cv2.imread(path10)
    
    name = "path/to/folder/test_limpo_negativos_colorido/"+ str(p) + '.jpg'
    cv2.imwrite(name,image)
    os.remove(path10)
    p = p+1
    


    
   
   


