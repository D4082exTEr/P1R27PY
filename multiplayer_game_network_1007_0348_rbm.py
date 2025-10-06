# 代码生成时间: 2025-10-07 03:48:36
import socket
import threading
import json
from queue import Queue


# 定义一个游戏客户端类
class GameClient:
    def __init__(self, host, port, username):
        self.host = host
        self.port = port
        self.username = username
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.queue = Queue()
        self.running = False
        self.game_state = None
        
    # 连接到服务器
def connect_to_server(self):
        try:
            self.socket.connect((self.host, self.port))
            self.running = True
            self.start_listener()
            self.start_sender()
        except Exception as e:
            print(f"连接服务器失败: {e}")
        
    # 开始监听服务器消息
def start_listener(self):
        def receive():
            try:
                while self.running:
                    message = self.socket.recv(1024).decode('utf-8')
                    if message:
                        self.queue.put(message)
            except Exception as e:
                print(f"接收消息失败: {e}")
                self.stop()
        
        threading.Thread(target=receive).start()
        
    # 开始发送消息到服务器
def start_sender(self):
        def send():
            try:
                while self.running:
                    message = self.queue.get()
                    if message:
                        self.socket.sendall(message.encode('utf-8'))
            except Exception as e:
                print(f"发送消息失败: {e}")
                self.stop()
        
        threading.Thread(target=send).start()
        
    # 发送消息
def send_message(self, message):
        try:
            self.queue.put(message)
        except Exception as e:
            print(f"发送消息失败: {e}")
        
    # 停止客户端
def stop(self):
        self.running = False
        self.socket.close()
        self.queue.queue.clear()
        
    # 获取游戏状态
def get_game_state(self):
        return self.game_state
        
    # 设置游戏状态
def set_game_state(self, game_state):
        self.game_state = game_state
        

# 定义一个游戏服务器类
class GameServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        
    # 开始监听客户端连接
def start_listener(self):
        def accept_connections():
            try:
                while True:
                    client_socket, client_address = self.server_socket.accept()
                    client = GameClient(client_address[0], client_address[1], "Anonymous")
                    client.socket = client_socket
                    self.clients.append(client)
                    print(f"客户端 {client_address} 已连接")
                    self.handle_client(client)
            except Exception as e:
                print(f"监听客户端连接失败: {e}")
        
        threading.Thread(target=accept_connections).start()
        
    # 处理客户端
def handle_client(self, client):
        def receive():
            try:
                while True:
                    message = client.socket.recv(1024).decode('utf-8')
                    if message:
                        self.broadcast_message(message, client)
            except Exception as e:
                print(f"接收消息失败: {e}")
                self.remove_client(client)
        
        threading.Thread(target=receive).start()
        
    # 广播消息
def broadcast_message(self, message, sender):
        for client in self.clients:
            if client != sender:
                try:
                    client.socket.sendall(message.encode('utf-8'))
                except Exception as e:
                    print(f"发送消息失败: {e}")
                    self.remove_client(client)
        
    # 移除客户端
def remove_client(self, client):
        self.clients.remove(client)
        print(f"客户端 {client.socket.getpeername()} 已断开连接")
        
    # 停止服务器
def stop(self):
        self.server_socket.close()
        for client in self.clients:
            client.socket.close()
        

# 测试代码
def main():
    host = '127.0.0.1'
    port = 12345
    username = 'Player1'
    client = GameClient(host, port, username)
    client.connect_to_server()
    while True:
        try:
            message = input("Enter message: ")
            client.send_message(message)
        except Exception as e:
            print(f"发送消息失败: {e}")
            break
    client.stop()

if __name__ == '__main__':
    main()