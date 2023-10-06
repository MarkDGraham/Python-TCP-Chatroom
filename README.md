# Python-TCP-Chatroom
A Python client-to-client (one-to-one) chat room application utilizing TCP / IP. 
<br/>

## Usage Instructions:
1) Enter the folder where the code is stored. <br/>
2) Right click to open menu. <br/>
3) Click 'Open in terminal' option. <br/>
4) Enter the executable script for the code in your respective system. <br/>

## Setting up Multi-device connection:
&emsp;To setup multi-device connection, set the server host to the main machine <br/>
IP address and the port to an unused port. Then, set clients to that IP and the <br/>
ports should match. Once that is completed, run and watch the magic. <br/>

## server.py
&emsp;The host connection program that connects each client to each other.  <br/>
Setup as the main access point for clients to communicate. <br/>
<br/>

## client.py
&emsp;The clients connecting to the host or the server. The server must be <br/>
running for the clients to connect then communication can begin. <br/>