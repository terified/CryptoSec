import base64, zlib, lzma, gzip, marshal, re, os
import subprocess
import py_compile
import uncompyle6
import dis
import importlib.util

def clear():
    os.system("cls" if os.name == "nt" else "clear")

import os

def decode_string_input():
    file_path = input("Specify the path to the file containing the string: ")

    if not os.path.isfile(file_path):
        print("[-] File not found.")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            encrypted_string = file.read()

        if not encrypted_string:
            print("[-] The string in the file is empty.")
            return

        encrypted_string = encrypted_string.replace("\n", "").replace(" ", "")
        missing_padding = len(encrypted_string) % 4
        if missing_padding:
            encrypted_string += '=' * (4 - missing_padding)

        output_name = input("Enter a name for the pyc file (without .pyc): ") or "output"
        output_folder = input("Enter the save path (or press Enter to use the pyc_files folder): ") or "pyc_files"

        os.makedirs(output_folder, exist_ok=True)
        output_path = os.path.join(output_folder, f"{output_name}.pyc")

        decode_and_save(encrypted_string, output_path)

    except Exception as e:
        print(f"[-] Error while processing the file: {e}")

def func(code):
    return zlib.decompress(base64.b64decode(code[::-1]))

def mzb():
    print('🔍 Decompile Marshal, Zlib, Base64 from string in .txt file')
    file_path = input('📄 Path to .txt file with encoded string: ')
    output_name = input('💾 Output filename (without .py): ')
    
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
    except FileNotFoundError:
        print('❌ File not found!')
        return

    temp_code = f'''
from sys import stdout
from uncompyle6.main import decompile
import base64, zlib, marshal

x = marshal.loads(zlib.decompress(base64.b64decode({repr(content)})))
decompile(2.7, x, stdout)
'''

    os.makedirs('pyc_files', exist_ok=True)
    temp_file = 'mi_temp.py'
    with open(temp_file, 'w') as f:
        f.write(temp_code)

    output_path = f'pyc_files/{output_name}.py'
    os.system(f'python2 {temp_file} > "{output_path}"')

    os.remove(temp_file)

    print(f'✅ Decompiled code saved to: {output_path}')

    # Повтор?
    again = input('🔁 Want to decrypt again? (Y/N): ').lower()
    if again == 'y':
        mzb()
    else:
        print('👋 Done.')

def save_encrypted_code():
    file_path = r"C:\Users\h1xx\Desktop\CryptoSec\base64_zlib_decode.txt"

    if not os.path.isfile(file_path):
        print("[-] File not found.")
        return

    with open(file_path, "rb") as f:
        code = f.read()

    regex = re.compile(rb"^exec\(\(_\)\(b'(.+)'\)\)$")

    while True:
        result = regex.search(code)
        if not result:
            break
        code = func(result.group(1))

    output_name = input("Enter a name for the pyc file (without .py): ") or "output"
    output_folder = input("Enter the save path (or press Enter to use the pyc_files folder): ") or "pyc_files"

    os.makedirs(output_folder, exist_ok=True)

    output_path = os.path.join(output_folder, output_name + ".pyc")

    with open(output_path, "wb") as f:
        f.write(code)

    print(f"\n[+] Файл успешно сохранён: {output_path}")

def decode_and_save(data, filename):
    """ Decodes and saves the decoded data into a file. """
    try:
        decoded = base64.b64decode(data[::-1])  # Reverse string and decode
        decoded = zlib.decompress(decoded)      # Zlib decompression
        decoded = lzma.decompress(decoded)      # LZMA decompression
        decoded = gzip.decompress(decoded)      # Gzip decompression
        code_obj = marshal.loads(decoded)       # Unmarshal

        with open(filename, 'wb') as f:
            f.write(code_obj) 
        print(f"Decoded data saved as {filename}")
    except Exception as e:
        print(f"[!] Error in decode_and_save: {e}")
