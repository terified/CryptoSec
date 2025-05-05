import subprocess
import sys
import time
import os
import platform
import webbrowser
import random


RESET = "\033["
BLACK_BG = "\033[40m"
GREEN_TEXT = '\033[1;32m'
required_modules = [
    "uncompyle6",
    "pystyle"
    
        
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_with_delay(text, delay=0.0):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Для переноса строки после завершения

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_modules():
    print_with_delay(GREEN_TEXT + """        
    
    
   ░░░░░░░▀▀░░░░▄█▄░░░░░░░░░░░░
   ░░░░░▄███▄░░░████▄░░░░░░░░░░
   ░░░░▄█████▄░███████░░░░░░░░░
   ░░░░░▀█████░████████▄░░░░░░░
   ░█▄░░░███████████████▄░░░░░░
   ░██░▄█████████████████▄░░░░░
   ███▄███████████████████▄░░░░
   ▀██████████▀▀▀███████████░░░
   ░▀██▀██████▄░░░░░▀████████░░
   ░░░░░░███████▄░░░░░▀███████░
   ░░░░░░█████████▄░░░░░░░▀▀███
   ░░░░░░▀██████████░░░░░░░░░░▀
   ░░░░░░░███████████▄░░░░░░░░░
   ░░░░░░░▀█████████████▄░░░░░░
   ░░░░░░░░███████████████▄░░░░
   ░░░░░░░░░██████████████▀░░░░
   ░░░░░░░░░▀██████████▀░░░░░░░
   ░░░░░░░░░░███████▀▀░░░░░░░░░
   ░░░░░░░░░░░██▀▀█▄░░░░░░░░░░░
       creator:@ipl_adapter
     
    
    """ + RESET)
    input(" EEnter")
    for module in required_modules:
        try:
            __import__(module)
            print(GREEN_TEXT + f"[^•^] {module} установлен.")
        except ImportError:
            print(f"Готовлю к установке  {module}...")
            install(module)
            print_with_delay(GREEN_TEXT + f"Установлен модуль {module}" + RESET)


    print_with_delay(GREEN_TEXT + "ГОТОВО." + RESET)
    time.sleep(4)
    os.system('cls' if os.name == 'nt' else 'clear')

check_and_install_modules()
os.system('cls' if os.name == 'nt' else 'clear')