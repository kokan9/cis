import socket
import ssl

context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

secure_sock = context.wrap_socket(sock, server_hostname="localhost")

secure_sock.connect(("localhost", 8443))

secure_sock.sendall(b"Hello Server!")

data = secure_sock.recv(1024)

print("Received from server: ", data.decode())

secure_sock.close()
