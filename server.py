import os
import socket
import pickle
y = []
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
path = '.'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind((HOST, PORT))
      s.listen(5)
      while True:
            conn, addr = s.accept()
            print('Connected by', addr)
            data = conn.recv(1024)
            files = os.listdir(path)
            for x in files:
                  y.append(x)
            data2 = pickle.dumps(y)
            if not data:
                 break
            if  data == "ls":
                     conn.send(data2)
                     y[:] = []

            elif data in y:
                 filename = data
                 f = open(filename, 'rb')
                 l = f.read(1024)
                 while (l):
                      conn.send(l)
                      print('sent' ,repr(l))
                      l = f.read(1024)
                 f.close()
            else:
                conn.send("no file")
                conn.close()
      #conn.close()


