import socket
import codecs
import pickle
import os

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
   x = raw_input("\n**to ask for the files list please enter -ls- \n"
                 "**to request a file please enter the filename\n")
   s.sendall(x)
   data = s.recv(1024)
   if x == "ls":
      data2 = pickle.loads(data)
      print(data2)
   else:
       if data == "no file":
          print("no such file")
       else:
         with open("received.txt", 'wb') as f:
            print("File found")
            print("Receiving data...")
            if not data:
               print("No data recieved")
            else:
               print(data)
   ans = raw_input('\nDo you want to continue(y/n) :') 
   if ans == 'y': 
      continue
   else: 
      break
s.close()
