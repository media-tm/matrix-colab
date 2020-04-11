#!/usr/bin/env python

'''
图像梯度原理：
OpenCV提供了三种不同的梯度滤波器(高通滤波器)：Sobel，Scharr和Laplacian。
Sobel和Scharr是求一阶或二阶导数。
Scharr是对Sobel(使用小的卷积核求解梯度角度时)的优化，Laplacian是求二阶导数。
https://www.kancloud.cn/aollo/aolloopencv
'''

import cv2
import numpy
from matplotlib import pyplot as plt

img = cv2.imread('color-earth.png',0)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(img,cmap='gray')
plt.title('original'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap='gray')
plt.title('laplacian'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap='gray')
plt.title('Sobel X'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap='gray')
plt.title('Sobel Y'),plt.xticks([]),plt.yticks([])

plt.show()