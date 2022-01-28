import numpy as np
import cv2 as cv

# 创建空白画布
img = np.zeros((512, 512, 3), np.uint8)
# 画一条直线
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# 画一个矩形
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# 画一个圆
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)
# 画一个椭圆
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
# 画折线
cv.polylines(img, [pts], True, (0, 255, 255))
# 写字
font = cv.FONT_HERSHEY_COMPLEX
cv.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv.LINE_AA)
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
