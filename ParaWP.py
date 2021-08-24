import requests
import time
from colorama import init, Fore
init(convert=True)
print(Fore.RED + ' ██▓███   ▄▄▄       ██▀███  ▄▄▄      ███▄    █ ▒█████   ██▀███   ███▄ ▄███▓ ▄▄▄       ██▓    ')
time.sleep(0.2)
print(Fore.RED + '▓██░  ██▒▒████▄    ▓██ ▒ ██▒████▄    ██ ▀█   █▒██▒  ██▒▓██ ▒ ██▒▓██▒▀█▀ ██▒▒████▄    ▓██▒    ')
time.sleep(0.2)
print(Fore.RED + '▓██░ ██▓▒▒██  ▀█▄  ▓██ ░▄█ ▒██  ▀█▄ ▓██  ▀█ ██▒██░  ██▒▓██ ░▄█ ▒▓██    ▓██░▒██  ▀█▄  ▒██░    ')
time.sleep(0.2)
print(Fore.RED + '▒██▄█▓▒ ▒░██▄▄▄▄██ ▒██▀▀█▄ ░██▄▄▄▄██▓██▒  ▐▌██▒██   ██░▒██▀▀█▄  ▒██    ▒██ ░██▄▄▄▄██ ▒██░    ')
time.sleep(0.2)
print(Fore.RED + '▒██▒ ░  ░ ▓█   ▓██▒░██▓ ▒██▒▓█   ▓██▒██░   ▓██░ ████▓▒░░██▓ ▒██▒▒██▒   ░██▒ ▓█   ▓██▒░██████▒')
time.sleep(0.2)
print(Fore.RED + '▒▓▒░ ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░▒▒   ▓▒█░ ▒░   ▒ ▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░▓  ░')
time.sleep(0.2)
print(Fore.RED + '░▒ ░       ▒   ▒▒ ░  ░▒ ░ ▒░ ▒   ▒▒ ░ ░░   ░ ▒░ ░ ▒ ▒░   ░▒ ░ ▒░░  ░      ░  ▒   ▒▒ ░░ ░ ▒  ░')
time.sleep(0.2)
print(Fore.RED + '░░         ░   ▒     ░░   ░  ░   ▒     ░   ░ ░░ ░ ░ ▒    ░░   ░ ░      ░     ░   ▒     ░ ░   ')
time.sleep(0.2)
print(Fore.RED + '               ░  ░   ░          ░  ░        ░    ░ ░     ░            ░         ░  ░    ░  ░')
time.sleep(0.2)
print('============================================================================================== ')

def wpcheck():

    urls = input("Enter file urls : ")
    dir = '/wp-json/wp/v2/'
    with open(urls, 'r') as links:
        for row in links:
            url = row.strip()
            row = row.strip() + dir
            try:
                req = requests.get(row)
                data = req.json()
                db = data['namespace']
                if db == 'wp/v2':
                    print(Fore.GREEN + url , ' ==> WordPress')
                    live = open('WordPress.txt', 'a')
                    live.write(url + '\n')
            except:
                    print(Fore.YELLOW + url , ' ==> Not WordPress')
                    live = open('NotWordPress.txt', 'a')
                    live.write(url + '\n')
wpcheck()
