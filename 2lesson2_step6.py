from selenium import webdriver
from math import*
import time

try: 
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    x_calc=str(log(abs(12*sin(int(x)))))
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(x_calc)
    browser.execute_script("window.scrollBy(0, 150);")
    option1 = browser.find_element_by_class_name('form-check-input')
    option1.click()
    browser.execute_script("window.scrollBy(0, 150);")
    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()
    browser.execute_script("window.scrollBy(0, 100);")
	#обавить поиск кнпки
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
