from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import cap

driver = webdriver.Chrome()
driver.set_network_conditions(offline=True, latency=2, download_throughput=500 * 1024, upload_throughput=500 * 1024)
driver.get("https://www.google.com/")
action = ActionChains(driver)
action.pause(2)
action.send_keys(Keys.ARROW_UP)
action.perform()
time.sleep(2)
cap.start()




