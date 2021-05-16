from socket import EWOULDBLOCK
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import passwdManager

#Setup
url = 'https://mitt.kau.se/login/sv'
ops = webdriver.DesiredCapabilities.CHROME.copy()
ops["detach"] = True
driver = webdriver.Chrome(desired_capabilities=ops)
driver.get(url)

#Click login button
driver.find_element_by_class_name('btn-warning').click()

#Login
usernameInput = driver.find_element_by_id('username')
passwordInput = driver.find_element_by_id('password')
loginButton = driver.find_element_by_class_name('form-button')

usernameInput.send_keys(passwdManager.decrypt('u'))
passwordInput.send_keys(passwdManager.decrypt('p'))
loginButton.click()

s = input()

