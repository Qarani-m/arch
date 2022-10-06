from ctypes.wintypes import MSG
from pickletools import float8, uint8
import socket
import threading
import numpy as np
import sys
import os
import cv2
import time
import pyautogui
from io import BytesIO

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 12996
header = 500000
server.bind((host,port))





def imgConversion(msg):
  a = np.array(np.frombuffer(msg, dtype=np.uint8))
  screen_size =(1920,1080)
  fourcc = cv2.VideoWriter_fourcc(*"XVID")
  out = cv2.VideoWriter("output.avi",fourcc,20.0,(screen_size))
  fps =60
  prev= 0
  while True:
    time_elapsed = time.time()-prev
    img = pyautogui.screenshot()
    if time_elapsed> 1.0/fps:
      prev = time.time()
      out.write(a)
      cv2.waitKey(5)






def handleClient(conn, addr):
	print(f"[NEW CONNECTION]: {addr}")
	connected = True;screen_size =(1920,1080);fourcc = cv2.VideoWriter_fourcc(*"XVID");out = cv2.VideoWriter("output.avi",fourcc,20.0,(screen_size));fps =60;prev= 0
	while connected:
		msg_length = 43434343#conn.recv(header).decode("utf-8")
		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode("utf-8")
			f = np.fromstring(msg,dtype=np.float32, sep=" ")
			frame = np.array(f, ndmin=3)
			print(frame)
			
		
   
			if msg == "Disconnect":connected = False
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
			# imgConversion(msg)
	conn.close()

def start():
	server.listen(10)
	while True:
		conn,addr = server.accept()
		t = threading.Thread(target=handleClient,args=(conn,addr))
		t.start()
		print(f"[CONNECTIONS] {threading.active_count()-1}")

print("starting...")
start()
