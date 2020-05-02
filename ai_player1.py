from tensorflow.keras.models import load_model
import time
import selenium
from mss import mss
import numpy as np
import cv2
import threading 
coordinates = (370, 240, 690,400)
def cor12(): 
    coordinates = (360, 240, 680,400) 
    return coordinates
def cor30(): 
    coordinates = (390, 240, 710,400)
   
    return coordinates

model = load_model('D:/Project/dino_326.h5')

start = time.time()
x =1
y=0
def predict(game_element):    
    sct = mss()
    #coordinates = (345, 240, 665,400)#dino_1
    #coordinates = (370, 240, 610,400)#dino_3
    #dino_326
    
    timer = threading.Timer(38.0, cor30)
    timer.start() 





    img = np.array(sct.grab(coordinates))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img, threshold1=100, threshold2=200)
    img = img[np.newaxis, :, :, np.newaxis]
    img = np.array(img)



    # model prediction
    y_prob = model.predict(img)
    prediction = y_prob.argmax(axis=-1)

    if prediction == 2:
        # jump
        #time.sleep(.07)
        game_element.send_keys(u'\ue013')
        print('TO THE SKIES')
        time.sleep(.04)
    if prediction == x:
        print('CHILL')
        # do nothing
        pass
    if prediction == y:
        print('DUCKS')
        # duck
        game_element.send_keys(u'\ue015')
        time.sleep(.2)