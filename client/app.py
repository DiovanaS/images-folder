from base64 import b64encode
from colorama import Fore
from io import BytesIO
from PIL import ImageGrab
from pynput.keyboard import Key, KeyCode, Listener
from socketio import Client
from typing import Literal
import colorama


# parameter _

SERVER_HOST = 'wss://images-folder.onrender.com/'


# service _

def print_screen() -> str:
    screenshot = ImageGrab.grab()
    with BytesIO() as buffer:
        screenshot.save(buffer, format='png')
        base64 = b64encode(buffer.getvalue())
        return base64.decode('utf-8')


# communication _

def display_presentation() -> None:
    print(
        f'{Fore.WHITE} * Serving WebSocket Client\n'
        f'{Fore.YELLOW}Press PRINTSCREEN to send screenshot or ESC to quit'
    )


def handle_emission(
    event: Literal['success', 'error'],
    message: str
) -> None:
    color = Fore.GREEN if event == 'success' else Fore.RED
    print(f'{color}{message}')


# execution _

if __name__ == '__main__':
    # _ initialize colorama
    colorama.init(autoreset=True)

    # _ display presentation (obviously)
    display_presentation()

    # _ instantiate socketio client
    socket_io = Client()

    # _ define event handlers
    for event in ('success', 'error'):
        handler = lambda message, event=event: handle_emission(
            event, 
            message
        )
        socket_io.on(event, handler)

    # _ connect to server
    socket_io.connect(SERVER_HOST)

    # _ define key events
    def on_press(key: KeyCode) -> None:
        # _ press print screen - send screenshot
        if key == Key.print_screen:
            base64 = print_screen()
            socket_io.emit('print_screen', base64)
        # _ press esc - disconnect and terminate the program
        elif key == Key.esc:
            socket_io.disconnect()
            exit(0)

    # _ listen for keyboard key press
    with Listener(on_press) as listener:
        listener.join()
