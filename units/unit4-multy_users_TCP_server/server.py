import select

"""the function gets 3 params:
1. read_list - list of sockets we might want to read from
2. write_list - list of sockets we might want to write from
3. error_list - list of sockets we might want to know if there was an error in them"""
ready_to_read, ready_to_write, in_error = select.select([server_socket] + client_socket, [], [])


