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

# 发送批量请求到IP-API.com并处理结果
def get_geolocation_and_save(ips):
    url = "http://ip-api.com/batch"
    payload = [{'query': ip} for ip in ips]
    headers = {
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            results = response.json()
            with open('jg.txt', 'a') as file_jg, open('jgb.txt', 'a') as file_jgb:
                for item in results:
                    if 'query' in item and 'countryCode' in item:
                        # 完整的IP#countrycode记录
                        output_jg = f"{item['query']}#{item['countryCode']}"
                        file_jg.write(output_jg + '\n')
                        # 仅IP地址的记录
                        output_jgb = f"{item['query']}"
                        file_jgb.write(output_jgb + '\n')
                        print(output_jg)  # 打印完整的IP#countrycode记录
                    elif 'query' in item:
                        # 仅IP地址的记录
                        output_jgb = f"{item['query']}"
                        file_jgb.write(output_jgb + '\n')
                        print(output_jgb)  # 打印仅IP地址的记录
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
        'https://raw.githubusercontent.com/wokaotianshi123/cf-clean-ips/main/ip.txt', 
        'https://raw.githubusercontent.com/ymyuuu/IPDB/main/bestproxy.txt' 
    ]
    # 读取IP地址
    ips = read_ips(*remote_urls)
    if ips:
        get_geolocation_and_save(ips)

if __name__ == "__main__":
    main()
