from selenium import webdriver
import time
import os 

try: 
    link = " http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("hello@gmail.com")

    # получаем путь к директории текущего исполняемого файла 
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'hello.txt')
    element = browser.find_element_by_css_selector(['type="file"'])
    element.send_keys(file_path)
    
    button = browser.find_element_by_id('submit')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()