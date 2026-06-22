import cv2

img=cv2.imread("image.png")

cw=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
ccw=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Clockwise",cw)
cv2.imshow("Counter Clockwise",ccw)
cv2.waitKey(0)
