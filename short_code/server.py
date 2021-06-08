# import socket
 
# def Main():
#     host = "18.219.84.155"
#     port = 5000
     
#     mySocket = socket.socket()
#     mySocket.bind((host,port))
     
#     mySocket.listen(1)
#     conn, addr = mySocket.accept()
#     print ("Connection from: " + str(addr))
#     while True:
#         data = conn.recv(1024).decode()
#         if not data:
#                 break
#         print ("from connected  user: " + str(data))
         
#         data = str(data).upper()
#         print ("sending: " + str(data))
#         conn.send(data.encode())
             
#     conn.close()
     
# if __name__ == '__main__':
#     Main()
# # 103.6.158.162/32


import socket

def Main():
    mySocket = socket.socket()

    host = socket.gethostname()
    host = "127.0.0.1"
    print(host)
    port = 6543

    mySocket.bind((host,port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
        print("Now listening...\n")
        try:
            data = conn.recv(1024).decode()
            if not data:
                print("No data")
            elif data == 'killsrv':
                conn.close()
                sys.exit()
            else:
                data = str(data).upper()
                print ("sending: " + str(data))
        except Exception as e:
            print(e)
    conn.close()

if __name__ == '__main__':
    Main()
