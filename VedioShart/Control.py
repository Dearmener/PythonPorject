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

# 获取音频输入设备列表及其索引
def get_input_devices():
    devices = sd.query_devices()
    input_devices = []
    for idx, device in enumerate(devices):
        if device['max_input_channels'] > 0:
            input_devices.append((idx, device['name']))
    return input_devices

# 打印音频输入设备列表供客户选择
def print_input_devices(input_devices):
    print("可用的音频输入设备：")
    for idx, device_name in input_devices:
        print(f"[{idx}] {device_name}")

# 选择音频输入设备
def select_input_device(input_devices):
    while True:
        selection = input("请选择音频输入设备的索引号：")
        try:
            device_idx = int(selection)
            if device_idx in [idx for idx, _ in input_devices]:
                return device_idx
            else:
                print("无效的设备索引号，请重新选择。")
        except ValueError:
            print("无效的输入，请输入设备索引号的整数值。")

# 创建Socket连接
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
sock.bind(server_address)
sock.listen(1)
connection, client_address = sock.accept()

# 获取音频输入设备列表并让客户选择
input_devices = get_input_devices()
print_input_devices(input_devices)
input_device_idx = select_input_device(input_devices)

# 回调函数，用于接收音频数据并播放
def callback(outdata, frames, time, status):
    data = connection.recv(BLOCK_SIZE)
    outdata[:] = np.frombuffer(data, dtype=np.int16).reshape((BLOCK_SIZE, CHANNELS))

# 开始音频播放和接收
print("开始接收音频...")
input_device_info = sd.query_devices()[input_device_idx]
