# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 01:05:20 2019

@author: KIIT
"""
# importing needed libraries
import cv2
def main():
    events = [i for i in dir(cv2) if 'EVENT' in i]
    print(events)

if __name__ == "__main__":
    main()