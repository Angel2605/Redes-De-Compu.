import sys
import socket
import getopt
import threads
 import thread

#define some global variables

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = 0

use def ():
print "BHP Net Tool"
Print
print "Usage: bhpnet.py -t target_host -p port"
print "-l --listen - listen on [host]: [port] for incoming connections"
print "-e --execute = file_to_run - execute the given file upon receiving a connection"
print "-c --command - initialize a shell command"
print "-u --upload = destination - upon receiving the connection upload a file and write to [destination]"
Print
Print
print "Examples:"
print "Examples:"
 print "bhpnet.py -t 192.168.0.1 -p 5555 -l -c"
 print "bhpnet.py -t 192.168.0.1 -p 5555 -l -u = c: \\ target.exe"
 print "bhpnet.py -t 192.168.0.1 -p 5555 -l -e = \" cat / etc / passwd \ ""
 print "echo 'ABCDEFGHI' | ./bhpnet.py -t 192.168.11.12 -p 135"
 sys. exit (0)

def main ():
 global listening
 global port
 global execution
global command
 global upload_destination
 global goal

 if not len ​​(sys. argv [1:]):
 use ()

 # read command line options
proof :
 opts, args = getopt. getopt (sys. argv [1:], "hle: t: p: cu:", ["help", "listen", "execute", "target", "port", "command", "load"] )
except getopt. GetoptError as err:
 print str (err)
 use ()

 for or, a in opta:
 if or in ("-h", "--help"):
 use ()
 elif or in ("-l", "--hear"):
 listen = True
 elif or en ("-e", "--execute"):
 run = a
 elif or in ("-c", "--commandshell"):
command = True
elif or in ("-u", "--upload"):
 upload_destination = a
elif or en ("-t", "--target"):
 target = a
 elif or en ("-p", "--port"):
port = int (a)
 another thing :
 assert False, "Option not controlled"

# Are we going to listen or just send data from stdin?
if not listening and len (destination) and port> 0:

 # read into buffer from command line
 # this will crash so send CTRL-D if you don't send input
 # to stdin
 buffer = sys. stdin. read ()

# send data
client_sender (buffer)

# we will listen and potentially
# load things, run commands, and drop a shell
# depending on our command line options above
if you listen :
x server_loop ()

def client_sender (buffer):

 client = socket. socket (socket. AF_INET, socket. SOCK_STREAM)

 proof :
 # connect to our destination host
 client . connect ((destination, port))

if len (buffer):
client . send (buffer)
 
while it is true:

 # now wait for postback
 recv_len = 1
 answer = ""

while recv_len:

 data = customer. recv (4096)
 recv_len = len (data)
 answer + = data

 if recv_len <4096:
 break

 print response,

 # wait for more information
buffer = raw_input ("")
 buffer + = "\ n"

 #send it
 client . send (buffer)


 except:

 print "[*] Exception! Exiting".

 # break down the connection
 client . shut down ()

def server_loop ():
 global goal

 # if no target is defined, we listen on all interfaces
 if not len ​​(target):
 target = "0.0.0.0"

 server = socket. socket (socket. AF_INET, socket. SOCK_STREAM)
 server. bind ((destination, port))
 
server. listen (5)

while it is true:
 client_socket, addr = server. to accept ()

 # spin a thread to handle our new client
 client_thread = thread. Thread (target = client_handler, args = (client_socket,))
 client_thread. beginning ()

def run_command (command):

 # trim the new line
 command = command. rstrip ()

 # run the command and retrieve the output
 proof :
output = thread. check_output (command, stderr = thread. STDOUT, shell = True)
 except:
 output = "The command could not be executed. \ r \ n"

 # send the output to the client
 return output

def client_handler (client_take):
 global load
 global execution
 global command

 # check the load
 if len (upload_destination):

 # read all bytes and write to our destination
 file_buffer = ""

 # keep reading data until none is available
 while it is true:
 data = client_connector. recv (1024)

 if not data:
 break
 another thing :
 file_buffer + = data

 # now we take these bytes and try to write them
proof :
 file_descriptor = open (upload_destination, "wb")
 file_descriptor. write (file_buffer)
 file_descriptor. shut down ()

# recognize that we wrote the file
 client_socket. send ("File successfully saved in% s \ r \ n"% upload_destination)
 except:
 client_socket. submit ("Could not save file to% s \ r \ n"% upload_destination)



# check command execution
si len (run):

 # run the command
 output = run_command (execute)

 client_socket. send (output)


# now we go to another loop if a command shell was requested
if command:

 while it is true:
 # display a simple message
client_socket. send ("<BHP: #>")

 # now we receive until we see a line break ¬
 (enter password)
 cmd_buffer = ""
 while "\ n" is not in cmd_buffer:
 cmd_buffer + = client_socket. recv (1024)


 # send back command output
 response = run_command (cmd_buffer)

 # returns the response
 client_socket. send (reply)

principal ()
