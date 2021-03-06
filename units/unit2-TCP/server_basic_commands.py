import random
import socket
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# This ip tells the server to listen to every client from the computer or outside
server_socket.bind(("0.0.0.0", 8820))
server_socket.listen()
print("Server is up and running")
# The accept method returns a tuple.
# the first value is a socket object
# the second value is a tuple that contains the IP and the PORT of the client that got connected
(client_socket, client_address) = server_socket.accept()
print("Client connected")
while True:
    data = client_socket.recv(1024).decode()
    if data == "NAME":
        client_socket.send("Basic command server".encode())
    elif data == "TIME":
        client_socket.send(time.asctime(time.gmtime()).encode())
    elif data == "RAND":
        client_socket.send(random.randrange(1, 10).__str__().encode())
    elif data == "Quit":
        print("closing client socket now...")
        client_socket.send("Bye".encode())
        break
    else:
        client_socket.send("Please choose another request\n".encode())
# After closing the client socket the server continue to listen
client_socket.close()
# After closing the server socket the communication with clients is over
server_socket.close()
