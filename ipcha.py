import requests

# 从远程地址读取IP地址
def read_ips(*remote_urls):
    ips = []
    for remote_url in remote_urls:
        try:
            response = requests.get(remote_url)
            response.raise_for_status()
            ips.extend(response.text.splitlines())
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching IPs from {remote_url}: {e}")
    return ips

# 发送批量请求到IP-API.com并打印结果
def get_geolocation_and_save(ips, file_with_hash, file_without_hash):
    url = "http://ip-api.com/batch" 
    payload = [{'query': ip} for ip in ips]  # 构建包含每个IP的列表
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            results = response.json()
            with open(file_with_hash, 'a') as file_with_hash_obj, open(file_without_hash, 'a') as file_without_hash_obj:
                for item in results:
                    if 'query' in item and 'countryCode' in item:
                        # 统一使用#分隔符
                        output_with_hash = f"{item['query']}#{item['countryCode']}"
                        file_with_hash_obj.write(output_with_hash + '\n')
                        print(output_with_hash)  # 打印带#的输出
                    else:
                        # 如果数据不完整，不保存到文件，只打印提示
                        print(f"Incomplete data for IP: {item['query']}")
        else:
            print(f"Error: Received response with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while processing geolocation: {e}")

# 主函数
def main():
    remote_urls = [
        'https://gitjs.wokaotianshi123.cloudns.org/https://raw.githubusercontent.com/wokaotianshi123/cf-clean-ips/main/ip.txt',
        'https://gitjs.wokaotianshi123.cloudns.org/https://raw.githubusercontent.com/ymyuuu/IPDB/main/bestproxy.txt'
    ]
    ips = read_ips(*remote_urls)
    if ips:
        get_geolocation_and_save(ips, 'jg.txt', 'jgb.txt')

if __name__ == "__main__":
    main()
