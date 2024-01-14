import http.client
import json
import requests
# import time

# 开始计时
# start_time = time.time()

# 获取PDF文本
url = 'http://localhost:5000/upload'
files = {'pdf': open('3.pdf', 'rb')}
response = requests.post(url, files=files)
long_text = response.text  # 从接口获得的长文本


# print(long_text)

# 分段函数
def split_text(text, max_size):
    for start in range(0, len(text), max_size):
        yield text[start:start + max_size]


# 配置GPT API   api.zhangsan.cloud
conn = http.client.HTTPSConnection("api.zhangsan.cloud")
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer sk-zkyXXXXXXXXXXXXXXXaA47c77',
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
}

# 准备发送到GPT API的消息
all_responses = []

# 系统提示，加入到第一个消息段
system_prompt = "请总结本篇论文,并详细告诉我论文中是基于什么背景.例如：用到了什么方法/算法，是怎么解决的，得到了什么结果，一步步详细告诉我，reply in chinese."

for i, segment in enumerate(split_text(long_text, 8000)):
    if i == 0:
        # 第一个段落，添加系统提示
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": segment}
        ]
    else:
        messages = [
            {"role": "user", "content": segment}
        ]

    payload = json.dumps({
        "model": "gpt-3.5-turbo-16k-0613",
        "messages": messages
    })

    conn.request("POST", "/v1/chat/completions", payload, headers)
    res = conn.getresponse()
    data = res.read()
    all_responses.append(json.loads(data.decode("utf-8")))

# 打印或处理所有的响应
for response in all_responses:
    content = response["choices"][0]["message"]["content"]
    print(content)


# print('\n\n')
# # 结束计时并输出运行时间
# end_time = time.time()
# print("Flask API 请求运行时间: {:.2f}秒".format(end_time - start_time))
