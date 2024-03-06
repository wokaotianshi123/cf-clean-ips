import os
import requests
from bs4 import BeautifulSoup

# 删除原有的cs.txt文件(如果存在)
if os.path.exists("cs.txt"):
    os.remove("cs.txt")

# 发送GET请求获取网页内容
url = "https://stock.hostmonit.com/CloudFlareYes"
response = requests.get(url)
html_content = response.content

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html_content, "html.parser")

# 找到数据表格
table = soup.find("table", {"class": "table"})

# 初始化列表存储IP和Colo值
ip_list = []
colo_list = []

# 遍历表格行
if table:
    rows = table.find_all("tr")
    for row in rows:
        columns = row.find_all("td")
        if len(columns) >= 2:
            ip = columns[0].text.strip()
            colo = columns[1].text.strip()
            ip_list.append(ip)
            colo_list.append(colo)

# 将IP和Colo值用#连接
content = [f"{ip}#{colo}" for ip, colo in zip(ip_list, colo_list)]

# 将结果写入cs.txt文件
with open("cs.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(content))
