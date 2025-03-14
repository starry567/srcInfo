from plugins.TideFingercms import extract_info

s = '''
[21:27:44] [INFO] Start InfoScan
[21:27:48] [+] [TCP/HTTP] [200] [jQuery][JAVA] http://cyxy.wtu.edu.cn [创新创业学院]
[21:27:48] [+] 已完成 1/1
[21:27:48] [+] 扫描结束,耗时: 6.937933418s'''

print(extract_info(s))