from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считать значение х y
    x = browser.find_element_by_id('num1').text
    y = browser.find_element_by_id('num2').text
    d=str(int(x)+int(y))
    #выбрать список
    select = Select(browser.find_element_by_css_selector("select"))
    select.select_by_value('d') # ищем элемент 
    
   
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()