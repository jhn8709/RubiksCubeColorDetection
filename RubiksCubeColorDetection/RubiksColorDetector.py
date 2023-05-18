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

img_list = ['RubiksImagesPNG/IMG_1300.png',
            'RubiksImagesPNG/IMG_1301.png',
            'RubiksImagesPNG/IMG_1302.png',
            'RubiksImagesPNG/IMG_1303.png',
            'RubiksImagesPNG/IMG_1304.png',
            'RubiksImagesPNG/IMG_1305.png']

rubiks_sides = {
    "side1": [],
    "side2": [],
    "side3": [],
    "side4": [],
    "side5": [],
    "side6": [],
    }

black = (0, 0, 0)

# lower bound and upper bound for Green color
lower_bound_g = np.array([45, 80, 80])
upper_bound_g = np.array([65, 255, 255])
# lower bound and upper bound for Red color
lower_bound_r = np.array([170, 80, 80])
upper_bound_r = np.array([180, 255, 255])
# lower bound and upper bound for Blue color
lower_bound_b = np.array([105, 80, 80])
upper_bound_b = np.array([120, 255, 255])
# lower bound and upper bound for Yellow color
lower_bound_y = np.array([20, 80, 80])
upper_bound_y = np.array([30, 255, 255])
# lower bound and upper bound for Orange color
lower_bound_o = np.array([8, 80, 80])
upper_bound_o = np.array([16, 255, 255])
# lower bound and upper bound for White color
lower_bound_w = np.array([10, 0, 80])
upper_bound_w = np.array([20, 70, 255])


side_list = list(rubiks_sides)

cols = [77, 150, 221]
rows = [132, 202, 277]

hue_list = []
saturation_list = []

for i in range(len(img_list)):
    img = cv.imread(img_list[i]) # load in image
    #print(type(img))
    resized_img = rescaleFrame(img, scale=0.1) # change size of image
    cv.imshow(side_list[i], resized_img) # show BGR image
    hsv = cv.cvtColor(resized_img, cv.COLOR_BGR2HSV) # convert BGR to HSV color space
    #cv.imshow('HSV', hsv) # show HSV image
    #hue_list = []
    #saturation_list = []
    for row in rows:
        for col in cols:
            hue_list.append(hsv[row, col, 0])
            saturation_list.append(hsv[row, col, 1])
    #print(hue_list)
    #print(saturation_list)
    cv.waitKey(0)
    #cv.destroyAllWindows()

inc = 0
for sides in side_list:
    for i in range(9):
        if saturation_list[inc] < 70:
            rubiks_sides[sides].append("white")
        else:
            rubiks_sides[sides].append(colorDetectionHue(hue_list[inc]))
        inc += 1

for sides in side_list:    
    print(sides, end=": ")
    print(rubiks_sides[sides])

cv.waitKey(0)
cv.destroyAllWindows()
    


