import PyPDF2

# 打开PDF文件
pdf_file = open('file.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# 创建一个新的PDF写入器
pdf_writer = PyPDF2.PdfWriter()

# 遍历每一页
for page_num in range(len(pdf_reader.pages)):
    # 获取当前页
    page = pdf_reader.pages[page_num]
    # 遍历每个内容对象
    for content in page["/Contents"].get_objects():
        if content == b'\n':
            continue
        # 如果内容是文本对象
        if isinstance(content, PyPDF2.pdf.ContentStream):
            for operands, operator in content.operations:
                if operator == b'Tf':
                    # 将字体修改为新字体
                    operands[0] = "/LXGW WenKai"
            # 将修改后的内容添加到新的PDF写入器
            pdf_writer.add_page(page)
            break

# 保存修改后的PDF文件
pdf_output = open('example_modified.pdf', 'wb')
pdf_writer.write(pdf_output)

# 关闭文件
pdf_file.close()
pdf_output.close()
