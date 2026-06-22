import cv2, numpy as np

v=cv2.VideoCapture("video.mp4")

while True:
    r,f=v.read()
    if not r: break

    h,w=f.shape[:2]

    p1=np.float32([[0,0],[w,0],[0,h],[w,h]])
    p2=np.float32([[50,50],[w-50,0],[0,h],[w,h-50]])

    M=cv2.getPerspectiveTransform(p1,p2)
    out=cv2.warpPerspective(f,M,(w,h))

    cv2.imshow("Video",out)

    if cv2.waitKey(25)==27: break

v.release()
cv2.destroyAllWindows()
