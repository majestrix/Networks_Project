import socket
import codecs
import pickle

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
x = input("**to ask for the files list please enter -ls- \n **to request a file please enter the filename")
s.sendall(x.encode())
data = s.recv(1024)
if x == "ls":
   data2 = pickle.load()
   print(data2)

else:
    if data == "no file":
       print("no such file")
    else:
         with open('received', 'wb') as f:
              print('file opened')
              print('receiving data...')
                    #print('data=%s', (data))
              if not data:
                     print ("empty file")
                    # write data to a file
              f.write(data)


#print('Received', repr(x))
