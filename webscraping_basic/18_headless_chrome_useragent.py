from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument('window-size=1920x1080')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36')

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent'
browser.get(url)

detected_value = browser.find_element(By.ID, 'detected_value').find_element(By.CSS_SELECTOR, 'a').text
print(detected_value)

browser.quit()
