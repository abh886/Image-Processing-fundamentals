# -*- coding: utf-8 -*-
"""
Basics of image processing 1

In this program we will  see how to display an image
How to read values of each pixel
Saving the image into the system
Apply concepts like bilinear interpolation,FFT
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
#from PIL import Image

img = cv2.imread('KT.jpg',0)
print(img)
cv2.imshow('Klay Thompson',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Klay_t.png',img)
imgplot = plt.imshow(img, interpolation="bilinear")
plt.title('Image after bilinear interpolation')
plt.show()
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
imgplot1 = plt.imshow(img, interpolation="nearest")
plt.title('Image after nearest interpolation')
plt.show()
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)

magnitude_spectrum = 20*np.log(np.abs(fshift))
b=plt.imshow(magnitude_spectrum, cmap = 'cool')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()