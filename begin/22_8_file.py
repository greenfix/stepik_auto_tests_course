from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
from selenium.webdriver.support.ui import Select
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

source = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(source)

    current_dir = os.path.abspath(os.path.dirname(__file__))   
    file_path = os.path.join(current_dir, 'file.txt')          

    browser.find_element(By.NAME, "firstname").send_keys('Firsr')
    browser.find_element(By.NAME, "lastname").send_keys('Last')
    browser.find_element(By.NAME, "email").send_keys('first@last.com')
    browser.find_element(By.NAME, "file").send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

