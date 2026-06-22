import cv2

c=cv2.VideoCapture(0)
speed=100

while True:
    r,f=c.read()
    if not r: break

    cv2.imshow("Webcam",f)

    k=cv2.waitKey(speed)

    if k==ord('f'):
        speed=10      # Fast
    elif k==ord('s'):
        speed=100     # Slow
    elif k==27:
        break

c.release()
cv2.destroyAllWindows()
