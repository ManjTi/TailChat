import socket
import datetime
import threading
print ("""
>>>>>>>>>>>>>>>>>>>>>>>>>
TailChat Project (Lite)
You are Hosting Tail
Version Release 1.0 Fix
>>>>>>>>>>>>>>>>>>>>>>>>>
""")

# Customiztation for Host Part
PORT = 104 # Change default port number if you need to.
import os
# Create a server (Host tail) socket and another user uses clien tail to connect to this server. Both server and client can send and receive data.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', PORT))
s.listen(1)
print ("Tail is running & listening on port", PORT)
messages = []
already_connected = False
# Start a socket in a thread to receive data from client.
while True:
    conn, addr = s.accept()
    if already_connected:
        conn.send("Someone is already connected to this server. Please try again later.".encode())
        conn.close()
        continue
    else:
        already_connected = True
        #clear linux / windows terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        #Print client's IP address and port number.
        client_info = ("Tails are now connected to this server, client tail:  ", addr)
        print (client_info)
        messages.append(client_info)
        # Send a welcome message to the client.
        conn.send("(From Host Tail) Your tails are now connected.\n".encode())
        # Both server and client can send and receive data to each other.
        # start a different thread to recieve messages from client and print them.
        def receive_message():
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                recieved_msg = data.decode()
                messages.append("(From Client Tail) " + recieved_msg)
        #clear the screen after each message is sent and print messages.
        #clear console linux / windows
                os.system('cls' if os.name == 'nt' else 'clear')
                print ("\n")
                for message in messages:
                    print (message)
        receive_thread = threading.Thread(target=receive_message)
        receive_thread.start()
        # Start a thread to send messages to client.
        def send_message():
            while True:
                message = input()
                if message == "quit":
                    conn.close()
                    #stop server socket
                    s.close()
                    #stop thread
                    receive_thread.join()
                    break
                    
                messages.append(message)
                conn.send(message.encode())
                #clear the screen after each message is sent and print messages.
                #clear console linux / windows
                os.system('cls' if os.name == 'nt' else 'clear')
                print ("\n")
                for message in messages:
                    print (message)


        send_thread = threading.Thread(target=send_message)
        send_thread.start()

        # Wait for the threads to finish.
        receive_thread.join()
        send_thread.join()