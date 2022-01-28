import cv2

img = cv2.imread(r'tiga.jpg')
cv2.imshow('tiga', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('tiga.jpg', img)
    cv2.destroyAllWindows()
