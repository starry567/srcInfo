from prettytable import PrettyTable

from config import apikey_cms
import requests

def cms(domain):
    api_url = f"https://whatcms.org/API/Tech?key={apikey_cms}&url={domain}"
    print(api_url)
    response = requests.get(api_url)
    #print(response.text)
    # 检查响应状态码是否为 200 (OK)
    if response.status_code == 200:
        data = response.json()
        if data['results'] != []:
            tech_table = PrettyTable()
            tech_table.field_names = ["技术名称", "版本", "类别", "更多信息"]
            # 提取技术栈数据并添加到表格中
            cms_output=[]
            for tech in data['results']:
                tech_table.add_row([
                    tech['name'],
                    tech['version'] if tech['version'] else 'N/A',
                    ', '.join(tech['categories']),
                    f"https:{tech['url']}"  # 拼接完整的 URL
                ])
                cms_output.append(
                        (tech.get('name', 'N/A') or '') +
                        (tech.get('version', 'N/A') or '') +
                        "," +
                        (', '.join(tech.get('categories', [])) if tech.get('categories') else 'N/A')
                )

                #cms_output = tech['name']+tech['version']+","+"".join(tech['categories'])
                #print(cms_output)
            i=1
            for o in cms_output:
                print(str(i)+","+"".join(o))
                i=i+1

            # 打印技术栈表格
            print("技术栈信息:")
            print(tech_table)
        else:
            print("未识别到cms信息")
        if data['meta'] != []:
            # 创建 PrettyTable 对象来存储社交媒体数据
            social_table = PrettyTable()
            # 设置列名
            social_table.field_names = ["社交网络", "URL", "个人资料"]
            # 提取社交媒体数据并添加到表格中
            cms_social = []
            for social in data['meta']['social']:
                social_table.add_row([
                    social['network'],
                    social['url'],
                    social['profile']
                ])
                cms_social.append (
                        (social.get('network', 'N/A') or '') +
                        (social.get('url', 'N/A') or '') +
                        (social.get('profile', 'N/A') or '')
                )
                #print(cms_social)
            i=1
            for s in cms_social:
                print(str(i)+":"+"".join(s))

            # 打印社交媒体表格
            print("\n社交媒体信息:")
            print(social_table)
        else:
            print("未识别到社交信息")
    else:
        print(f"请求失败，状态码：{response.status_code}")

if __name__ == '__main__':
    cms("www.tibetpolicy.net")


"""
技术栈信息:
+-----------+--------+----------------------+---------------------------------+
|  技术名称 |  版本  |         类别         |             更多信息            |
+-----------+--------+----------------------+---------------------------------+
| WordPress | 6.1.1  |      Blog, CMS       | https://whatcms.org/c/WordPress |
|    PHP    | 7.3.33 | Programming Language |    https://whatcms.org/c/PHP    |
|   MySQL   |  N/A   |       Database       |   https://whatcms.org/c/MySQL   |
+-----------+--------+----------------------+---------------------------------+
未识别到社交信息
"""

