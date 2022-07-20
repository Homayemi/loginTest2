from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://the-internet.herokuapp.com/')

driver.find_element(By.LINK_TEXT, "Form Authentication").click()
driver.find_element(By.NAME, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.TAG_NAME, "button").click()
message = driver.find_element(By.ID, "flash").text
assert "You logged into a secure area!" in message
print("Test passed!!!")
