import cv2

v=cv2.VideoCapture("video.mp4")

while True:
    r,f=v.read()
    if not r: break
    cv2.imshow("Fast",f)
    if cv2.waitKey(10)==27: break

v.release()
cv2.destroyAllWindows()
