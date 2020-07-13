import random
import os
from os import path as p
from random import randint as r
from selenium import webdriver
from time import sleep as s
colors=['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m']
W ='\033[0m'
def banner():
    os.system('COLOR 02')
    x = str(r(0, 999))
    print("______________________________")
    print("|         Blue  devil        |")
    print("|Telegram - t.me/AKASH_AM1   |")
    print("|Insta - @blue_devil_official|")
    print("|YT -  www.youtube.com/channel/UCro6gU2S9CrTmcOkAUBswww")
    print("|Subscribe &&  Li9ke         |")
    print(f"CURRENT ONLINE BOT USERS = {x}")
    print("------------------------------")
def vbanner():
    logo = ("                                                                          \n"
            "           /~~~~~~\ \n"
            "          /        \                            |---------    |          |\n"
            '         /          \     |  /      /~~~~~\     |             |          |\n'
            '        /============\    | /      /       \    |             |          |\n'
            '       /              \   |/      /_________\   |________|    |==========|\n'
            '      /                \  |\     /           \           |    |          |\n'
            "     /                  \ | \   /             \          |    |          |\n"
            "                                                ---------|    |          |\n"
            "        YT -  www.youtube.com/channel/UCro6gU2S9CrTmcOkAUBswww\n")
    print(f'{random.choice(colors)}{logo}{W}')
def start():
    banner()
    vid = input(f'{random.choice(colors)}ENTER VIDEO LINK : {W}')
    if 'youtu' not in vid and 'https://' not in vid:
        print(f'{random.choice(colors)}[ERROR] WRONG LINK\n[ERROR] ONLY YT LINK ACCEPTED #!!#\n')
        print(f'RETRYING...{W}')
        s(2)
        os.system('CLS')
        start()
    elif 'youtu' in vid and 'https://' in vid:
        cd = input(f"{random.choice(colors)}ENTER THE PLACE OF CHROMRDRIVER OR PRESS ENTER TO USE DEFAULT PLACE : {W}")
        if cd == '' and p.exists("C:\\Downloads\\chromedriver_win32\\chromedriver.exe"):
            n = int(input(f'{random.choice(colors)}ENTER NUMBER OF REQUIRED VIEWS : {W}'))
            if n == 0:
                print(f'{random.choice(colors)}DONE !!!!!!!!!!!!!!!!!!!!!!!!!!!1{W}')
                exit()
            m = int(input(f'{random.choice(colors)}ENTER MINIMUM WATCH TIME IN SECS\n[RECOMMENDED] 60\n>>>{W}'))
            driver = webdriver.Chrome("C:\\Downloads\\chromedriver_win32\\chromedriver.exe")
            i = 1
            while i <= n:
                os.system('CLS')
                vbanner()
                print(f"{random.choice(colors)}Views : {i}")
                driver.get(vid)
                if m < 25:
                    s(25)
                else:
                    s(m)
                i += 1
                while i >= n:
                    print(f'{random.choice(colors)}DONE')
                    s(3)
                    exit()
        elif '\\' in cd and 'chromedriver.exe' in cd and p.exists(cd):
            n = int(input(f'{random.choice(colors)}ENTER NUMBER OF REQUIRED VIEWS : {W}'))
            if n == 0:
                vbanner()
                print(f'{random.choice(colors)}DONE !!!!!!!!!!!!!!!!!!!!!!!!!!!1{W}')
                s(3)
                os.system('EXIT')
            m = int(input(f'{random.choice(colors)}ENTER MINIMUM WATCH TIME IN SECS\n[RECOMMENDED] 60\n>>>{W}'))
            driver = webdriver.Chrome(cd)
            i = 1
            while i <= n:
                os.system('CLS')
                vbanner()
                print(f"{random.choice(colors)}Views : {i}")
                driver.get(vid)
                if m < 25:
                    s(25)
                else:
                    s(m)
                s(m)
                i += 1
                while i >= n:
                    print(f'{random.choice(colors)}DONE')
                    s(3)
        else:
            os.system('CLS')
            vbanner()
            print(f'{random.choice(colors)}[ERROR]  WRONG LOCATION\n[EXAMPLE]  C:\\Downloads\\chromedriver_win32\\chromedriver.exe')
            print(f'RETRYING...{W}')
            s(2)
            os.system('CLS')
            start()
start()
