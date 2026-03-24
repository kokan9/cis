import socket
import ssl

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile = "server.crt", keyfile = "server.key")
server_address = ('localhost', 8443)
sock.bind(server_address)
sock.listen()
print("Waiting for a connection...")

while True:
    connection, client_address = sock.accept()
    secure_connection = None
    try: 
        print("Connection from", client_address)
        secure_connection = context.wrap_socket(connection, server_side = True)
        data = secure_connection.recv(1024)
        print("Received: ",data)
        message = "Hello, Client!"
        secure_connection.sendall(message.encode("UTF-8"))
    except ssl.SSL_Error as e:
        print("SSL Error: ", e)
    finally:
        if secure_connection is not None:
            secure_connection.close()