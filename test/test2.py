from plugins.TideFingercms import Tide_cms


cms = Tide_cms("http://cyxy.wtu.edu.cn")

print(cms)
if cms == []:
    print("unknown")
else:
    print("".join(cms))
