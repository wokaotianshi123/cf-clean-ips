import requests
from bs4 import BeautifulSoup

# 发送GET请求获取网页内容
url = "https://stock.hostmonit.com/CloudFlareYes"
response = requests.get(url)
html_content = response.content

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html_content, "html.parser")

# 找到IP和Colo列表
ip_list = []
colo_list = []

# 遍历表格数据
for tr in soup.find_all("tr"):
    tds = tr.find_all("td")
    if len(tds) >= 2:
        ip = tds[0].text.strip()
        colo = tds[1].text.strip()
        ip_list.append(ip)
        colo_list.append(colo)

# 将IP和Colo值用#连接
content = [f"{ip}#{colo}" for ip, colo in zip(ip_list, colo_list)]

# 将结果写入cs.txt文件
with open("cs.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(content))
