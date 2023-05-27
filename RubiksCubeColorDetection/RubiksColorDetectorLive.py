# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def colorDetectionHue(hue):
    if hue < 16:
        color = "orange"
    elif hue < 30:
        color = "yellow"
    elif hue < 65:
        color = "green"
    elif hue < 120:
        color = "blue"
    else:
        color = "red"
    
    return color

rubiks_sides = {
    "side1": [],
    "side2": [],
    "side3": [],
    "side4": [],
    "side5": [],
    "side6": [],
    }

# Reading Videos
capture = cv.VideoCapture(1) # Uses 2nd connected camera

side_list = list(rubiks_sides)

cols = [77, 150, 221] # location of pixel for 1st, 2nd, and 3rd column of cube
rows = [132, 202, 277] # location of pixel for 1st, 2nd, and 3rd row of cube

hue_list = []
saturation_list = []

while True:
    isTrue, frame = capture.read()
    #print(type(img))
    resized_f = rescaleFrame(frame, scale=0.3) # change size of image
    #cv.imshow(side_list[i], resized_img) # show BGR image (use this to set cols and rows list)
    hsv = cv.cvtColor(resized_f, cv.COLOR_BGR2HSV) # convert BGR to HSV color space
    #cv.imshow('HSV', hsv) # show HSV image
    for row in rows:
        for col in cols:
            hue_list.append(hsv[row, col, 0])
            saturation_list.append(hsv[row, col, 1])
    #print(hue_list)
    #print(saturation_list)
    cv.waitKey(0) # add code here to determine when next side should be detected
    #cv.destroyAllWindows()

inc = 0
for sides in side_list:
    for i in range(9):
        if saturation_list[inc] < 70: # white is the only color on the cube to have low saturation
            rubiks_sides[sides].append("white") 
        else:
            rubiks_sides[sides].append(colorDetectionHue(hue_list[inc])) # detect color by hue
        inc += 1

for sides in side_list:    
    print(sides, end=": ")
    print(rubiks_sides[sides])

    


