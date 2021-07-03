import sys
import socket
import threads
def server_loop local_host, local_port, remote_host, remote_port, receive_first):

 server = socket. socket (socket. AF_INET, socket. SOCK_STREAM)
 proof :
 server. bind ((local_host, local_port))
 except:
 print "[!!] Error listening on% s:% d"% (local_host, local_port)
 print "[!!] Check for other listening jacks or correct permissions".
 sys. exit (0)

 print "[*] Listening to% s:% d"% (local_host, local_port)


 server. listen (5)

 while it is true:
 client_socket, addr = server. to accept ()

 # print local connection information
 print "[==>] I received incoming connection from% s:% d"% (addr [0], addr [1])

 # start a thread to talk to the remote host
 proxy_thread = threading. Thread (target = proxy_handler, arg = (client_socket, remote_host, remote_port, receive_first))

 proxy_thread. beginning ()

def main ():

 # no fancy command line parsing here
 if len (sys. argv [1:])! = 5:
 print "Usage: ./proxy.py [localhost] [localport] [remotehost] [remoteport] [receive_first]"
 print "Example: ./proxy.py 127.0.0.1 9000 10.12.132.1 9000 True"
 sys. exit (0)

 # configure local listener parameters
 local_host = sys. argv [1]
 local_port = int (sys. argv [2])

 # set remote target
 remote_host = sys. argv [3]
 remote_port = int (sys. argv [4])

 # this tells our proxy to connect and receive data
 # before sending to remote host
 receive_first = sys. argv [5]

 if "True" in Receive_first:
 receive_first = True
 another thing :
 receive_first = False

 # now turn our listening plug
 server_loop (local_host, local_port, remote_host, remote_port, receive_first)


def proxy_handler (client_socket, remote_host, remote_port, receive_first):

 # connect to remote host
 take_remoto = take. socket (socket. AF_INET, socket. SOCK_STREAM)
 
take_remote. connect ((remote_host, remote_port))
 
# receive data from the remote end if necessary
if it receives_first:

remote_buffer = receive_from (remote_socket)
hexdump (remote_buffer)
 
# send it to our response handler remote_buffer = response_handler (remote_buffer)

 # if we have data to send to our local client, send it
 if len (remote_buffer):
 print "[<==] Sending% d bytes to localhost". % len (remote_buffer)
 client_socket. send (remote_buffer)
 
# now we are going to go and read from local,
 # send remote, send local
 # rinse, wash, repeat
 while it is true:
 
# read from local host
 local_buffer = receive_from (client_socket)
 

if len (local_buffer):
 print "[==>] Received% d bytes from localhost". % len (local_buffer)
 hexdump (local_buffer)
 
# send it to our request manager
 local_buffer = request_handler (local_buffer)

# send data to remote host
 take_remote. send (local_buffer)
 print "[==>] Sent to remote".

 # receive the reply
 remote_buffer = receive_from (remote_socket)
 
if len (remote_buffer):
 
print "[<==] Received% d bytes from remote control". % len (remote_buffer)
 hexdump (remote_buffer)
 
# send to our response handler
 remote_buffer = response_handler (remote_buffer)
 
# send the response to the local socket
 client_socket. send (remote_buffer)
 
print "[<==] Sent to localhost".
 
# if there is no more data on either side, close the connections
if no len (local_buffer) or no len (remote_buffer):
 client_socket. shut down ()
 take_remote. shut down ()
print "[*] There is no more data. Closing connections".
 
break

# this is a nice hex dump function directly taken from
# comments here:
# http://code.activestate.com/recipes/142812-hex-dumper/
def hexdump (src, length = 16):
 result = []
 digits = 4 if isinstance (src, unicode) else 2

 for i in xrange (0, len (src), length):
 s = src [i: i + length]
 hexa = b ''. join (["% 0 * X"% (digits, ord (x)) for x in s])
 text = b ''. join ([x if 0x20 <= ord (x) <0x7F if not b '.' for x in s])
 Outcome . add (b "% 04X% - * s% s"% (i, length * (digits + 1), hexadecimal, text))
 
print b '\ n'. join (result)

def receive_from (connection):

buffer = ""
 # We set a waiting time of 2 seconds; depends on your
 #target, may need to be adjusted
 Connection . settimeout (2)
 
proof :
 # keep reading in the buffer until
 # no more data
 # or we disconnect
while it is true:
 data = connection. recv (4096)

 
if not data:
 break

 buffer + = data
except:
 Approve

 return buffer

# modify any request destined for the remote host
def request_handler (buffer):
 # make package modifications
 return buffer

# modify responses destined for the local host
def response_handler (buffer):
 # make package modifications
 return buffer

principal ()
