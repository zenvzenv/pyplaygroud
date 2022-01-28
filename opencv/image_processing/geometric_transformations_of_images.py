import cv2 as cv
import numpy as np

img = cv.imread('../messi.jpg')
# res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)

# or
height, width = img.shape[:2]
res = cv.resize(img, (2*height, 2*width), interpolation=cv.INTER_CUBIC)

cv.imshow('res', res)
cv.waitKey(0)
cv.destroyAllWindows()

