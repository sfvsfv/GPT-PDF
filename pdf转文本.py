# coding=gbk
# pip install pypdf2 --upgrade

import PyPDF2

# ��PDF�ļ�
with open('2.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)

    # ��ȡPDF����ҳ��
    num_pages = len(reader.pages)

    # ��ҳ��ȡ
    for page in range(num_pages):
        page_obj = reader.pages[page]
        print(page_obj.extract_text())
