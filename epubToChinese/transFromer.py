import ebooklib
from ebooklib import epub
from opencc import OpenCC

# 定义一个函数，用于将字符串中的繁体字转换为简体字
def convert_to_simplified_chinese(text):
    cc = OpenCC('t2s')  # 创建一个简繁体转换器，从繁体转换为简体
    return cc.convert(text)

# 定义一个函数，用于将 EPUB 文件中的所有 HTML 文件的内容转换为简体中文
def convert_epub_to_simplified_chinese(epub_file_path, output_file_path):
    try:
        # 读取 EPUB 文件
        book = epub.read_epub(epub_file_path)

        # 遍历所有的 HTML 文件，将内容中的繁体字转换为简体
        for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            content = item.get_content().decode('utf-8')
            converted_content = convert_to_simplified_chinese(content)
            item.set_content(converted_content.encode('utf-8'))

        # 将修改后的 EPUB 文件保存为新文件
        epub.write_epub(output_file_path, book)

    except (IOError, OSError, ValueError, epub.EpubException) as error:
        print("Error: " + str(error))

# 调用函数，将 EPUB 文件中的所有繁体字转换为简体字，并保存为新文件
convert_epub_to_simplified_chinese('input.epub', 'output.epub')
