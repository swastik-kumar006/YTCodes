from time import sleep as s
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
CHROME_DRIVER = '/app/.chromedriver/bin/chromedriver'
i = 1
chrome_options = Options()
prefs = {"download.default_directory": "./chromedriver.exe"}
chrome_options.add_argument("--window-size=1927x1083")
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
while i <= 500000:
    print(f"Sent Views : {i}")
    driver.get('https://www.youtube.com/watch?v=qUlHZt5kYLI=3s')
    s(250)
    i += 1
