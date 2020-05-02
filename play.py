from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import ai_player1

driver = webdriver.Chrome()
driver.set_network_conditions(offline=True, latency=0,download_throughput=500 * 1024,  upload_throughput=500 * 1024 )
driver.get('http://www.google.com/')
time.sleep(2)

# main page to send key commands to
page = driver.find_element_by_class_name('offline')

# start game
page.send_keys(u'\ue00d')

# controls the dinosaur
while True:
   ai_player1.predict(page) 
    
