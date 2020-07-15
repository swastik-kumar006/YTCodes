import random
from os import system as o
o('pip install selenium')
from time import sleep as s
from selenium import webdriver
from Config import CHROME_DRIVER
from selenium.webdriver.chrome.options import Options
from Config import GOOGLE_CHROME_BIN
i = 1
while i <= 50000:
    chrome_options = Options()
    prefs = {"download.default_directory": "./"}
    chrome_options.binary_location = GOOGLE_CHROME_BIN
    chrome_options.add_argument("--window-size=1927x1083")
    chrome_options.add_experimental_option("prefs", prefs)
    print(f"Sent Views : {i}")
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
    driver.get('https://youtu.be/LAH2PEfcdIc')
    s(250)
    i += 1
