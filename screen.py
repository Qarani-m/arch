import numpy as np
import cv2
import time
import pyautogui
import base64


screen_size = (1920,1080)
forcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi",forcc,20.0,(screen_size))

fps = 60
prev = 0


def bytesArr():
	with open("B.png","rb") as img:
		str_= base64.b64encode(img.read())
		str2= base64.b64decode(str_)
		with open("c.png" ,"wb") as file:
			file.write(str2)
		print(str2)

bytesArr()



# while True:
# 	time_elapsed = time.time() - prev
# 	img = pyautogui.screenshot("B.png")
	
# 	if time_elapsed> 1.0/fps:
# 		prev = time.time()
# 		frame = np.array(img)
# 		frame =cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
# 		out.write(frame)
# 	cv2.waitKey(100)

cv2.destroyAllWindows()
out.release()


