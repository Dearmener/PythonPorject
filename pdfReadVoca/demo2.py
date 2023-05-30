import PyPDF2
import nltk
import re

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.chunk import RegexpParser

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def read_pdf_extract_english_words_and_phrases(pdf_file):
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page in range(num_pages):
            page_obj = pdf_reader.pages[page]
            text = page_obj.extract_text()

            # Remove Chinese characters
            text = re.sub(r'[\u4e00-\u9fff]+', '', text)

            # Tokenize sentences
            sentences = sent_tokenize(text)

            for sentence in sentences:
                # Tokenize words
                words = word_tokenize(sentence)

                # Remove stopwords and specific string
                words = [word.lower() for word in words if
                         word.isalpha() and word.lower() not in stopwords.words('english') and word.lower() != 'oliver' and word.lower() != '雅思托福工作室' and word.lower() != 'e' and word.lower() != 'l']

                # Part of speech tagging
                tagged_words = nltk.pos_tag(words)

                # Define a grammar for noun phrase chunking
                grammar = r"""
                    NP: {<DT|PP\$>?<JJ>*<NN.*>+}   # chunk determiner/possessive, adjectives and nouns
                        {<NNP>+}                # chunk sequences of proper nouns
                """

                # Create a chunk parser
                chunk_parser = RegexpParser(grammar)

                # Chunk the sentence
                tree = chunk_parser.parse(tagged_words)

                # Traverse the tree and extract noun phrases
                for subtree in tree.subtrees():
                    if subtree.label() == 'NP':
                        phrase = ' '.join(word for word, tag in subtree.leaves())
                        print(phrase)
                print("---")


if __name__ == '__main__':
    pdf_file = 'file.pdf'
    read_pdf_extract_english_words_and_phrases(pdf_file)
