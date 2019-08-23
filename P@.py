# -*- coding: utf-8 -*-
"""
Image filtering(both low)
"""

import cv2
import matplotlib.pylab as plt
import numpy as np

img = cv2.imread('KT.jpg',0)
print(img)
cv2.imshow('Klay Thompson',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Klay_T.png',img)

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))
median = cv2.medianBlur(img,5)

plt.imshow(dst)
plt.title('filtered image')
plt.show()

plt.imshow(blur)
plt.title('Average filtering using kernel')
plt.show()

plt.imshow(median)
plt.title('Median filtered image')
plt.show()