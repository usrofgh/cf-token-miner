import os
import subprocess

import pyperclip
import pytesseract
import pyautogui

def copy_to_clipboard(text: str):
    if os.name == "posix":
        process = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE)
        process.communicate(input=text.encode('utf-8'))
    else:
        pyperclip.copy(text)

def paste_from_clipboard() -> str:
    if os.name == "posix":
        process = subprocess.Popen(['xclip', '-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
        output, _ = process.communicate()
        return output.decode('utf-8')
    else:
        return pyperclip.paste()

def find_xy_by_word(word: str) -> tuple:
    screen = pyautogui.screenshot()
    data = pytesseract.image_to_data(screen, config='--psm 6', output_type=pytesseract.Output.DICT)
    for i, w in enumerate(data["text"]):
        if w.lower() == word.lower():
            x = data["left"][i]
            y = data["top"][i]
            return x, y
