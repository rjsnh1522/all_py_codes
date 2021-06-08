import socket
 
def Main():
    host = '18.219.84.155'
    #host = "127.0.0.1"
    port = 5000
     
    mySocket = socket.socket()
    mySocket.connect((host,port))
     
    message = input(" -> ")
    print(f"message {message}")
    while True:
        message = input("Please enter your message   ")
        if message != 'q':
            mySocket.send(message.encode())
        # data = mySocket.recv(1024).decode()
        # print ('Received from server: ' + data)
        # message = input(" -> ")
        # print(f"message {message}")
        message = ""
             
    mySocket.close()
 
if __name__ == '__main__':
    Main()
