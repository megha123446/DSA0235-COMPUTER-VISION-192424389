import cv2
img=cv2.imread("image1c.png",0)
edge=cv2.Canny(img,100,200)
cv2.imshow("Canny",edge)
cv2.waitKey(0)
