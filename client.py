import socket

# Створюємо TCP сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Задаємо IP-адресу та порт сервера
server_address = ('localhost', 12345)

# Намагаємося встановити з'єднання з сервером
client_socket.connect(server_address)
print('З\'єднання з сервером встановлено...')

# Обмін повідомленнями
while True:
    received_message = client_socket.recv(1024).decode('utf-8')
    print('Повідомлення від сервера:', received_message)
    message = input('Введіть повідомлення для сервера: ')
    client_socket.send(message.encode('utf-8'))

# Закриваємо з'єднання та сокет
client_socket.close()
