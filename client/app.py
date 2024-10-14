from base64 import b64encode
from colorama import Fore, Style
from io import BytesIO
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from socketio import Client
from typing import Literal
import colorama


# parameter _

SERVER_HOST = 'ws://127.0.0.1:5000'


# service _

def print_screen() -> str:
    screenshot = ImageGrab.grab()
    with BytesIO() as buffer:
        screenshot.save(buffer, format='png')
        base64 = b64encode(buffer.getvalue())
        return base64.decode('utf-8')


# feedback _

def handle_emission(
    event: Literal['success', 'error'],
    message: str
) -> None:
    color = Fore.GREEN if event == 'success' else Fore.RED
    print(f'{color}{message}{Style.RESET_ALL}')


# execution _

if __name__ == '__main__':
    # step 1: initialize colorama
    colorama.init()

    # step 2: instantiate socket client
    socket_io = Client()

    # step 3: define event handlers
    for event in ('success', 'error'):
        handler = lambda message: handle_emission(event, message)
        socket_io.on(event, handler)

    # step 4: connect to server
    socket_io.connect(SERVER_HOST)

    # step 5 onwards: listen for print screen press
    def on_press(key: Key) -> None:
        if key == Key.print_screen:
            base64 = print_screen()
            socket_io.emit('print_screen', base64)
            
    with Listener(on_press) as listener:
        listener.join()
