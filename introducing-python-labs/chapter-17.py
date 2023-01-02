# Network utilities
import socket

print(socket.gethostbyname('www.amazon.com'))
print(socket.getaddrinfo('www.amazon.com', 80))

#many examples in book for networking, PRC, serialization and parallelism