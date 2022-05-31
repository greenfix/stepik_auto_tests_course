from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

source = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(source)

    wait = WebDriverWait(browser, 12)

    response = wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    browser.find_element(By.ID, "book").click()

    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(x))
    browser.find_element(By.ID, "solve").click()

    alert = browser.switch_to.alert
    print(alert.text)
    alert.accept()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

