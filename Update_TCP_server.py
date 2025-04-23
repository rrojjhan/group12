import socket
import select
import json

HOST = '100.83.170.97' #VPN IP given
PORT = 1234

subscribers = []  #track subscribers
publishers = []   #track publishers

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create a socket for connection
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #allow to reuse the port (prevent the 'address in use' errors)
server_socket.bind((HOST, PORT)) #binds to the broker IP
server_socket.listen() #enables the broker to accept TCP connections

sockets_list = [server_socket]

print(f"Pub/Sub Broker running on {HOST} : {PORT}") #display the server's ip and port

while True: #the code is continuosly looping to check for connections unless the program is stopped
    read_sockets, _, _ = select.select(sockets_list, [], []) #single threading
    for sock in read_sockets:
        if sock == server_socket: #compare if the sock equals the same


            #conn is a new socket object usable to send and receive data on the connection, and address is the address bound to the socket on the other end of the connection.
            conn, addr = server_socket.accept() #accept the socket connection
            print(f"New connection from {addr}") #displays the new connection and connection's IP address
            sockets_list.append(conn)#adds new connection to the ongoing socket_list so that the program keeps track of all active connections
        else:
            try:
                data = sock.recv(1024)
                if not data:

                    print(f"client disconnected from {addr}")
                    sockets_list.remove(sock) #removes the client from the list when disconnected
                    continue
                else:

                    #checking if incoming client is a subscriber
                    message = data.decode().strip().lower()
                    if message == "subscriber": #based on the devicesub.py
                        if sock not in subscribers:
                            subscribers.append(sock)#adds new connection to the ongoing subscriber list
                            print(f"Subscriber registered: {addr}")
                    else:
                        try:

                            #this section focuses on recieving the payload from the publisher
                            json_data = json.loads(data.decode())
                            if sock not in publishers:
                                publishers.append(sock)
                                print(f"Publisher detected: {addr}")
                            print(f"Forwarding: {data.decode().strip()}") #continuosly fowarding publisher payload to subscribers
                            for sub in subscribers:
                                try:
                                    sub.sendall(data) #send the data to subscribers
                                except:
                                    subscribers.remove(sub)
                        except json.JSONDecodeError:
                            pass
            except Exception as e:
                print(f"Error: {e}")
                sockets_list.remove(sock)
                sock.close()