import os
import cv2
from mss import mss
import numpy as np
import keyboard

def preprocessing(img):
    img = cv2.Canny(img, threshold1=100, threshold2=200)
    return img
x =0

# captures dinosaur run game, designed for my personal computer (adjust coordinates resepctively)
def start():
    """
    Captures video feed frame by frame, 
    """

    sct = mss()

    coordinates = (355, 240, 895,400)

    

    def on_press_reaction(event):
        img = preprocessing(np.array(sct.grab(coordinates)))
        global x

        if event.name =='up':
            cv2.imwrite('./images/jump/fre_{0}.jpg'.format(x), img)           
            print('jump write')
            x += 1
    
        if event.name == 'down':
            cv2.imwrite('./images/duck/fre_{0}.jpg'.format(x), img)           
            print('duck')
            x += 1
    
        if event.name == 'a':
            cv2.imwrite('./images/ideal/fre_{0}.jpg'.format(x), img)           
            print('ideal')
            x += 1
    
        # break the video feed
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
    keyboard.on_press(on_press_reaction)

    while True:
        pass

