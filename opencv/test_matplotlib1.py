import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('tiga.jpg', cv2.WINDOW_NORMAL)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
