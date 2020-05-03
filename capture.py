import os
import cv2
from mss import mss
import numpy as np
import keyboard



# captures dinosaur run game, designed for my personal computer (adjust coordinates resepctively)
def start():
    """
    Captures video feed frame by frame, crops out unecessary dino and processes
    """

    sct = mss()

    coordinates = (350, 240, 670,400)


    x = 0
        
    while True:


        if keyboard.is_pressed('up arrow'): 
            img = np.array(sct.grab(coordinates))
            img = cv2.Canny(img, threshold1=100, threshold2=200)
            cv2.imwrite('./images/0jump/frm_{0}.jpg'.format(x), img)
            print('jump write'.format(x))
            x += 1

        if keyboard.is_pressed('down arrow'):
            img = np.array(sct.grab(coordinates))
            img = cv2.Canny(img, threshold1=100, threshold2=200)
            cv2.imwrite('./images/2duck/frm_{0}.jpg'.format(x), img)
            print('duck')
            x += 1

        
        if keyboard.is_pressed('a'):
            img = np.array(sct.grab(coordinates))
            img = cv2.Canny(img, threshold1=100, threshold2=200)
            cv2.imwrite('./images/ideal/frm_{0}.jpg'.format(x), img)
            print('ideal')
            x += 1


               
