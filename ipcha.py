import requests
import os
import time

def read_ips(*remote_urls):
    ips = []
    for remote_url in remote_urls:
        try:
            response = requests.get(remote_url)
            response.raise_for_status()
            ips.extend(response.text.splitlines())
        except Exception as e:
            print(f"Error fetching IPs: {e}")
    return ips

def get_geolocation_and_save(ips):
    url = "http://ip-api.com/batch"
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Python/Requests'
    }
    
    batch_size = 100  # 每批最多100个IP
    for i in range(0, len(ips), batch_size):
        batch_ips = ips[i:i+batch_size]
        try:
            response = requests.post(url, json=batch_ips, headers=headers)
            if response.status_code == 200:
                process_response(response.json())
            else:
                print(f"Batch {i//batch_size} failed: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Request error: {e}")
        time.sleep(4)  # 控制请求频率

def process_response(results):
    if os.path.exists('jg.txt'):
        os.remove('jg.txt')
    if os.path.exists('jgb.txt'):
        os.remove('jgb.txt')
    
    with open('jg.txt', 'a') as f_jg, open('jgb.txt', 'a') as f_jgb:
        for item in results:
            if item.get('status') == 'success':
                line = f"{item['query']}#{item['countryCode']}"
                f_jg.write(line + '\n')
                f_jgb.write(item['query'] + '\n')
                print(line)
            else:
                print(f"Failed IP: {item.get('query', 'Unknown')} - {item.get('message')}")

def main():
    remote_urls = [
        'https://raw.githubusercontent.com/wokaotianshi123/cf-clean-ips/main/ip.txt'
    ]
    ips = read_ips(*remote_urls)
    if ips:
        get_geolocation_and_save(ips)

if __name__ == "__main__":
    main()
