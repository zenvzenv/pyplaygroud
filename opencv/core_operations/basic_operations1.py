import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('../messi.jpg')
# 获取该图片的 100，100 位置的像素的 BGR 像素
px = img[100, 100]
print(px)
# 只获取蓝色数值
# 最后一位表示索引伟，0-B,1-G,2-R
blue = img[100, 100, 0]
print(blue)

# 对特定像素进行复制
px = [255, 255, 255]
print(px)

# 使用 numpy 获取像素点和设置像素点会更好
red = img.item(10, 10, 2)
print(red)
img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))

# 获取图片的基本信息
print(img.shape)

# 获取图片有多少个像素点
print(img.size)

# 获取像素数据类型
print(img.dtype)

# ball = img[280:340, 330:390]
# img[273:333, 100:160] = ball

# 拆分通道
b, g, r = cv.split(img)
img = cv.merge((b, g, r))

BLUE = [255, 0, 0]
replicate = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REFLECT_101)
warp = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_WRAP)
# 给图片加上边框
constant = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=BLUE)

plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REPLICATE')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REPLICATE101')
plt.subplot(235), plt.imshow(warp, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')
plt.show()

# cv.imshow('img', img)
# cv.waitKey(0)
# cv.destroyAllWindows()
