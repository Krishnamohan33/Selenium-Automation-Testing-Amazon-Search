from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()


driver.get("https://www.amazon.in/")
driver.maximize_window()


search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("Krishnamohan Yagneswaran")


search_box.send_keys(Keys.RETURN)


time.sleep(5)

driver.quit()
print("Search completed successfully!")
