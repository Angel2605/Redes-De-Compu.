import socket
import threads
bind_ip = "0.0.0.0"
bind_port = 9999
server = socket. socket (socket. AF_INET, socket. SOCK_STREAM)
server. bind ((bind_ip, bind_port))
server. listen (5)
print "[*] Listening on% s:% d"% (bind_ip, bind_port)
# this is our customer management thread
 def handle_client (client_socket):
 # print what the client sends
 request = client_socket. recv (1024)
 print "[*] Received:% s"% request
 # Send a package
 client_socket. send ("ACK!")
 client_socket. shut down ()
while it is true:
 client, addr = server. to accept ()
 print "[*] Accepted connection from:% s:% d"% (addr [0], addr [1])
 # turn our client thread to handle incoming data
 client_handler = thread. Thread (target = handle_client, args = (client,))
 client_manager. beginning ()
