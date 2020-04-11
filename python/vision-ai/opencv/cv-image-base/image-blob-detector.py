#!/usr/bin/env python

'''
image-blob-detector.py
================

This is a demo that tracks color blob
This reads from file:blob-detector.jpg

Author: martin.cheng@rock-chips.com

Usage:
------
    None
'''

import cv2
import numpy as np

def unit_create_detector():
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()
    
    # Change thresholds
    params.minThreshold = 10;
    params.maxThreshold = 200;
    
    # Filter by Area.
    params.filterByArea = True
    params.minArea = 200
    
    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.1
    
    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.87
    params.maxConvexity = 1.00
    
    # Filter by Inertia
    params.filterByInertia = True
    params.minInertiaRatio = 0.01
    
    # Create a detector with the parameters
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
        detector = cv2.SimpleBlobDetector(params)
    else : 
        detector = cv2.SimpleBlobDetector_create(params)

    return detector

def unit_blob_detector(detector, frame):
    keypts = detector.detect(frame)
    
    # draw centers of all keypoints in new image
    blank = np.array([])
    cv2.drawKeypoints(frame, keypts, frame, color=(0,255,0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("frame", frame)

if __name__ == '__main__':
    frame = cv2.imread(cv2.samples.findFile("blob-detector.jpg"))
    detector = unit_create_detector()
    unit_blob_detector(detector, frame)

    cv2.waitKey(0)