from PIL import ImageGrab


def self_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")
    screenshot.close()


#writing a main code for the server handling clients


available_clients = []
def hold_clients():