"""
server.py

Created on Fri Oct 6 02:19:53 2023

@author: Mark Graham
"""

### Packages for application
import socket
import threading

### Set port and host for binding
## 127.0.0.1 is the local host and will network on the internal IP.
## Port must be check to make sure it is not currently being used.
host = '127.0.0.1'
port = 59000

### Created a Server socket using IPv4 and TCP/IP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

### BIND STEP:
## Establish the server socket to the host and port.
server.bind((host, port))

### LISTEN STEP:
## Activate the server socket to listen for clients trying to connect.
server.listen()

## Store clients and aliases of the clients into an array for tracking.
clients = []
aliases = []

### Function to send a message to all active clients in the session.
def broadcast(message):
    for client in clients:
        client.send(message)

### Functio to determine if client is still in the chat or has left
### if they left then remove them from client and alias lists.
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)     ### Receive message
            broadcast(message)              ### Send message to everyone
        except:
            index = clients.index(client)   ### Identify the client that left
            clients.remove(client)          ### Remove them from the list
            client.close()                  ### Shutdown the connection 
            alias = aliases[index]          ### Get the alias of the client.
            broadcast(f'{alias} has left the chatroom!'.encode('utf-8'))
            aliases.remove(alias)           ### Remove thm from the alias list.
            break                           ### Exit the infinite loop. 

### Function to receieve the client connections
def receive():
    while True:
        ### Run server into active mode
        print('Server is running and listening ...')

        ### Accept connection from client
        client, address = server.accept()
        print(f'Connection is established with {str(address)}')

        ### Request alias from client and store it.
        client.send('What is your alias?'.encode('utf-8'))
        alias = client.recv(1024)
        aliases.append(alias)

        ### Add client to clients at same time as alias (== index)
        clients.append(client)

        ### Confirm the alias to the user
        print(f'The alias of this client is {alias}'.encode('utf-8'))

        ### Send message to chatroom of alias has entered
        broadcast(f'{alias} has entered the chatroom!'.encode('utf-8'))

        ### Confirm connection
        client.send(f'{alias} you are now connected!'.encode('utf-8'))

        ### Establish multi-chatting feature (multithreading) 
        thread = threading.Thread(target = handle_client, args=(client,))
        thread.start()


### Begin the Server program in certain order!
if __name__ == "__main__":
    receive()