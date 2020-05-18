from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://localhost:8000')
#print (driver.title)
#driver.quit()

assert 'Django' in driver.title