import socket
import select

MAX_MSG_LENGTH = 1024
SERVER_PORT = 5555
SERVER_IP = "0.0.0.0"


def print_clients_sockets(client_sockets):
    for c in client_sockets:
        """The function getpeername() returns the client IP and PORT"""
        print("\t", c.getpeername())


def main():
    print("Setting up server...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen()
    # This is the list of all the socket objects that will connect to the server
    print("Listening for clients...")
    client_sockets = []
    messages_to_send = []
    while True:
        ready_to_read, ready_to_write, in_error = select.select([server_socket] + client_sockets, client_sockets, [])
        for current_socket in ready_to_read:
            """If the current socket is the server socket it means that a new client is trying to connect"""
            if current_socket is server_socket:
                (client_socket, client_address) = current_socket.accept()
                print("New client joined!", client_address)
                client_sockets.append(client_socket)
                print_clients_sockets(client_sockets)
            else:
                print("New data from client")
                try:
                    data = current_socket.recv(MAX_MSG_LENGTH).decode()
                    if data == "":
                        print("Connection closed")
                        client_sockets.remove(current_socket)
                        current_socket.close()
                        print_clients_sockets(client_sockets)
                    else:
                        # current_socket.send(data.encode())
                        messages_to_send.append((current_socket, data))
                    for message in messages_to_send:
                        current_socket, data = message
                        if current_socket in ready_to_write:
                            current_socket.send(data.encode())
                            messages_to_send.remove(message)
                except:
                    client_sockets.remove(current_socket)
                    current_socket.close()
                    print("The active sockets are: " + client_sockets)


main()
