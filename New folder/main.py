import numpy as np
import cv2
import time
import pyautogui

screen_size =(1920,1080)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.mp4",fourcc,20.0,(screen_size))

fps =60
prev= 0

while True:
	time_elapsed = time.time()-prev
	img = pyautogui.screenshot()
	print(type(img))
cv2.destroyAllWindows()
out.release()
