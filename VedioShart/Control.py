import socket
import pyaudio

# 配置音频参数
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# 创建套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('192.168.0.102', 12345)  # 绑定本机IP地址和一个未被占用的端口号
sock.bind(server_address)
sock.listen(1)

# 初始化音频输出
audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

print("等待连接...")
connection, client_address = sock.accept()
print("已连接:", client_address)

print("开始接收音频...")
while True:
    data = connection.recv(CHUNK)
    if not data:
        break
    stream.write(data)

# 关闭连接
stream.stop_stream()
stream.close()
audio.terminate()
connection.close()
sock.close()
