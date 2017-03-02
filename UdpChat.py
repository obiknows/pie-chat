# UdpChat.py -> a UDP Chat application in python
# written by sam nnodim (son2105)
import sys, cmd, socket

# THE CLIENT
# def client(args, prompt, intro):


# THE SERVER
def server(port, prompt, intro):
    # create the client's table
    clients = {}

    # create the socket
    host = '127.0.0.1'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind( (host, int(port)) )
    print ( intro )
    print ( prompt + 'server is running at '+host+':'+port)
    print ( prompt )

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
    intro = 'Welcome to UChat. Type help or ? to list commands.\n'
    prompt = '$>>> '

    if (mode[0] == 'client'):      # in client, mode.
        client(mode, prompt, 'Welcome to UChat.\n')
    else:                          # in server, mode.
        server(mode[1], prompt, 'Welcome to UChat Server.\n')


# run the program
if __name__ == '__main__':
    main(sys.argv)
