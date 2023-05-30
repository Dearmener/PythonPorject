# import re
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.tag import pos_tag
# from PyPDF2 import PdfReader
#
# nltk.download('punkt')
# # 设置NLTK使用的标注器
# nltk.download('averaged_perceptron_tagger')
#
# # 读取PDF文件并识别英文单词和短语
# def read_pdf_extract_english_words_and_phrases(file_path):
#     with open(file_path, 'rb') as file:
#         pdf_reader = PdfReader(file)
#         num_pages = len(pdf_reader.pages)
#
#         # 遍历每一页
#         for page_num in range(num_pages):
#             page = pdf_reader.pages[page_num]
#             text = page.extract_text()
#
#             # 分词
#             words = word_tokenize(text)
#
#             # 词性标注
#             tagged_words = pos_tag(words)
#
#             # 提取英文单词和短语
#             english_words_phrases = [word for word, pos in tagged_words if re.match(r'^[A-Za-z]+$', word)]
#
#             # 打印英文单词和短语
#             print(f"Page {page_num + 1}:")
#             print(english_words_phrases)
#             print()
#
# # 指定PDF文件路径
# pdf_file = 'file.pdf'
#
# # 调用函数进行读取和打印
# read_pdf_extract_english_words_and_phrases(pdf_file)
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from PyPDF2 import PdfReader

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def read_pdf_extract_english_words_and_phrases(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()

            words = word_tokenize(text)
            tagged_words = pos_tag(words)

            english_words_phrases = []
            consecutive_chars = set(["or", "I", "E", "L", "T", "S"])  # 连续的字符集合

            for word, pos in tagged_words:
                if re.match(r'^[A-Za-z]+$', word) and word not in consecutive_chars:
                    english_words_phrases.append(word)

            print(f"Page {page_num + 1}:")
            print('\n'.join(english_words_phrases))
            print()

pdf_file = 'file.pdf'
read_pdf_extract_english_words_and_phrases(pdf_file)
