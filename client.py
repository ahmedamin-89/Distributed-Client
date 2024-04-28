import socket

def receive_file(client_socket, save_filename):
    """ Receive the processed file from the server. """
    with open(save_filename, 'wb') as f:
        while True:
            data = client_socket.recv(1024)
            if data.endswith(b'END'):
                data = data[:-3]  # Remove the 'END' marker
                f.write(data)
                break
            f.write(data)

def send_request(operation, filename):
    """Send an image processing request to the server along with the image file."""
    host = 'localhost'
    port = 4000
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    message = f"{operation},{filename}"
    client_socket.send(message.encode())
    
    receive_file(client_socket, f"received_{filename}")
    
    print(f"Processed image saved as 'received_{filename}'")
    client_socket.close()

def main():
    operation = input("Enter the operation (grayscale, blur, edges): ")
    filename = input("Enter the filename of the image: ")
    send_request(operation, filename)

if __name__ == "__main__":
    main()
