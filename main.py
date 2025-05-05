import os
import time
import ctypes
from pystyle import Colorate, Colors
from decoder_core import (
    decode_string_input,
    save_encrypted_code,
    mzb
)

if os.name == 'nt':
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 3)

colors_themes = [
    Colors.red_to_yellow,
    Colors.green_to_cyan,
    Colors.blue_to_purple,
    Colors.cyan_to_blue,
    Colors.green_to_yellow,
    Colors.red_to_blue,
    Colors.blue_to_green,
    Colors.purple_to_red,
    Colors.cyan_to_green,
    Colors.yellow_to_red
]

theme_names = [
    "Red → Yellow",
    "Green → Turquoise",
    "Blue → Purple",
    "Turquoise → Blue",
    "Green → Yellow",
    "Red → Blue",
    "Blue → Green",
    "Purple → Red",
    "Cyan → Green",
    "Yellow → Red"
]

banner_txt = '''  
  ▄▄█▀▀▀█▄█                              ██            ▄█▀▀▀█▄█                 
▄██▀     ▀█                              ██           ▄██    ▀█                 
██▀       ▀███▄███▀██▀   ▀██▀████████▄██████  ▄██▀██▄▀███▄     ▄▄█▀██  ▄██▀██  
██          ██▀ ▀▀  ██   ▄█   ██   ▀██  ██   ██▀   ▀██ ▀█████▄▄█▀   ███▀   ██  
██▄         ██       ██ ▄█    ██    ██  ██   ██     ██     ▀████▀▀▀▀▀▀█        
▀██▄     ▄▀ ██        ███     ██   ▄██  ██   ██▄   ▄███     ████▄    ▄█▄    ▄  
  ▀▀█████▀▄████▄      ▄█      ██████▀   ▀████ ▀█████▀█▀█████▀  ▀█████▀█████▀  
                     ▄█        ██                                              
                    ██▀       ▄████▄                                           
                                                 telegram: t.me/ferotier        
                                           by yatomuro | decompile & decode tool
'''

# Меню
menu_txt = '''
                ╔══════════════════════════════╗         ╔════════════════════════════════════╗    
                ║  1 > Decode Zlib & Base64    ║         ║  2 > Decode rendyobfuscator_bot    ║  
                ╚══════════════════════════════╝         ╚════════════════════════════════════╝         
        
                                  ╔═════════════════════════════════════════╗        
                                  ║               [0] > Exit                ║        
                                  ╚═════════════════════════════════════════╝
'''

def print_banner(color_theme):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(color_theme, banner_txt))

def choose_theme():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Select the interface color theme:\n")

    for i, name in enumerate(theme_names):
        print(f"  {i+1} > {name}")

    while True:
        choice = input("\nEnter theme number ")
        if choice.isdigit() and 1 <= int(choice) <= len(colors_themes):
            return colors_themes[int(choice)-1]
        else:
            print("❌ Invalid input. Try again.")

def show_menu(color_theme):
    print(Colorate.Vertical(color_theme, menu_txt))
    choice = input("\nSelect option: ")

    if choice == "0":
        print("Exit.")
        exit()
    elif choice == "1":
        save_encrypted_code()
    elif choice == "2":
        decode_string_input()
    elif choice =="3":
        mzb()
    else:
        print("❌ Incorrect option.")

if __name__ == "__main__":
    selected_theme = choose_theme()
    print_banner(selected_theme)
    show_menu(selected_theme)
