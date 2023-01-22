import socket
import threading as td
import sys
import struct
import time
# from pysql import mysqls as ms

server_ip = 'localhost'
port = 5050
PORT2 = 5000
BUFFSIZE = 10100

def listenmsg():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.bind(('',PORT2))
    while  True:
        message, address = s.recvfrom(BUFFSIZE)
        print("\nYou got message:", message.decode('utf-8'))

def server_handler(client):
    while True:
        try:
            data = client.recv(BUFFSIZE).decode('utf8')
            print("server say:",data)

        except:
            print('ERROR! connect failed.')
            break
        #exit funtion
        if data == 'q':
            print("----------- exit -----------")
            # print('OUT : ',client)
            break
        elif not data:
            print("----------- exit -----------")
            # print(str(data))
            print("error")
            break
        # print(data.decode('utf-8'))
    # user exit
    client.close()
    sys.exit()
def client_connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        client.connect((server_ip,port))
    except:
        print('ERROR! can not connect to server.')
        sys.exit()

    # runthread
    task = td.Thread(target=server_handler,args=(client,))
    task.start()

    # รอข้อรับความแบบกระจายทุกคนที่เชื่อมต่อจะได้รับเมื่อเชื่อมต่ออยู่
    task2 = td.Thread(target=listenmsg)
    task2.start()
    # input from user.
    print('='*15 + '  Welcome to Foodservice  ' + '='*15+'\n')
    print("\t1. Login\n\t2. Register\n\t3. Bill history\n\t4. Order Food\n")
    while True:
        msg = input('Message: ')
        if msg == '':
            msg = " "
        client.send(msg.encode('utf-8'))
        time.sleep(0.5)
        
        if msg == 'q':
            break
    client.close()
    sys.exit()
#############################################################
############# รัน client_connect_to_server ที่นี่ ###############
############################################################
if __name__ == '__main__':
    client_connect_to_server()