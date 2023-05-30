from PIL import Image, ImageDraw, ImageFont

# 输入字符串
text = input("请输入要显示的字符串：")

# 壁纸尺寸
width = 1920
height = 1080

# 创建黑色底图
background = Image.new("RGB", (width, height), "#666666")

# 创建绘制对象
draw = ImageDraw.Draw(background)

# 字体和字号
font_size = 100

font_path = "/Users/mengguoqing/Library/Fonts/LXGWWenKai-Regular.ttf"  # 替换为正确的字体文件路径
font = ImageFont.truetype(font_path, font_size)

# 获取文本边界框
text_bbox = draw.textbbox((0, 0), text, font=font)

# 计算字符串的宽度和高度
text_width = text_bbox[2] - text_bbox[0]
text_height = text_bbox[3] - text_bbox[1]

# 计算字符串的位置
x = (width - text_width) // 2
y = (height - text_height) // 2

# 在底图上绘制字符串
draw.text((x, y), text, font=font, fill="#CC9966")

# 显示壁纸
background.show()

# 保存壁纸
background.save("wallpaper.png")
