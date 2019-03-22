import selectors
import socket
import types
import sys

# initial configuration

sel = selectors.DefaultSelector()

host = '127.0.0.1'
port = 9999

lsock = socket.socket(socket.AF_INET, socket.SOCKSTREAM)
lsock.bind((host, port))
lsock.listen()
print('listening on', (host, port))
lsock.setblocking(False) # lsock.setblocking(False) to configure the socket in non-blocking mode

sel.register(lsock, selectors.EVENT_READ, data=None) # sel.register() registers the socket to be monitored with sel.select() for the events you’re interested in. For the listening socket, we want read events: selectors.EVENT_READ.

# event loop
while True:
    events = sel.select(timeout=None) # blocks until there are sockets ready for I/O. It returns a list of (key, events) tuples, one for each socket. [key] is a SelectorKey namedtuple that contains a fileobj attribute. [key.fileobj] is the socket object, and mask is an event mask of the operations that are ready.
    for key, mask in events:
        if key.data is None:
            accept_wraper(key.fileobj)
            # If key.data is None, then we know it’s from the listening socket and we need to accept() the connection. We’ll call our own accept() wrapper function to get the new socket object and register it with the selector. We’ll look at it in a moment.
        else:
            service_connection(key, mask)
            # If key.data is not None, then we know it’s a client socket that’s already been accepted, and we need to service it. service_connection() is then called and passed key and mask, which contains everything we need to operate on the socket.

# the accept_wraper function
def accept_wraper(sock):
    conn, addr = sock.accept() # should be ready to read
    print('Accepted connection from....', addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
    # Next, we create an object to hold the data we want included along with the socket using the class types.SimpleNamespace.
    events =  selectors.EVENT_READ | selectors.EVENT_WRITE
    # Since we want to know when the client connection is ready for reading and writing, both of those events are set
    sel.register(conn, events, data=data)

# the service_connection function
def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024) # should be ready to read
        if recv_data:
            data.outb += recv_data
        else:
            print('closing connection to..', data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('echoing', repr(data.outb), 'to', data.addr)
            sent = sock.send(data.outb) # should be ready to write
            data.outb = data.outb[sent:]

