from PIL import Image
from fpdf import FPDF
import os

def images_to_pdf(input_folder):
    # 获取文件夹名称
    folder_name = os.path.basename(input_folder)
    # 创建一个新的PDF文件
    pdf_file = FPDF()
    # 遍历文件夹中的所有图像文件
    for image_file in os.listdir(input_folder):
        # 如果文件是图像文件则将其添加到PDF文件中
        if image_file.endswith(".jpg") or image_file.endswith(".png"):
            # 打开图像文件并获取其大小
            img = Image.open(os.path.join(input_folder, image_file))
            width, height = img.size
            pdf_file.add_page()
            pdf_file.image(os.path.join(input_folder, image_file), w=width, h=height)
    # 保存PDF文件
    pdf_file.output(folder_name + ".pdf")

# 调用函数并传入文件夹路径
# images_to_pdf("path/to/folder")

# 调用函数并传入文件夹路径
images_to_pdf("/Users/mengguoqing/Desktop/PythonProjects/pycharmProject/demo/雅思写作讲义/雅思写作范文合集/【Oliver雅思托福】雅思写作Task1范文（全体烤鸭必备）")
