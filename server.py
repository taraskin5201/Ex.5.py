import socket

# Створюємо TCP сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Задаємо IP-адресу та порт для прослуховування
server_address = ('localhost', 12345)

# Прив'язуємо сокет до вказаної адреси та порту
server_socket.bind(server_address)

# Починаємо прослуховування з'єднань
server_socket.listen(1)
print('Сервер слухає на порту 12345...')

# Приймаємо вхідне з'єднання
client_socket, client_address = server_socket.accept()
print('З'єднання встановлено з', client_address)

# Обмін повідомленнями
while True:
    message = input('Введіть повідомлення для клієнта: ')
    client_socket.send(message.encode('utf-8'))
    received_message = client_socket.recv(1024).decode('utf-8')
    print('Повідомлення від клієнта:', received_message)

# Закриваємо з'єднання та сокет
client_socket.close()
server_socket.close()
