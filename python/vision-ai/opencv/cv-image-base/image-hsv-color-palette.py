#!/usr/bin/env python

'''
HSV-BLACK  H(0/180) S(0/255) V(0/46)
HSV-GREY   H(0/180) S(0/43) V(46/220)
HSV-WHITE  H(0/180) S(0/30) V(221/255)
HSV-RED    H(0/10)/H(156/180) S(43/255) V(46/255)
HSV-ORANGE H(11/25) S(43/255) V(46/255)
HSV-YELLOW H(26/34) S(43/255) V(46/255)
HSV-GREEN  H(35/77) S(43/255) V(46/255)
HSV-CYAN   H(78/99) S(43/255) V(46/255)
HSV-BLUE   H(100/124) S(43/255) V(46/255)
HSV-PINK   H(125/155) S(43/255) V(46/255)
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt


def unit_image_create(width, height):
    #create a black use numpy,size is:512*512
    img_hsv = np.zeros((width, height, 3), np.uint8)
    #fill the image with white
    img_hsv.fill(255)
    return img_hsv

def unit_image_draw_text(image, rect, color_name):
    fontFace  = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    thickness = 2
    fontSize  = cv2.getTextSize(color_name, fontFace, fontScale, thickness)
    place     = (rect[0]+30, rect[1]+int((fontSize[1]+rect[3])/2))
    image     = cv2.putText(image, color_name, place, cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    return image

def unit_image_draw(image, rect, lower, upper, color_name):
    count = upper[1]-lower[1];
    delta_h = (upper[0]-lower[0]+1) / count
    delta_s = (upper[1]-lower[1]+1) / count
    delta_v = (upper[2]-lower[2]+1) / count
    delta_w = (rect[2]-rect[0]+1) / count
    for idx in range(0, int(count)):
        color = (int(lower[0] + idx*delta_h), int(lower[1] + idx*delta_s), int(lower[2] + idx*delta_v))
        image = cv2.rectangle(image, (rect[0] + int(idx*delta_w), rect[1], int(delta_w+0.5), rect[3]), color, -1)

    return unit_image_draw_text(image, rect, color_name);

def unit_image_draw_contours(frame, contours):
    for contour in contours:
        roi_rect = cv2.boundingRect(contour)
        roi_area = cv2.contourArea(contour)
        cv2.rectangle(frame, roi_rect, (255,255,0), 3)

def unit_image_find_contours(frame, lower, upper):
    img_mask = cv2.inRange(img_hsv, lower, upper)

    # morphology morph
    element  = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15), (-1, -1))
    img_mask = cv2.morphologyEx(img_mask, cv2.MORPH_OPEN, element)
 
    # morphology erode
    img_kernel = np.ones((3,3), np.uint8);
    img_mask   = cv2.erode(img_mask, img_kernel)
    
    # morphology dilate
    img_kernel = np.ones((10,10),np.uint8);
    img_mask   = cv2.dilate(img_mask, img_kernel, iterations = 1)
    contours, hierarchy = cv2.findContours(img_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    unit_image_draw_contours(frame, contours)


if __name__ == '__main__':
    img_hsv = unit_image_create(1800, 1000);
    # HSV-RED
    img_hsv = unit_image_draw(img_hsv, (0,   0, 1600, 80), (0,   43, 46), (10, 255, 255), "HSV-RED");
    # HSV-ORANGE
    img_hsv = unit_image_draw(img_hsv, (0, 100, 1600, 80), (11,  43, 46), (25, 255, 255), "HSV-ORANGE");
    # HSV-YELLOW
    img_hsv = unit_image_draw(img_hsv, (0, 200, 1600, 80), (26,  43, 46), (34, 255, 255), "HSV-YELLOW");
    # HSV-GREEN
    img_hsv = unit_image_draw(img_hsv, (0, 300, 1600, 80), (35,  43, 46), (77, 255, 255), "HSV-GREEN");
    # HSV-CYAN
    img_hsv = unit_image_draw(img_hsv, (0, 400, 1600, 80), (78,  43, 46), (99, 255, 255), "HSV-CYAN");
    # HSV-BLUE
    img_hsv = unit_image_draw(img_hsv, (0, 500, 1600, 80), (100, 43, 46), (124, 255, 255), "HSV-BLUE");
    # HSV-PINK
    img_hsv = unit_image_draw(img_hsv, (0, 600, 1600, 80), (125, 43, 46), (155, 255, 255), "HSV-PINK");
    # HSV-BLACK
    img_hsv = unit_image_draw(img_hsv, (0, 700, 1600, 80), (0,   0,   0), (180, 255, 46), "HSV-BLACK");
    # HSV-GRAY
    img_hsv = unit_image_draw(img_hsv, (0, 800, 1600, 80), (0,   0,  46), (180, 43, 220), "HSV-GRAY");
    # HSV-WHITE
    img_hsv = unit_image_draw(img_hsv, (0, 900, 1600, 80), (0,   0, 221), (180, 30, 255), "HSV-WHITE");
    
    unit_image_find_contours(img_hsv, np.array([100,  106,  105]), np.array([124,  255,  255]))
    img_rgb = cv2.cvtColor(img_hsv,cv2.COLOR_HSV2BGR)
    # Displaying the image 
    cv2.imshow("HSV-Color-Palette", img_rgb);
    cv2.waitKey(0);