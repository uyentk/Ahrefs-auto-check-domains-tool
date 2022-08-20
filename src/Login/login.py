from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"
url = "https://app.ahrefs.com/batch-analysis"
email = "hoibeokkk@rattlenhumbarnyc.com"
password = "teamasm10k"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(PATH, options= options)
driver.get(url)

def login_ahrefs():
    try:  
        txtUser = driver.find_element(By.NAME, 'email')
        txtUser.clear()
        txtUser.send_keys(email)
    except:
        pass
    txtPass = driver.find_element(By.NAME, 'password')
    txtPass.clear()
    txtPass.send_keys(password)
    driver.find_element(By.XPATH,"//button[@type='submit']").click()

