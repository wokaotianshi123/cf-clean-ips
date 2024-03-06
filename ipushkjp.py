import re
import requests

# 指定网址列表
urls = [
    "https://raw.githubusercontent.com/wokaotianshi123/cfipyouxuan/main/resip/JP.txt",
    "https://raw.githubusercontent.com/wokaotianshi123/cfipyouxuan/main/resip/HK.txt",
    "https://raw.githubusercontent.com/wokaotianshi123/cfipyouxuan/main/resip/TW.txt",
    "https://raw.githubusercontent.com/wokaotianshi123/cfipyouxuan/main/resip/KR.txt",
    "https://raw.githubusercontent.com/wokaotianshi123/cfipyouxuan/main/resip/SG.txt",
    "https://raw.githubusercontent.com/wokaotianshi123/cfipyouxuan/main/resip/US.txt"
]

# 遍历每个网址
for url in urls:
    # 发送HTTP请求获取网页内容
    response = requests.get(url)

    # 提取网页内容中所有IP地址
    ip_pattern = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
    ip_list = re.findall(ip_pattern, response.text)

    # 根据文件名确定连接符
    filename = url.split("/")[-1]
    separator = "#" + filename.split(".")[0]

    # 用连接符连接IP地址,并在每行后添加换行符
    new_content = "\n".join([ip + separator for ip in ip_list])

    # 将结果写入新文件
    with open(filename, "w") as f:
        f.write(new_content + "\n")
