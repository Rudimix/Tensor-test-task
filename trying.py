from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import requests
import time

# Используем Chrome для доступа к сайту
driver = webdriver.Chrome()
url ='https://sbis.ru/'
driver.get(url)
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//a[text()="Контакты"]').click()
driver.find_element(By.XPATH, '//a[@href="https://tensor.ru/"]/img[1]').click()
windows=driver.window_handles
driver.switch_to.window(windows[1])
strengthInPeople = driver.find_element(By.XPATH, "//div/p[contains(text(), 'Сила в людях')]")
strengthInPeople.find_element(By.XPATH, '//a[contains(@href,"/about")]').click()
blockWorking=driver.find_element(By.XPATH, "//div[contains(@class, 'tensor_ru-About__block3')]")
images=blockWorking.find_elements(By.CLASS_NAME, 'tensor_ru-About__block3-image-wrapper')
sizes=[[],[]]

for image in images:
    size= [image.size['width'], image.size['height']]
    sizes[0].append(size[0])
    sizes[1].append(size[1])

if len(set(sizes[0]))==1 and len(set(sizes[1]))==1:
    print("Все изображения одинаковые")
else:
    print("Не все изображения одинаковые")
 