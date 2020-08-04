from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()

try:
	browser.get(link)
	input1 = browser.find_element_by_css_selector('div .first_block div.first_class>input')
	input1.send_keys('Alex')
	
	input2 = browser.find_element_by_css_selector('div.first_block div:nth-child(2) input')
	input2.send_keys('Vyder')
	
	input3 = browser.find_element_by_css_selector('div.first_block div:nth-child(3) input')
	input3.send_keys('example@list.ru')
	
	button = browser.find_element_by_xpath('//button[text()="Submit"]')
	button.click()
	
	#проверяем, что зарегались
	time.sleep(5)
	
	#находим элемент ассерта по заголовку
	welcome_text_elt = browser.find_element_by_tag_name("h1")
	#присваивает тексту отдельную переменную
	welcome_text = welcome_text_elt.text
	
	# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
	assert "Congratulations! You have successfully registered!" == welcome_text
	
	
	
finally:
	time.sleep(10)
	browser.quit()
	
