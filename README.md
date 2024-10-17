### 📁 Images Folder

#### 🇧🇷 Português

Ecossistema dividido em servidor e cliente para o envio de capturas de tela através de comunicação via WebSocket. Quando o cliente pressiona a tecla `Print Screen`, uma captura da tela é enviada ao servidor no formato base64. O servidor reconstrói a imagem em formato PNG, armazena-a no diretório de uploads e envia uma confirmação, que é devidamente interpretada pelo cliente. O desenvolvimento seguiu o estilo Pythonic, com uma arquitetura simples e direta, consolidando todo o código em um único arquivo.

#### 🇺🇸 English

An ecosystem divided into server and client for sending screenshots via WebSocket communication. When the client presses the `Print Screen` key, a screenshot is sent to the server in base64 format. The server reconstructs the image in PNG format, stores it in the uploads directory, and sends a confirmation, which is properly interpreted by the client. The development followed the Pythonic style, with a simple and straightforward architecture, consolidating all the code into a single file.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Socket.io](https://img.shields.io/badge/Socket.io-25c2a20?style=for-the-badge&logo=socket.io&badgeColor=white)

### 🛠️ Installation and Configuration

The applications was developed using **Python 3.11**, and it is recommended to use this version to ensure compatibility. You will need to obtain a local copy of the source code, which can be done with the following command:

```bash
git clone https://github.com/DiovanaS/images-folder
```

After that, you must configure each application individually. Start with the [**🗄️ Server**](./server/README.md). Then, proceed to the [**💻 Client**](./client/README.md).

### ⚖️ License

This project adopts the **MIT License**, which allows you to use and make modifications to the code as you wish. The only thing I ask is that proper credit is given, acknowledging the effort and time I invested in building it.
