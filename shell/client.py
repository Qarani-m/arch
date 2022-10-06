import socket
import threading


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 27898
addr = (host,port)
header = 64
format = "utf-8"

client.connect((host, port))

def message(msg):
  message  = msg.encode(format)
  msg_len = len(message)
  send_len = str(msg_len).encode(format)
  send_len += b" "*(header-len(send_len))
  client.send(send_len)
  client.send(message)
  msg= client.recv(1024).decode(format)
  print(msg)




while True:
  message(input("llll"))