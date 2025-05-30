import requests
from bs4 import BeautifulSoup
import os

# 目标网址
base_url = 'https://www.airandspaceforces.com/?s=B-21'

# 定义一个用于保存文件的目录
save_directory = 'saved_pages'
if not os.path.exists(save_directory):
    os.makedirs(save_directory)


# 发送HTTP GET请求获取初始页面
response = requests.get(base_url)

# 检查请求是否成功
if response.status_code == 200:
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有的<h3 class="post-title">标签
    h3_tags = soup.find_all('h3', class_='post-title')

    # 遍历每个<h3>标签，并找到其中的<a>标签
    for index, h3 in enumerate(h3_tags):
        a_tag = h3.find('a')  # 查找<h3>内的<a>标签
        if a_tag:
            # 提取<a>标签的href属性和文本内容
            link_url = a_tag['href']
            link_title = a_tag.get_text(strip=True)  # 获取<a>标签的文本内容

            # 如果是相对链接，则需要将其转换为绝对链接
            if not link_url.startswith('http'):
                link_url = requests.compat.urljoin(base_url, link_url)

                # 发送新的HTTP GET请求以获取链接页面的内容
            link_response = requests.get(link_url)

            # 检查新链接的请求是否成功
            if link_response.status_code == 200:
                # 使用BeautifulSoup解析链接页面的HTML
                link_soup = BeautifulSoup(link_response.text, 'html.parser')

                # 查找所有<p>标签
                p_tags = link_soup.find_all('p')

                # 提取<p>标签的内容
                p_contents = [p.get_text(strip=True) for p in p_tags]

                # 生成文件名，使用<a>标签的文本内容和索引来避免文件名冲突
                file_name = f"{hash(link_url)}-{index}.txt"
                file_path = os.path.join(save_directory, file_name)

                # 将页面内容（即所有<p>标签的内容）写入文件
                with open(file_path, 'w', encoding='utf-8') as file:
                    for content in p_contents:
                        file.write(content + '\n')  # 每个段落后添加换行符

                print(f"链接: {link_url} 的<p>标签内容已保存到文件 {file_path}")
            else:
                print(f"无法获取链接 {link_url} 的内容，状态码: {link_response.status_code}")
else:
    print('请求初始页面失败，状态码：', response.status_code)