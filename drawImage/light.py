from PIL import Image, ImageDraw, ImageFont, ImageFilter

# 输入字符串
text = input("请输入要显示的字符串：")

# 壁纸尺寸
width = 1920
height = 1080

# 创建黑色底图
background = Image.new("RGB", (width, height), "black")

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

# 创建文本图像
text_image = Image.new("RGBA", (text_width, text_height), (0, 0, 0, 0))
text_draw = ImageDraw.Draw(text_image)
text_draw.text((0, 0), text, font=font, fill=(255, 255, 255, 255))

# 应用模糊滤镜
blurred_text = text_image.filter(ImageFilter.GaussianBlur(radius=2))

# 将模糊文本图像粘贴到底图上
background.paste(blurred_text, (x, y), blurred_text)

# 显示壁纸
background.show()

# 保存壁纸
background.save("wallpaper.png")
