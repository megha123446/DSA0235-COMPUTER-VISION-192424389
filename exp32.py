import cv2
v=cv2.VideoCapture('video.mp4')
fs=[]
while True:
 r,f=v.read()
 if not r: break
 fs.append(f)
for f in fs[::-1]:
 cv2.imshow('Reverse',f)
 if cv2.waitKey(30)==27: break