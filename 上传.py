# coding=gbk
import requests

url = 'http://localhost:5000/upload'
files = {'pdf': open('2.pdf', 'rb')}
response = requests.post(url, files=files)

# 直接打印文本而不是编码文本
print(response.text)
