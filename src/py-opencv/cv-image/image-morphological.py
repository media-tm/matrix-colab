#!/usr/bin/env python

'''
形态学转换原理：
一般情况下对二值化图像进行操作。
需要两个参数，一个是原始图像，第二个被称为结构化元素或者核，它是用来决定操作的性质的。
基本操作为腐蚀和膨胀，他们的变体构成了开运算，闭运算，梯度等。
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

image= cv2.imread('color-earth.png',0)
# 5x5 kernel
kernel = np.ones((5,5),np.uint8)
# OpenCV2腐蚀
erosion = cv2.erode(image, kernel, iterations=1)
#  OpenCV2膨胀
dilation = cv2.dilate(image, kernel, iterations=1)
#  OpenCV2开运算，先腐蚀在膨胀
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
#  OpenCV2闭运算，先膨胀在腐蚀
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
#  OpenCV2形态学梯度，腐蚀和膨胀的差别
gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
#  OpenCV2礼貌，开运算后与原图的差
tophat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
#  OpenCV2黑帽， 闭运算后与原图的差
blackhat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

plt.subplot(2,4,1), plt.imshow(image,cmap='gray')
plt.title('source'), plt.xticks([]),plt.yticks([])
plt.subplot(2,4,2),plt.imshow(erosion,cmap='gray')
plt.title('cv2.erode'), plt.xticks([]),plt.yticks([])
plt.subplot(2,4,3),plt.imshow(dilation,cmap='gray')
plt.title('cv2.dilate'), plt.xticks([]),plt.yticks([])
plt.subplot(2,4,4),plt.imshow(opening,cmap='gray')
plt.title('MORPH_OPEN'), plt.xticks([]),plt.yticks([])
plt.subplot(2,4,5), plt.imshow(closing,cmap='gray')
plt.title('MORPH_CLOSE'),plt.xticks([]),plt.yticks([])
plt.subplot(2,4,6), plt.imshow(gradient,cmap='gray')
plt.title('MORPH_GRADIENT'),plt.xticks([]),plt.yticks([])
plt.subplot(2,4,7), plt.imshow(tophat,cmap='gray')
plt.title('MORPH_TOPHAT'),plt.xticks([]),plt.yticks([])
plt.subplot(2,4,8), plt.imshow(blackhat,cmap='gray')
plt.title('MORPH_BLACKHAT'),plt.xticks([]),plt.yticks([])

plt.show()


