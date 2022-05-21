#!/usr/bin/env python3

import socket
import tqdm
import os


SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 * 4  #  4kb


def send_file(file_path, host, port):
    file_name = os.path.basename(os.path.realpath(file_path))
    file_size = os.path.getsize(file_path)

    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"[+] Connecting to {host}:{port}")
    ClientSocket.connect((host, port))
    print("[+] Connected")

    data = f"{file_name}{SEPARATOR}".encode()
    ClientSocket.send(data)

    progress = tqdm.tqdm(range(file_size // 1024), f"Sending {file_name[:20]}...: ", unit="KB", unit_scale=True, unit_divisor=1024)

    with open(file_path, "rb") as file:
        while True:
            bytes_read = file.read(BUFFER_SIZE)
            if not bytes_read:
                break

            ClientSocket.sendall(bytes_read)
            progress.update(len(bytes_read) // 1024)

    ClientSocket.close()


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Simple File Sender")
    parser.add_argument("file", help="File name to send")
    parser.add_argument("host", help="The IP/Domain of receiver")
    parser.add_argument("port", help="Port to use")

    args = parser.parse_args()

    file_path = args.file
    host = args.host
    port = args.port

    send_file(file_path, host, int(port))


if __name__ == "__main__":
    main()
