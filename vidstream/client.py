import socket
from tkinter import Frame
import numpy as np
import cv2
import time
import pyautogui

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
print(host)
port = 12996
header=500000

client.connect((host,port))


def message(msg):
  message = msg.encode("utf-8")
  msg_len = len(message)
  send_len = str(msg_len).encode("utf-8")
  send_len += b" " *(header - len(send_len))
  client.send(send_len)
  client.send(message)

def message_(msg):
  
  while True:
   
    msg_len = len(msg)
    send_len = str(msg_len).encode("utf-8")
    send_len += b" " *(header - len(send_len))
    client.send(send_len)
    # real_msg = msg.encode("utf-8")
    client.send(msg)
    # print(msg)
    
    # 
    # 
def screen():
  while True:
    img= pyautogui.screenshot()
    frame = np.array(img)
    d1 = frame.flatten()
    print(len(d1))
    message_(bytes(list(d1)))

		
  
  
screen()