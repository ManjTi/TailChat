import os
import socket
import datetime
import threading
print ("""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>> TailChat Project (Lite)
>>> You are connecting Tail
>>> Version Release 1.0 Fix
>>>>>>>>>>>>>>>>>>>>>>>>>>>>
""")

# Customiztation for Client Part
HOST = 'localhost' # Enter your hostname or IP address here if you want to use it everytime you run the program
PORT = 104 # Enter your port number here if you want to use it everytime you run the program

if HOST == '':
    HOST = input("Enter your hostname or IP address: ")
if PORT == 0:
    PORT = int(input("Enter your port number: "))

# Try to connect to the server socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
messages = []
# start a thread to listen to messages from server.
def receive_message():
    while True:
        data = s.recv(1024)
        if not data:
            break
        rec_mes = data.decode()
        messages.append("(From Host) " + rec_mes)
        #clear the screen after each message is sent and print messages.
        #clear console linux / windows
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("\n")
        for message in messages:
            print (message)

receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

# start a thread to send messages to server.
def send_message():
    while True:
        message = input()
        if message == "quit":
            s.close()
            break
        s.send(message.encode())
        messages.append(message)
send_thread = threading.Thread(target=send_message)
send_thread.start()
# Wait for the threads to finish.
receive_thread.join()
send_thread.join()
