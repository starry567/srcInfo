import argparse
from pprint import pprint

from plugins.ipinfo import IP_info
from plugins.subdomain import site_site138
from plugins.title import start_title
from plugins.TideFingercms import Tide_cms


def script_info():
    print("author:  阿权")
    print("src")
    print('The tool is hoped to be helpful to everyone!!')

def start():
    script_info()
    parser = argparse.ArgumentParser(description="src tools")
    parser.add_argument('--scan', type=str, help='all information')
    parser.add_argument('--ipinfo', type=str, help='search ip information')
    parser.add_argument('--cms', type=str ,help='search cms')


    args = parser.parse_args()
    if args.scan:
        domain_list = site_site138(args.scan)
        print("subdomain save to srcTarget.txt")
        start_title(domain_list)
        print("information save to output.xlsx")
        #Tide_cms() in start_title()

    if args.ipinfo:
        information = IP_info(args.ipinfo)
        pprint(information)

    if args.cms:
        cms_list = Tide_cms(args.cms)
        print("".join(cms_list))


if __name__ == '__main__':
    start()




