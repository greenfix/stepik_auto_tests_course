from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math
from selenium.webdriver.support.ui import Select

# source = "http://suninjuly.github.io/selects1.html"
source = " http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(source)

    x = browser.find_element(By.ID, "num1")
    y = browser.find_element(By.ID, "num2")
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(int(x.text) + int(y.text)))
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
