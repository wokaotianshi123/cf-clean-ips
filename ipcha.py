import requests

# 从远程地址读取IP地址
def read_ips(*remote_urls):
    ips = []
    for remote_url in remote_urls:
        try:
            response = requests.get(remote_url)
            response.raise_for_status()  # 这将抛出一个HTTPError，如果HTTP请求返回了4xx或5xx响应
            ips.extend(response.text.splitlines())
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching IPs from {remote_url}: {e}")
    return ips

# 发送批量请求到IP-API.com并打印结果
def get_geolocation_and_print(ips):
    url = "http://ip-api.com/batch"
    # 构建请求数据
    payload = ips
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            results = response.json()
            for item in results:
                if 'query' in item and 'countryCode' in item:
                    output = f"{item['query']}#{item['countryCode']}"
                    print(output)
                    # 保存到文件
                    with open('jg.txt', 'a') as file:
                        file.write(output + '\n')
                else:
                    print(f"Incomplete data for IP: {item['query']}")
        else:
            print(f"Error: Received response with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while processing geolocation: {e}")

# 主函数
def main():
    # 远程地址列表
    remote_urls = [
        'https://gitjs.wokaotianshi123.cloudns.org/https://raw.githubusercontent.com/wokaotianshi123/cf-clean-ips/main/ip.txt',
        'https://gitjs.wokaotianshi123.cloudns.org/https://raw.githubusercontent.com/ymyuuu/IPDB/main/bestproxy.txt'
    ]
    # 读取IP地址
    ips = read_ips(*remote_urls)
    if ips:
        get_geolocation_and_print(ips)

if __name__ == "__main__":
    main()