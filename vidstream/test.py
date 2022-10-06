import socket
import threading
server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host = socket.gethostbyname(socket.gethostname())
host="192.168.100.8"
port = 12998
header = 64
server.bind((host,port))

def handleClient(conn, addr):
	print(f"[NEW CONNECTION]: {addr}")
	connected = True
	while connected:
		msg_length = conn.recv(header).decode("utf-8")
		if msg_length:
			msg_length = int(msg_length)
			msg = conn.recv(msg_length).decode("utf-8")
			if msg == "Disconnect":
				connected = False
			print(msg)
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
while input("") == "stop":
	pass






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
	cv2.imwrite("file.png",img)
	if time_elapsed> 1.0/fps:
		prev = time.time()
		frame = np.array(img)

		frame =cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
		out.write(frame)
	cv2.waitKey(10)

cv2.destroyAllWindows()
out.release()






import socket
import numpy as np
import cv2
import time
import pyautogui

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
print(host)
port = 12998
header=64

client.connect((host,port))


def message(msg):
	message = msg.encode("utf-8")
	msg_len = len(message)
	send_len = str(msg_len).encode("utf-8")
	send_len += b" " *(header - len(send_len))
	client.send(send_len)
	client.send(message)

message("hello world")

















while True:
		print("jjjj")
		time_elapsed = time.time()-prev
		img = pyautogui.screenshot()

		frame = np.array(img)

		is_success, im_buf_arr = cv2.imencode(".jpg", frame)
		byte_im = im_buf_arr.tobytes()
		message_(byte_im)
		print("hhh")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  def screen():
	

	while True:
		print("jjjj")
		img = pyautogui.screenshot()
		frame = np.array(img)
		is_success, im_buf_arr = cv2.imencode(".jpg", frame)
		byte_im = im_buf_arr.tobytes()
		message_(byte_im)






 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3]
 [ 4  