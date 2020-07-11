from os import system as o
o('pip install selenium')
from selenium import webdriver
from getpass import getpass
colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
W='\033[0m'
def banner():
    x = r(0, 99999)
    y = str(x)
    print(random.choice(colors))
    print("______________________________")
    print("|         Blue  devil        |")
    print("|Telegram - t.me/AKASH_AM1   |")
    print("|Insta - @blue_devil_official|")
    print("|YT -  www.youtube.com/channel/UCro6gU2S9CrTmcOkAUBswww")
    print("|Subscribe &&  Li9ke         |")
    print(f"CURRENT ONLINE BOT USERS = {y}")
    print("------------------------------")
    print(W)
banner()
login = input("Enter in your username: ")
p = getpass("Enter your password: ")

driver = webdriver.Chrome("G:\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://en-gb.facebook.com/login/")

username_textbox = driver.find_element_by_id("email")
username_textbox.send_keys(login)

password_textbox = driver.find_element_by_id("pass")
password_textbox.send_keys(p)

login_button = driver.find_element_by_id("loginbutton")
login_button.submit()
print('DONE!!')
