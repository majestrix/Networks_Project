import os
import socket
import pickle
import atexit
from thread import *
import threading

y = []
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
path = '.'
print_lock = threading.Lock()


def error_socket(s):
      s.close()
      
def threaded_sock(conn):
      files = os.listdir(path)
      for x in files:
            y.append(x)
      encodedFile = pickle.dumps(y)
      try:
            while True:
                  data = conn.recv(1024)
                  if not data:
                        break
                  if data == "ls":
                        conn.send(encodedFile)
                        y[:] = []
                  elif data in y:
                        filename = data
                        f = open(filename,'rb')
                        l = f.read(1024)
                        while(l):
                              conn.send(l)
                              print("Sent",repr(l))
                              l = f.read(1024)
                  else:
                        conn.send("make sure you enter the file correctly\n")
            print_lock.release()
            conn.close()
      except Exception:
            import traceback
            print(traceback.format_exc())
            print_lock.release()
            conn.close()


      
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
atexit.register(error_socket,(s))
while True:
      conn,add = s.accept()
      print("Connected to",add[0],":",add[1])
      print_lock.acquire()
      start_new_thread(threaded_sock, (conn,))
s.close()


