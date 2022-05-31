from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

source = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(source)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")

    box = browser.find_element(By.ID, "robotCheckbox")

    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    x = browser.find_element(By.ID, "input_value")  
    browser.find_element(By.ID, "answer").send_keys(calc(x.text))

    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

