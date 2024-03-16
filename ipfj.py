import os

# 定义文件夹名称
folder_name = 'ipfj'

# 确保文件夹存在
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# 读取jg.txt文件并处理
with open('jg.txt', 'r') as file:
    lines = file.readlines()

# 创建一个字典来存储国家代码和对应的文件名
country_files = {}

# 遍历每一行
for line in lines:
    # 分割IP地址和国家代码，strip()用于移除可能的空白字符，包括换行符
    ip, country_code = line.strip().split('#')
    country_code = country_code.strip()  # 移除换行符和可能的空格
 
# ... 接下来的代码
    # 确保国家代码文件名是唯一的
    if country_code not in country_files:
        # 创建文本文件，文件名以国家代码为名
        country_file_path = os.path.join(folder_name, country_code + '.txt')
        with open(country_file_path, 'w') as country_file:
            # 写入IP地址，每个IP地址占一行
            country_file.write(ip + '\n')
        country_files[country_code] = country_file_path

    # 如果国家代码已存在于字典中，则直接写入IP地址到对应的文件
    else:
        with open(country_files[country_code], 'a') as country_file:
            country_file.write(ip + '\n')
