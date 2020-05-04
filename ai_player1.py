from tensorflow.keras.models import load_model
import time
from mss import mss
import numpy as np
import cv2
import pyautogui
# coordinates  =(365, 240, 685,400)

# def cor30(): 
#     coordinates = (400, 240, 720,400)
#     return coordinates
    
model = load_model('D:/Project/model.hdf5')

def predict(game_element):
   start =0   
   while True:
    

    sct = mss()

    if start < 70.0:
        coordinates  =(360, 240, 680,400)
        
    else:
        coordinates = (420, 240, 740,400)
    img = np.array(sct.grab(coordinates))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img, threshold1=100, threshold2=200)
    img = img[np.newaxis, :, :, np.newaxis]
    img = np.array(img)



    # model prediction
    y_prob = model.predict(img)
    prediction = y_prob.argmax(axis=-1)
    
    print(start)
    if prediction == 2:
        # jump        
        game_element.send_keys(u'\ue013')
        print('jump')
        time.sleep(.03)
        
    if prediction == 1:
        print('ideal')
        start = time.perf_counter()

        # do nothing
        pass
    if prediction == 0:
        print('duck') 
        pyautogui.keyDown('down')
        time.sleep(0.25)
        pyautogui.keyUp('down')

       