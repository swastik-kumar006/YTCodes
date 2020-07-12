from os import system as o
import random
o('pip install selenium')
from random import randint as r
from selenium import webdriver
from getpass import getpass
colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
W ='\033[0m'
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

# Make Sure To Put THe Proper PLace fOR cHROMEdRIVER
# Replace All "\"with "\\" Or Else U will Face Error
driver = webdriver.Chrome("G:\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://en-gb.facebook.com/login/")

username = driver.find_element_by_id("email")
username.send_keys(login)

password = driver.find_element_by_id("pass")
password.send_keys(p)

submit = driver.find_element_by_id("loginbutton")
submit.submit()
print('DONE!!')

