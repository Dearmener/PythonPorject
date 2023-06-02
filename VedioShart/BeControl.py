import sounddevice as sd
import numpy as np
import socket

# 配置网络参数
HOST = '192.168.0.104'  # 替换为控端的IP地址
PORT = 12345  # 替换为控端的端口号

# 配置音频参数
SAMPLE_RATE = 44100
CHANNELS = 2
BLOCK_SIZE = 1024

# 创建Socket连接
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
sock.connect(server_address)

# 变量用于检测音频数据是否到达
data_received = False

# 回调函数，用于捕获音频数据并发送到控端
def callback(indata, frames, time, status):
    global data_received
    sock.sendall(indata.tobytes())
    data_received = True

# 开始音频捕获和发送
print("开始传输音频...")
with sd.InputStream(callback=callback, channels=CHANNELS, samplerate=SAMPLE_RATE, blocksize=BLOCK_SIZE):
    while True:
        data = sock.recv(BLOCK_SIZE)
        if not data:
            break
        audio_data = np.frombuffer(data, dtype=np.float32)
        num_samples = len(audio_data) // CHANNELS
        reshaped_data = audio_data[:num_samples * CHANNELS].reshape((num_samples, CHANNELS))
        # 播放音频数据
        sd.play(reshaped_data, samplerate=SAMPLE_RATE)
        # 等待音频数据被播放完毕
        sd.wait()
        # 判断是否有新的音频数据到达
        if data_received:
            print("被控端输出了声音")
            data_received = False

# 关闭连接和音频流
sock.close()
