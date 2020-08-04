from selenium import webdriver
import time
import math
def calc(x_element):
  return str(math.log(abs(12*math.sin(int(x_element.text)))))
try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()

    window_name = browser.window_handles[1]
    browser.switch_to.window(window_name)

    x_element = browser.find_element_by_id('input_value')
    x=calc(x_element)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(x)

    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()