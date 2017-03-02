# UdpChat.py -> a UDP Chat application in python
# written by sam nnodim (son2105)
import sys, cmd, socket, json

# THE CLIENT
def client(args, prompt, intro):
    # create the client's table
    clients = {}

    # parse the args
    NAME         = args[1]
    SERV_IP      = args[2]
    SERV_PORT    = int(args[3])
    PORT         = args[4]

    # create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # register on the server
    regsitration_form = {
        'name': NAME,
        'addr': sock.getsockname()[0],
        'port': PORT,
    }
    message = json.dumps(regsitration_form)

    print (message)
    sent = sock.sendto(message, (SERV_IP, SERV_PORT))
    # (data, server) = sock.recvfrom(4096)

    sock.close()

# THE SERVER
def server(port, prompt, intro):
    # create the client's table
    clients = {}

    # create the socket
    HOST = '127.0.0.1'
    PORT =  int(port)

    sock = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
    sock.bind( ('',PORT) )
    # sock.listen(5)

    # start the prompt
    print ( intro )
    print ( prompt + 'server is listening at '+HOST+':'+port)
    print ( prompt )

    while True:
        # accept registrations
        (data, clientIP) = sock.recvfrom(4096)
        print prompt, "received message:", data
        pass

def determineMode(args):
    # if (-s) is passed, go into "server mode"
    if(len(args) == 3 and args[1] == '-s'):
        return ('server', args[2])
        # return -> (-s, server-port)
    elif(len(args) == 6 and args[1] == '-c'):
        return ('client', args[2], args[3], args[4], args[5]  )
        # return -> (-c , nick-name, server-ip, server-port, client-port)
    else:
        return None;  # return nothing if mode cannot be determined

# MAIN LOOP
def main(argv):
    # validate # of inputs, then parse command-line args
    mode = determineMode(argv)

    if ( mode is None ):
        sys.exit('\n\tIncorrect Syntax: To start UChat, run `python UdpChat.py <-c|-s> <command-line arguments>`\n')

    # Setup the "shell" chat env.
    prompt = '$>>> '

    if (mode[0] == 'client'):      # in client, mode.
        client(mode, prompt, 'Welcome to UChat.\n')
    else:                          # in server, mode.
        server(mode[1], prompt, 'Welcome to UChat Server.\n')


# run the program
if __name__ == '__main__':
    main(sys.argv)
