import sys
import random
import time
import tkinter as Tk
import os
import pygame
pygame.mixer.init()
track = pygame.mixer.music.load(r"Pimp.ogg")
pygame.mixer.music.play()
os.system('cls')
def Logal():
    print('''
        GGGGGGGGGGGGG                                                                               
     GGG::::::::::::G                                                                               
   GG:::::::::::::::G                                                                               
  G:::::GGGGGGGG::::G                                                                               
 G:::::G       GGGGGG  aaaaaaaaaaaaa      mmmmmmm    mmmmmmm       eeeeeeeeeeee        ssssssssss   
G:::::G                a::::::::::::a   mm:::::::m  m:::::::mm   ee::::::::::::ee    ss::::::::::s  
G:::::G                aaaaaaaaa:::::a m::::::::::mm::::::::::m e::::::eeeee:::::eess:::::::::::::s 
G:::::G    GGGGGGGGGG           a::::a m::::::::::::::::::::::me::::::e     e:::::es::::::ssss:::::s
G:::::G    G::::::::G    aaaaaaa:::::a m:::::mmm::::::mmm:::::me:::::::eeeee::::::e s:::::s  ssssss 
G:::::G    GGGGG::::G  aa::::::::::::a m::::m   m::::m   m::::me:::::::::::::::::e    s::::::s      
G:::::G        G::::G a::::aaaa::::::a m::::m   m::::m   m::::me::::::eeeeeeeeeee        s::::::s   
 G:::::G       G::::Ga::::a    a:::::a m::::m   m::::m   m::::me:::::::e           ssssss   s:::::s 
  G:::::GGGGGGGG::::Ga::::a    a:::::a m::::m   m::::m   m::::me::::::::e          s:::::ssss::::::s
   GG:::::::::::::::Ga:::::aaaa::::::a m::::m   m::::m   m::::m e::::::::eeeeeeee  s::::::::::::::s 
     GGG::::::GGG:::G a::::::::::aa:::am::::m   m::::m   m::::m  ee:::::::::::::e   s:::::::::::ss  
        GGGGGG   GGGG  aaaaaaaaaa  aaaammmmmm   mmmmmm   mmmmmm    eeeeeeeeeeeeee    sssssssssss  
    ''')
def AI():
    os.system('cls')
    a="Hello"
    b="Who are you?"
    c="What is your name?"
    d="Open Game website"
    e="I'm sad"
    f="Exit"
    g="Get out!"
    h="Fuck you!"
    i="Shutdown my computer"
    j="Say \"Hello,I'm your AI-Pet\""
    k="Output A"
    l=":("
    m=";)"
    n="By!Say \"By~\""
    o="Start notepad"
    p="Start cmd"
    q="Start Facebook"
    r="Color green"
    s="Color red"
    t="Recover color"
    u="My IP"
    v="My system's info"
    w="Stop music"
    x="Start music"
    y="How old are you?"
    z="Your download website"
    print('''
   _____  .___         __________        __   
  /  _  \ |   |        \______   \ _____/  |_ 
 /  /_\  \|   |  ______ |     ___// __ \   __\
/    |    \   | /_____/ |    |   \  ___/|  |  
\____|__  /___|         |____|    \___  >__|  
        \/                            \/
    ''')
    print("Contents to be able to input:")
    print("Hello")
    print("Who are you?")
    print("What is your name?")
    print("Open Game website")
    print("I'm sad")
    print("Get out!")
    print("Fuck you!")
    print("Shutdown my computer")
    print("Say \"Hello,I'm your AI-Pet\"")
    print("Output A")
    print(":(")
    print(";)")
    print("By!Say \"By~\"")
    print("Start notepad")
    print("Start cmd")
    print("Start Facebook")
    print("Color green")
    print("Color red")
    print("Recover color")
    print("My IP")
    print("My system's info")
    print("Stop music")
    print("Start music")
    print("How old are you?")
    print("Your download website")
    print("Exit")
    print(" ")
    print('\033[1;33;44mYou say\033[0m')
    while True:
        In2=input('You say:')
        if In2==a:
            print("Hi,I'm good.  :)")
            time.sleep(3)
        elif In2==b:
            print("I im your AI-Pet")
            time.sleep(3)
        elif In2==c:
            print("\033[0;36;40mMy name...\033[0m")
            print("You say!")
            In3=input('My name:')
            print("My name is ")
            print(In3)
            print("Thank you!")
            time.sleep(3)
        elif In2==d:
            print("OK")
            os.system('start https://ccw.site/')
        elif In2==e:
            print("You can relax by listening to songs, playing games, or seeking help from a mental health teacher")
            time.sleep(3)
        elif In2==f:
            print("Byby...")
            sys.exit(0)
        elif In2==g:
            print(":( What?")
            time.sleep(1)
            print("OK")
            sys.exit(0)
        elif In2==h:
            print("***")
            print("Fuck you too!")
            time.sleep(3)
        elif In2==i:
            print("Oh...")
            sleep(1)
            print("OK")
            os.system('shutdown /s /t 00')
        elif In2==j:
            print("Hello,I'm your AI-Pet")
            time.sleep(3)
        elif In2==k:
            print("A")
            time.sleep(3)
        elif In2==l:
            print(":(")
            time.sleep(3)
        elif In2==m:
            print(";)")
            time.sleep(3)
        elif In2==n:
            print("By~")
            time.sleep(3)
        elif In2==o:
            print("OK")
            time.sleep(1)
            print("Starting notepad...")
            time.sleep(1)
            os.system('start notepad')
            time.sleep(3)
        elif In2==p:
            print("OK")
            time.sleep(1)
            print("Starting cmd...")
            time.sleep(1)
            os.system('start cmd')
            time.sleep(3)
        elif In2==q:
            print("Starting https://facebook.com...")
            time.sleep(1)
            os.system('start https://facebook.com')
            time.sleep(3)
        elif In2==r:
            print("OK")
            time.sleep(1)
            os.system('color 0a')
        elif In2==s:
            print("Red...OK!")
            time.sleep(0.8)
            os.system('color 04')
            time.sleep(3)
        elif In2==t:
            os.system('color 07')
            time.sleep(3)
        elif In2==u:
            print("Get IP...")
            time.sleep(1)
            os.system('ipconfig > C:\IP.txt')
            print("IP is in C:\IP.txt")
            time.sleep(3)
        elif In2==v:
            print("Get system's info...")
            time.sleep(1)
            os.system('systeminfo > C:\Systeminfo.txt')
            print("System's info is in C:\Systeminfo.txt")
            time.sleep(3)
        elif In2==w:
            print("Stoping music...")
            pygame.mixer.music.stop()
            time.sleep(3)
        elif In2==x:
            print("Starting music...")
            pygame.mixer.init()
            pygame.mixer.music.load('Pimp.ogg')
            pygame.mixer.music.play()
            time.sleep(3)
        elif In2==y:
            print("I'm ten years old")
            time.sleep(3)
        elif In2==z:
            print("Sorry, I haven't downloaded the website yet. You can recommend me to everyone in a USB stick")
            time.sleep(3)
        else:
            print("\033[0;31;40mError\033[0m")
            print("Not Found this string!")
            time.sleep(3)
            
def GameMain():
    '''Game's main'''
    print("One is an arithmetic game, and tow are AI")
    In=input('1、Arithmetic game\n2、AI Pets (Incomplete)\nGame >')
    if In=='1':
        t=0
        os.system('cls')
        print('Arithmetic game!')
        #  +
        for i in range(10000):
            time.sleep(2)
            a=random.randint(1,100)
            b=random.randint(1,100)
            print(a,end="")
            print("+",end="")
            print(b,end="")
            print("=",end="\n")
            In2=input(':')
            if int(In2)==a+b:
                print("Good!  :D")
                t=t+1
            else:
                print("No!It's ",end="")
                print(a+b,end="\n")
                print(" ")
        #  *
        for i in range(100):
            time.sleep(2)
            a=random.randint(1,100)
            b=random.randint(1,100)
            print(a,end="")
            print("*",end="")
            print(b,end="")
            print("=",end="\n")
            In2=input(':')
            if int(In2)==a*b:
                print("Good!  :D")
                t=t+1
            else:
                print("No!It's ",end="")
                print(a*b,end="\n")
                print(" ")
        print("Stop.")
        if t==10100:
            print("Your Arithmetic is Good!100!")
        else:
            print("Oh...",end="")
            print(t,end="\n")
        time.sleep(2)
        os.system('cls')
        print("[*] Stoping Game...")
        sleep(2)
        sys.exit(0)
    else:
        if In=='2':
            AI()
def Loading():
    print("[*] Seting Options...")
    time.sleep(3)
    print("[*] Loading...")
    time.sleep(3)
    print("[!] No User!")
    time.sleep(1)
    print("[+] Starting Login Window...")
    print("Default Username: Gamer197, Default Password: 123456")

#main
Logal()
Loading()

from tkinter import *

# 设置登录窗口
win = Tk()
win.title('Login')
win.geometry('300x150')
win.resizable(0, 0)
# 设置账号
Label(text='User:').place(x=50, y=30)
uname = Entry(win)
uname.place(x=100, y=30)
# 设置密码
Label(text='Password:').place(x=20, y=70)
pwd = Entry(win,show="*")
pwd.place(x=100, y=70)
# 登陆
def login():
    username = uname.get()
    password = pwd.get()
    if username == 'Gamer197' and password == '123456':
        print('[+] Landing successful!   :)')
        win.destroy()
    else:
        print('The account or password is incorrect.')
        print('Please rejoin the game.')
        win.destroy()
        sys.exit(0)
# 登陆按钮
Button(text='Login', command=login).place(x=100, y=110)
win.mainloop()
time.sleep(2)
print('[+] Starting Game...')
time.sleep(2)
GameMain()
