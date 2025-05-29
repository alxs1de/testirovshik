from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid")

blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
blue_button.click()

sleep(5)

driver.quit()
