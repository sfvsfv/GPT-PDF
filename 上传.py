# coding=gbk
import requests

url = 'http://localhost:5000/upload'
files = {'pdf': open('2.pdf', 'rb')}
response = requests.post(url, files=files)

# ֱ�Ӵ�ӡ�ı������Ǳ����ı�
print(response.text)
