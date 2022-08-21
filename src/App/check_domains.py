from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyperclip
import pandas as pd

PATH = "C:\Program Files (x86)\chromedriver.exe"
url = "https://app.ahrefs.com/batch-analysis"
email = "hoibeokkk@rattlenhumbarnyc.com"
password = "teamasm10k"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(PATH, options= options, service = Service(ChromeDriverManager().install()))
driver.get(url)

df = pd.read_csv("src/assets/input.csv", header = None)
df.columns = ["Domains"]

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

def get_domains():
    for i in df["Domains"]:
        # Copy domain name
        pyperclip.copy(i)
        clipboard_text= pyperclip.paste()

        # Paste domain name in batch analysis form
        txtDomain = driver.find_element(By.XPATH, "//textarea[@placeholder='Enter up to 200 URLs (one URL per line)']")
        txtDomain.send_keys(clipboard_text)
        txtDomain.send_keys(Keys.ENTER)

        # print(clipboard_text)
        # Empty the clipboard text
        clipboard_text = ""


login_ahrefs()
get_domains()

