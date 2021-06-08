import pyautogui
from time import sleep
from colorama import init, Fore
import os
from random import choice
clear_cmd = None
if os.name == 'nt':
    try:
        init()
        clear_cmd = 'cls'
    except Exception as er:
        print('somthing went wrong')
else:
    try:
        clear_cmd = 'clear'
    except Exception as er:
        print('some thing went wrong')

name = ["""
███████ ██████   █████  ███    ███ ███████ ██████  
██      ██   ██ ██   ██ ████  ████ ██      ██   ██ 
███████ ██████  ███████ ██ ████ ██ █████   ██████  
     ██ ██      ██   ██ ██  ██  ██ ██      ██   ██ 
███████ ██      ██   ██ ██      ██ ███████ ██   ██ 
                                                   
""",
        """
███████╗██████╗  █████╗ ███╗   ███╗███████╗██████╗ 
██╔════╝██╔══██╗██╔══██╗████╗ ████║██╔════╝██╔══██╗
███████╗██████╔╝███████║██╔████╔██║█████╗  ██████╔╝
╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██╔══╝  ██╔══██╗
███████║██║     ██║  ██║██║ ╚═╝ ██║███████╗██║  ██║
╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                   
"""
        ]


def banner():
    os.system(clear_cmd)
    sleep(2)
    colors = ['Red', 'Blue', 'Green', 'Yellow', 'CYAN']
    color_choise = choice(colors)
    banner_choise = choice(name)
    if color_choise == 'Red':
        print(Fore.RED+banner_choise)
    if color_choise == 'Blue':
        print(Fore.BLUE+banner_choise)
    if color_choise == 'Green':
        print(Fore.GREEN+banner_choise)
    if color_choise == 'Yellow':
        print(Fore.YELLOW+banner_choise)
    if color_choise == 'CYAN':
        print(Fore.CYAN+banner_choise)
    attack()


def attack():
    sleep(0.2)
    time = float(
        input(Fore.RED+'['+Fore.GREEN+'+'+Fore.RED+']'+Fore.YELLOW+'sleep time: '))
    sleep(0.2)
    size = int(input(Fore.RED+'['+Fore.GREEN+'+' +
               Fore.RED+']'+Fore.YELLOW+'size of attack: '))
    sleep(0.2)
    word = input(Fore.RED+'['+Fore.GREEN+'+'+Fore.RED +
                 ']'+Fore.YELLOW+'special word : ')
    sleep(3)
    for things in range(size):
        sleep(time)
        pyautogui.typewrite(word)
        pyautogui.hotkey('enter')


# attack()
banner()
# برای شروع باید اول با دستور
# python3 auto.py
# رانش کنی
# بعد از اون مقدار اولی که میدی میه اون تایمی که بین ارسال  کلمه نیازد دارری و دومین چیز مقدار کلمه یعنی تعدادی که میخواایی بفرستی و موزد اخر هم  بزار ببینم :)
# خود  اون کلمه خاصه فقط فارسی نمیشه الان من اینترنت کانکشنم خوب نی نمیتونم وص بشم ایجا تست میکنم بعد از زدن مورد اخر باید کرسور تای\ رو تو عرض چند سانیه بزاری جایی که میخواد شروع کنه
# منظور از کرسو همین چیزی ه که داره اینجا چشمک میزن
