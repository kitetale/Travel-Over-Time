#https://www.youtube.com/watch?v=u70unqjZuI8

import cv2

rAvg, gAvg, bAvg = None, None, None

total = 0

vid = cv2.VideoCapture("crop.mp4")

while True:
    ret, frame = vid.read()

    if ret == False: break

    total += 1

    B,G,R = cv2.split(frame.astype("float"))

    if rAvg is None:
        rAvg = R
        gAvg = G 
        bAvg = B
    else :
        rAvg = cv2.accumulateWeighted(R,rAvg,1/total)
        gAvg = cv2.accumulateWeighted(G,gAvg,1/total)
        bAvg = cv2.accumulateWeighted(B,bAvg,1/total)

avg = cv2.merge([bAvg,gAvg,rAvg]).astype("uint8")

cv2.imwrite("sidewalk_long_exposure.png",avg)

vid.release()
