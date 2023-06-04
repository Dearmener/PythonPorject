
import socket
import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

def send_audio(ip, port):
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))

    try:
        while True:
            data = stream.read(CHUNK)
            sock.sendall(data)
    finally:
        sock.close()
        stream.stop_stream()
        stream.close()
        p.terminate()

def receive_audio(ip, port):
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=CHUNK)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ip, port))
    sock.listen(1)

    conn, addr = sock.accept()
    print("连接来自：", addr)

    try:
        while True:
            data = conn.recv(CHUNK)
            stream.write(data)
    finally:
        conn.close()
        sock.close()
        stream.stop_stream()
        stream.close()
        p.terminate()

# 请根据实际情况修改IP和端口
sender_ip = "192.168.1.2"
receiver_ip = "192.168.1.3"
port = 12345

# 发送端电脑运行
send_audio(sender_ip, port)

# 接收端电脑运行
receive_audio(receiver_ip, port)