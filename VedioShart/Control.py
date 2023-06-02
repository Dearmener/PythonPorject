import sounddevice as sd
import numpy as np
import socket

# 配置网络参数
HOST = '192.168.0.102'
PORT = 12345  # 替换为被控端的端口号

# 配置音频参数
SAMPLE_RATE = 44100
CHANNELS = 2
BLOCK_SIZE = 1024

# 创建Socket连接
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
sock.bind(server_address)
sock.listen(1)
connection, client_address = sock.accept()

# 回调函数，用于接收音频数据并播放
def callback(outdata, frames, time, status):
    data = connection.recv(BLOCK_SIZE)
    outdata[:] = np.frombuffer(data, dtype=np.float32).reshape((BLOCK_SIZE, CHANNELS))

# 开始音频播放和接收
print("开始接收音频...")
stream = sd.OutputStream(callback=callback, channels=CHANNELS, samplerate=SAMPLE_RATE, blocksize=BLOCK_SIZE)
stream.start()

# 等待音频传输完成
while True:
    pass

# 关闭连接
stream.stop()
connection.close()
sock.close()
