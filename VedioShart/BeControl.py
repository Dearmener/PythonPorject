import socket
import pyaudio

# 配置音频参数
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# 创建套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.0.102', 12345)  # 替换为控端的IP地址和端口号
sock.connect(server_address)

# 初始化音频输入
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

print("开始传输音频...")
while True:
    data = stream.read(CHUNK)
    sock.sendall(data)

# 关闭连接
stream.stop_stream()
stream.close()
audio.terminate()
sock.close()
