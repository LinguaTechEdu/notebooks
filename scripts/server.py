"""
What's going on here?

In summary, this is a server script. It creates a portal (socket) for clients to use to connect. This server
listens to the port for anyone trying to connect to its address (ip).

socket.accept   returns (conn, addr)
"""
import socket
import threading

# The address and port for our server
bind_ip = "0.0.0.0"
bind_port = 9999

# The server (socket) is assigned the address
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))

# The server listens for any callers, but only up to 5 at a time.
server.listen(5)

# A message to print to console to confirm that the server is running.
print"[*] Listening on %s:%d" % (bind_ip, bind_port)

def handle_client(client_socket):
    """Get client messages and send acknowledgement of receipt."""
    request = client_socket.recv(1024)
    print "[*] Received: %s" % request
    client_socket.send("Message sent.")
    client_socket.close()

# Now keep listening forever for client requests.
while True:
    client, addr = server.accept()
    print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
