from base64 import b64decode
from flask import Flask, send_file
from flask_socketio import SocketIO, emit
from http import HTTPStatus
from os import path
from pathlib import Path
from uuid import uuid4


# path _

UPLOADS_DIR = Path.cwd() / 'uploads'


# parameter _

ALLOWED_HOSTS = '*'
JSON_SORT_KEYS = False
WEBSOCKET_MAX_MESSAGE_SIZE = 1024 * 1024 * 8


# configuration _

def _create_uploads_dir() -> None:
    UPLOADS_DIR.mkdir(exist_ok=True)


def _configure_socket_io(
    app: Flask,
    socket_io: SocketIO
) -> None:
    socket_io.init_app(
        app,
        cors_allowed_origins=ALLOWED_HOSTS,
        websocket_max_message_size=WEBSOCKET_MAX_MESSAGE_SIZE
    )


def configure_enviroment(
    app: Flask,
    socket_io: SocketIO
) -> None:
    app.json.sort_keys = JSON_SORT_KEYS
    _configure_socket_io(app, socket_io)
    _create_uploads_dir()


# instance _

app = Flask(__name__)
socket_io = SocketIO()
configure_enviroment(app, socket_io)


# service _

def generate_file_name() -> str:
    return f'{uuid4()}.png'


def compose_file_path(file_name: str) -> Path:
    if not file_name.endswith('.png'): file_name += '.png'
    return UPLOADS_DIR / file_name


def save_image(base64: str, file_path: Path) -> None:
    content = b64decode(base64)
    with open(file_path, 'wb') as buffer:
        buffer.write(content)


# event _

@socket_io.on('print_screen')
def on_print_screen(base64: str) -> None:
    file_name = generate_file_name()
    file_path = compose_file_path(file_name)
    save_image(base64, file_path)
    emit('success', f'The image has been saved as {file_name}')


# route _

@app.get('/')
def root():
    return {
        'title': 'Images Folder',
        'description': (
            'A server for processing captures. '
            'Upload base64-encoded images via WebSocket, '
            'and the server saves them as PNG files.'
        ),
        'authors': [
            'davidsantana06',
            'DiovanaS'
        ],
        'repository': 'https://github.com/DiovanaS/images-folder'
    }


@app.get('/<string:reference>')
def get_image(reference: str):
    file_path = compose_file_path(reference)
    if not path.exists(file_path):
        return (
            {'message': 'Image not found.'}, 
            HTTPStatus.NOT_FOUND
        )
    return send_file(file_path, as_attachment=True)
