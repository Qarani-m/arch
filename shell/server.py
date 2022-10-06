import sys
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 27898
addr = (host,port)
header = 64
format = "utf-8"


text = input("----")


server.bind(addr)

def handleClient(conn,addr):
  print(f"[connection from:] {addr}")
  connected = True
  text = ""
  while connected:
    print
    msg_length = conn.recv(header).decode(format)
    if msg_length:
      msg_length = int(msg_length)
      msg  = conn.recv(msg_length).decode(format)  
      print(msg)
      

    if msg == "disconnect":
      connected = False
      conn.close()
    if input("") == "":
      continue
   
  
def start():
  server.listen(10)
  while True:
  
    conn, addr= server.accept()
    thread = threading.Thread(target=handleClient, args=(conn,addr))
    thread.start()
    print(f"{threading.active_count()-1} : Connections")

print("Server starting....")
start()   

def send():
  pass