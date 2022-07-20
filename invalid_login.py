from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://the-internet.herokuapp.com/')


driver.find_element(By.LINK_TEXT,"Form Authentication").click()
driver.find_element(By.NAME,"username").send_keys("thomas")
driver.find_element(By.ID,"password").send_keys("SecretPassword!")
driver.find_element(By.TAG_NAME, "button").click()
message = driver.find_element(By.ID, "flash").text
assert "Your username is invalid!" in message
print("Test passed!!!")
