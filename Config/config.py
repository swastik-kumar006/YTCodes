from time import sleep as s
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
CHROME_DRIVER = './Config/chdriver/'
i = 1
chrome_options = Options()
prefs = {"download.default_directory": "./"}
chrome_options.add_argument("--window-size=1927x1083")
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
while i <= 500:
    print(f"Sent Views : {i}")
    driver.get('https://youtu.be/LAH2PEfcdIc')
    s(200)
    i += 1
