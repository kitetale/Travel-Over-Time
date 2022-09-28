#https://github.com/jasmcaus/opencv-course/blob/master/Section%20%233%20-%20Faces/faces_train.py

#https://www.youtube.com/watch?v=yqkISICHH-U&ab_channel=NicholasRenotte

import os
import cv2 as cv
import numpy as np

path = "/Users/ashk/Desktop/ExCap/shoes-recognition/data"
label = sneakers

def create_train():
    for img in os.listdir(path):
        img_path = os.path.join(path,img)

        img_array = cv.imread(img_path)
        if img_array is None:
            continue

        gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


