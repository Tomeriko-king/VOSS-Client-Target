from pathlib import Path

from take_screenshot import self_screenshot
from voss_socket import VOSSSocketClient, VOSSSocketClientTarget

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345


def tcp_connect_and_handle_loop():
    socket_target = VOSSSocketClientTarget()
    socket_target.connect(SERVER_IP)

    while True:
        socket_target.recv_take_screenshot_request()

        local_filename = self_screenshot()

        socket_target.send_take_screenshot_response(Path(local_filename))
