import sounddevice as sd
import numpy as np
import socket

# 配置网络参数
HOST = '192.168.0.102'  # 替换为控端的IP地址
PORT = 12345  # 替换为控端的端口号

# 配置音频参数
SAMPLE_RATE = 44100
CHANNELS = 2
BLOCK_SIZE = 1024

# 创建Socket连接
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
sock.connect(server_address)

# 回调函数，用于捕获音频数据并发送到控端
def callback(indata, frames, time, status):
    sock.sendall(indata.tobytes())

# 开始音频捕获和发送
print("开始传输音频...")
stream = sd.InputStream(callback=callback, channels=CHANNELS, samplerate=SAMPLE_RATE, blocksize=BLOCK_SIZE)
stream.start()

# 等待音频传输完成
while True:
    pass

# 关闭连接
stream.stop()
sock.close()
