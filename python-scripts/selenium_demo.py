from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://demo.com")
forgot = driver.find_element_by_id('loginForm:j_idt23')
forgot.click()
email = driver.find_element_by_id('forgotPass:mailId')
email.send_keys('rodrigo@demo.com')
send = driver.find_element_by_id('forgotPass:j_idt32')
send.click()
