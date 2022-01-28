import cv2 as cv
import numpy as np

flag = [i for i in dir(cv) if i.startswith("COLOR_")]
print(flag)

# 使用摄像头
cap = cv.VideoCapture(0)
# 读取视频
# cap = cv.VideoCapture('C:/Users/zw305/Desktop/facewap/wzr_video/73f714aa62176175bf4fbc02b29384db.mp4')
while 1:
    _, frame = cap.read()
    # 将颜色转成 HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # lower_blue = np.array([110, 50, 50])
    # lower_blue = np.array([0, 0, 252])
    # upper_blue = np.array([130, 255, 255])

    lower_blue = np.array([0, 0, 255])
    upper_blue = np.array([130, 255, 255])

    # 阈值 HSV 图像以仅获得蓝色
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # 按位与掩码和原始图像
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
