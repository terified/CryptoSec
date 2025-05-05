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
    file_path = input("Укажи путь до файла со строкой: ")

    if not os.path.isfile(file_path):
        print("[-] Файл не найден.")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            encrypted_string = file.read()

        if not encrypted_string:
            print("[-] Строка в файле пуста.")
            return

        encrypted_string = encrypted_string.replace("\n", "").replace(" ", "")
        missing_padding = len(encrypted_string) % 4
        if missing_padding:
            encrypted_string += '=' * (4 - missing_padding)

        output_name = input("Введи имя для pyc файла (без .pyc): ") or "output"
        output_folder = input("Введи путь для сохранения (или Enter для папки pyc_files): ") or "pyc_files"

        os.makedirs(output_folder, exist_ok=True)
        output_path = os.path.join(output_folder, f"{output_name}.pyc")

        decode_and_save(encrypted_string, output_path)

    except Exception as e:
        print(f"[-] Ошибка при обработке файла: {e}")

def func(code):
    return zlib.decompress(base64.b64decode(code[::-1]))

def mzb():
    print('🔍 Decompile Marshal, Zlib, Base64 from string in .txt file')
    file_path = input('📄 Path to .txt file with encoded string: ')
    output_name = input('💾 Output filename (without .py): ')
    
    # Читаем строку из txt
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()
    except FileNotFoundError:
        print('❌ File not found!')
        return

    # Формируем код, который будет декомпилироваться
    temp_code = f'''
from sys import stdout
from uncompyle6.main import decompile
import base64, zlib, marshal

x = marshal.loads(zlib.decompress(base64.b64decode({repr(content)})))
decompile(2.7, x, stdout)
'''

    # Создаём временный файл
    os.makedirs('pyc_files', exist_ok=True)
    temp_file = 'mi_temp.py'
    with open(temp_file, 'w') as f:
        f.write(temp_code)

    # Запускаем декомпиляцию
    output_path = f'pyc_files/{output_name}.py'
    os.system(f'python2 {temp_file} > "{output_path}"')

    # Удаляем временный файл
    os.remove(temp_file)

    print(f'✅ Decompiled code saved to: {output_path}')

    # Повтор?
    again = input('🔁 Want to decrypt again? (Y/N): ').lower()
    if again == 'y':
        mzb()
    else:
        print('👋 Done.')

def save_encrypted_code():
    # Заданный путь к файлу с кодом
    file_path = r"C:\Users\h1xx\Desktop\CryptoSec\base64_zlib_decode.txt"

    if not os.path.isfile(file_path):
        print("[-] Файл не найден.")
        return

    # Чтение содержимого файла в переменную code
    with open(file_path, "rb") as f:
        code = f.read()

    # Регулярка для поиска твоего exec((_)(b'...'))
    regex = re.compile(rb"^exec\(\(_\)\(b'(.+)'\)\)$")

    # Цикл декодирования
    while True:
        result = regex.search(code)
        if not result:
            break
        code = func(result.group(1))

    # Запрос имени для pyc файла
    output_name = input("Введи имя для pyc файла (без .py): ") or "output"
    output_folder = input("Введи путь для сохранения (или Enter для папки pyc_files): ") or "pyc_files"

    # Создание папки если её нет
    os.makedirs(output_folder, exist_ok=True)

    # Путь для сохранения файла
    output_path = os.path.join(output_folder, output_name + ".pyc")

    # Сохраняем в файл
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
            f.write(code_obj)  # Save the final decoded data
        print(f"Decoded data saved as {filename}")
    except Exception as e:
        print(f"[!] Error in decode_and_save: {e}")