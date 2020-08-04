from selenium import webdriver
import time
import math
import os 

try: 
    link = " http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считать значение х
    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    #заполнить значение
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    #отметить чекбокс
    option1 = browser.find_element_by_class_name('check-input')
    option1.click()
    #отметить радиобатон
    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()