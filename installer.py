#THE AUTHOR OF THIS  SCRIPT IS DARK DEVIL
#PLEASE GIVE CREDITS IF U WANT TO COPY
# JOIN ~ @I_am_Prediction_King_Bot FOR MORE 
#IMPORT
import os
from colorama import init, Fore
from time import sleep
import csv
import time
import random
import os
import pickle
import sys
import time,os,sys

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def typingInput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value  
  
def clearScreen():
  os.system("clear")

#COLORS
init()
n = Fore.RESET
lg = Fore.BLUE
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
gr = Fore.GREEN
colors = [lg, r, w, cy, ye, gr]

# REQUIREMENTS 
try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

# BANNER {LOGO} DARK DEVIL
def banner():
    import random

# REQUIREMENTS 
try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

# BANNER {LOGO} DARK DEVIL
def banner():
    import random

    b = [

'                    _ _      _   _              ',
'                    | (_)    | | (_)            ',
'  _ __  _ __ ___  __| |_  ___| |_ _  ___  _ __  ',
' |  _ \|  __/ _ \/ _  | |/ __| __| |/ _ \|  _ \ ',
' | |_) | | |  __/ (_| | | (__| |_| | (_) | | | |',
' | .__/|_|  \___|\__,_|_|\___|\__|_|\___/|_| |_|',
' | |                                            ',
' |_|   _                                        ',
' | |  (_)                                       ',
' | | ___ _ __   __ _                            ',
' | |/ / |  _ \ / _  |                           ',
' |   <| | | | | (_| |                           ',
' |_|\_\_|_| |_|\__, |                           ',
'                __/ |                           ',
'               |___/                            ',
 

                                                                                            


    ]
    for char in b:    
        print(f'{cy}{char}{n}{cy}')
    print(f'{r}   {r}')
    print(f'{r}  ?????????????     : {gr}?????????????????????????? ????????? {gr}')
    print(f'{r}  ????????       : {gr}@I_am_Prediction_King_Bot{gr}')
    print(f'{r}  ????????????????????????? : {gr}@deadsec0_0darky{gr}')
    print(f'{r}   {r}')

#typing text
typingPrint(" ?????????? ???????????????? ????????????????? ?????? ?????????????????????????? ????????? | ???????????????????? :@I_am_Prediction_King_Bot\n")
time.sleep(1)
typingPrint("?????????????   : ?????????????????????????? ?????????\n")
time.sleep(1)
typingPrint("????????????????????????? : @deadsec0_0darky\n")
time.sleep(1)
typingPrint("???????????????? ???????? ???????????? ???????? ????????????????\n")
time.sleep(1)






time.sleep(1)
clearScreen()



# FUNCTION CALLING 
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
while True:
    clr()
    banner()
    print(ye+'Choose an Option:'+n)
    print(cy+'            [1] ??????????????? ????????????????'+n)
    print(cy+'            [2] ???x?????'+n)
    a = int(input('\n Enter your choice: '))
    if a == 1:
    
       print("[+] Installing requierments ...")
       os.system('pip install telethon==1.24.0')
       os.system('pip install colorama==0.4.3')
       print("[+] setup complete !")
       print("[+] now you can run any tool !")
        
       input(f'\n Press enter to goto main menu...')
       
    if a == 2:
        clr()
        banner()
        exit()

 
