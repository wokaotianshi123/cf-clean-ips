import os
import requests
from bs4 import BeautifulSoup

# 删除原有的ip.txt文件(如果存在)
if os.path.exists("ip.txt"):
    os.remove("ip.txt")

# 发送GET请求获取网页内容
url = "https://monitor.gacjie.cn/page/cloudflare/ipv4.html"
response = requests.get(url)
html_content = response.content

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html_content, "html.parser")

# 找到数据表格
table = soup.find("table", {"class": "table"})

# 初始化列表存储IP和Colo值
data = []

# 遍历表格行
if table:
    rows = table.find_all("tr")
    for row in rows:
        columns = row.find_all("td")
        if len(columns) >= 2:
            ip = columns[0].text.strip()
            colo = columns[1].text.strip()
            data.append(f"{ip}#{colo}")

# 将结果写入ip.txt文件
with open("ip.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(data))
