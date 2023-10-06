"""
client.py

Created on Fri Oct 6 02:58:36 2023

@author: Mark Graham
"""

### Packages needed for application
import threading
import socket

### Get alias from the user (also known as username)
alias = input('Enter your alias >>> ')

### Establish client socket and connect to server 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))


### Function to receive messages from server using proper exception handling
### technique.
def client_receive():
    while True:
        try:
            ### Gets message from server when broadcasted.
            message = client.recv(1024).decode('utf-8')

            ### Checks for initial broadcast message.
            if message == 'What is your alias?':
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        
        ### If connection fails, alert the user and close the socket.
        except:
            print('Error!')
            client.close()
            break


### Function to send messages to the server for broadcasting.
def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))


### Enables receiving and sending simultaneously.
receive_thread = threading.Thread(target = client_receive)
receive_thread.start()

send_thread = threading.Thread(target= client_send)
send_thread.start()