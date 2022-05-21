#!/usr/bin/env python3

import socket
import _thread as thread
import os
import sys

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 * 4  #  4kb


ServerSideSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = sys.argv[1:3]
ThreadCount = 0


try:
    ServerSideSocket.bind((host, int(port)))
except socket.error as err:
    print(str(err))
    exit(1)

print(f"Socket is listening on {host}:{port}")
ServerSideSocket.listen()


def multi_threaded_client(connection):
    data = connection.recv(BUFFER_SIZE).decode()

    if SEPARATOR in data:
        file_name = data.split(SEPARATOR)[0]

        if not os.path.exists(f"{file_name}"):
            with open(f"{file_name}", "wb") as file:

                while True:
                    data = connection.recv(BUFFER_SIZE)
                    file.write(data)

                    if not data:
                        break

    connection.close()


try:
    while True:
        Client, address = ServerSideSocket.accept()
        print("Connected to: " + address[0] + ":" + str(address[1]))
        thread.start_new_thread(multi_threaded_client, (Client,))
        ThreadCount += 1
        print("Connection Number: " + str(ThreadCount))

except KeyboardInterrupt:
    ServerSideSocket.close()
    print("\rServer stoped\nBye")
