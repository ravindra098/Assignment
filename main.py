import cv2
import numpy as np
import os

# set video file path of input video with name and extension and setting 5 frames per second
FPS = 5
vid = cv2.VideoCapture('video.mp4')
vid.set(cv2.CAP_PROP_FPS, FPS)


if not os.path.exists('images'):
    os.makedirs('images')

currentframe = 0

#for frame identity
index = 0
while(True):
    # Extract images
    ret, frame = vid.read()


    # Saves images
    name = './images/frame' + str(index) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # next frame
    index += 1

    # specify the number of frames here
    if index == 75:
    	break
