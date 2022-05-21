# share_file
A simple client-server app used to send and receive file over web-socket


## Installation
```console
$ pip install tqdm sockets
```

## Use
- #### Server
```console
$ ./server.py <host|ip> <port>
```

- #### Client
```console
$ ./send_file.py <file_to_send> <server host|ip> <server port>
```

## Note
If a file with the same name of `<file_to_send>` is existed in the directory  
that `./server.py` runs in there, the sending operation won't work.
