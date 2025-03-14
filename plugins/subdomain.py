import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable


def site_site138(domain):
    domain_list = []
    headers = {
        "Cookie": "__gads=ID=341ce4d90ad15de9:T=1727342274:RT=1727342274:S=ALNI_MYyituak7mQVy6rswygYoyMCqBFeA; __gpi=UID=00000f1e9b049d99:T=1727342274:RT=1727342274:S=ALNI_MZgsPtW0u85I_zJsm30TXyW4WD2ag; __eoi=ID=32b768449d90dbfc:T=1727342274:RT=1727342274:S=AA-AfjaZV1U_VQk4HXhhosSZCFuP; Hm_lvt_6915b6622e4edeaddff40e931334c732=1727342051,1729512851,1729730903; Hm_lvt_aac43b0aec3a1123494f170e0aec4778=1731323025; HMACCOUNT=D9442D93D50467BB; Hm_lvt_ecdd6f3afaa488ece3938bcdbb89e8da=1731323263; Hm_lpvt_ecdd6f3afaa488ece3938bcdbb89e8da=1731323263; HMACCOUNT=D9442D93D50467BB; PHPSESSID=tf9nmnfdgeivisl1pm6vllu1v6; tfstk=fGR-T3XsRmmo274YHJMcx0bd0L0mmBLrq38_tMjudnKvSeJl-e9kRs_CP9OlZUxAdhxNVHLEzwsBAHIHExcMzU5FOcfKsfYzHS6sG3F5AsgC7N2W_-TSXU5FOm0SdOtDzh_Ljy0ROqCf-Nz5OMwSkt_Pc7_QNwZjki7COJ_7FS_f7Ne7VH1IkEsVRvUuyM45vWpHI_7M9v4g9WdAkDSyy-VhkCQReGT5hWNQ5aBRfUsxbA09btTFpBzU9gTWQH76VuiGUe9vDaCKi816kptOuQGg2ZJklFjXWyPeP_p96_9-0-5k2I1XNdUQOECR49QA3unAfQ8X_s6m1VLXg3YyMe4IOZxGcUR59fgNw_s5MZRn07sphpOlU6rSjT8BHnQR1g7vsCLJtljO-8gxkJyFFZumPCXiSVTzKZIio-2ULtbVkG0xkJyFFZ7Ajqc0LJWcu; BAIDU_SSP_lcr=https://cn.bing.com/; Hm_lpvt_aac43b0aec3a1123494f170e0aec4778=1731337977",
        "Sec-Ch-Ua": '"Chromium";v="130", "Microsoft Edge";v="130", "Not?A_Brand";v="99"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://site.ip138.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Priority": "u=0, i",
        "Connection": "close"
    }

    #子域名：
    urldomain = f"https://site.ip138.com/{domain}/domain.htm"
    responsedomain = requests.get(urldomain, headers=headers)
    if responsedomain.status_code == 200:
        soup = BeautifulSoup(responsedomain.text, 'html.parser')
        domain_section = soup.find(id='J_subdomain')
        #print(domain_section)
        if domain_section:
            tabledomain = PrettyTable(['序号','子域名'])
            domain = domain_section.find_all('p')
            with open('srcTargrt.txt','w') as file:
                for i in domain:
                    domain_list.append(i.text.strip())
                    file.write(i.text.strip()+'\n')
                    #print(i.text.strip())
        return domain_list



