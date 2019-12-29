# -*- coding: utf-8 -*-
'''
Robert Sobel filter
'''

import skimage
import numpy as np
import matplotlib.pyplot as plt


a=skimage.data.checkerboard()
edges=skimage.filters.roberts(a)
lap=skimage.filters.laplace(a)
gaus=skimage.filters.gaussian(a)
pre=skimage.filters.prewitt(a)
#wei=skimage.filters.wiener(a)
print(a)
print('\n---------------------------------------')
print(edges)
print('\n---------------------------------------')
print(lap)
print('\n----------------------------------------')
print(pre)

ip=skimage.io.imsave('datae.jpg',a)
op1=skimage.io.imsave('rob1.jpg',edges)
op2=skimage.io.imsave('lap.jpg',lap)
op3=skimage.io.imsave('gauss.jpg',gaus)
op4=skimage.io.imsave('pre.jpg',pre)