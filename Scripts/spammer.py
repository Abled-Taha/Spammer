import os
import keyboard
import pyautogui
import time

def startSpamCustom(SecondSection, spamWord):
    time.sleep(10)
    if SecondSection == 1:
        while True:
            if keyboard.is_pressed("/"):
                break
            pyautogui.typewrite(spamWord)
            if keyboard.is_pressed("/"):
                break
            pyautogui.press("enter")
            if keyboard.is_pressed("/"):
                break
        
    elif SecondSection == 2:
        while True:
            if keyboard.is_pressed("/"):
                break
            pyautogui.typewrite(spamWord)
            time.sleep(0.5)
            if keyboard.is_pressed("/"):
                break
            pyautogui.press("enter")
            time.sleep(0.5)
            if keyboard.is_pressed("/"):
                break


def startSpamDefault(SecondSection):
    time.sleep(10)
    currentDir = os.getcwd()
    if not currentDir.__contains__("Files"):
        os.chdir("Files")
    File = open("messages.txt")
    if SecondSection == 1:
        for word in File:
            if keyboard.is_pressed("/"):
                break
            pyautogui.typewrite(word)
            if keyboard.is_pressed("/"):
                break
            pyautogui.press("enter")
            if keyboard.is_pressed("/"):
                break

    elif SecondSection == 2:
        for word in File:
            if keyboard.is_pressed("/"):
                break
            pyautogui.typewrite(word)
            time.sleep(0.5)
            if keyboard.is_pressed("/"):
                break
            pyautogui.press("enter")
            time.sleep(0.5)
            if keyboard.is_pressed("/"):
                break