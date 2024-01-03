# coding=gbk
# pip install pypdf2 --upgrade

import PyPDF2

# 打开PDF文件
with open('2.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)

    # 获取PDF的总页数
    num_pages = len(reader.pages)

    # 逐页读取
    for page in range(num_pages):
        page_obj = reader.pages[page]
        print(page_obj.extract_text())
