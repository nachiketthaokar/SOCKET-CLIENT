from concurrent.futures import thread
import socket
from threading import Thread

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

def receive(self):
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message == 'NICKNAME':
                client.send(self.name.encode('utf-8'))
            else:
                self.show_message(message)
        except:
            print("An error occured!")
            client.close()
            break

def write(self):
    while True:
        message = (f"{self.name}: {self.msg}")
        client.send(message.encode('utf-8'))
        self.show_message(message)
        break

receive_thread = Thread(target=receive)
receive_thread.start()
write_thread = Thread(target=write)
write_thread.start()


        


   