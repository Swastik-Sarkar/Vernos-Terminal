#Vernos Terminal 0.0.1


from graphlib import CycleError
import sys
import os
import subprocess
import json
import random
import time
import socket
import json
from colorama import *
import gc


os.system("clear")
print(Fore.LIGHTGREEN_EX + "[+] Loading dxi..." + Fore.WHITE)
print(Fore.MAGENTA + "[+] Loaded!" + Fore.WHITE)
print(Fore.YELLOW + "[/] Ignored Spellings Errors" + Fore.WHITE)
print(Fore.RED + "[-] Null" + Fore.WHITE)
print(Fore.BLUE + "Run ID : 0z02943-0f_Vernos0.0.1 " + Fore.WHITE)


cred=Fore.RED
cblue=Fore.BLUE
cgreen=Fore.GREEN
cyellow=Fore.YELLOW
cmg=Fore.MAGENTA
cpink=Fore.LIGHTMAGENTA_EX
cwhite=Fore.WHITE
caqua=Fore.LIGHTBLUE_EX


path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
dv = 1
dvv = 2
print(cred + "\n\n\n\nV" + cblue + "e" + cgreen + "r" + cred + "n" + cblue + "o" + cgreen + "s" + cmg + " Terminal" + cyellow +" v0.0.1 Stable " + cwhite + "\n")
while True:
	code = input(cyellow + "usr" + Fore.CYAN + "$ " + cwhite)
	if code == 'ip':
		print("IP: " + host_ip)
		print("Machine Name is " + host_name)	
	if code == 'cls':
		print(cred + 'This text is red in color' + cwhite)
	if code == 'pip install':
		os.system("pip install" + input(""))
	if code == 'color red':
		print(cred + "colour of the text is changed to red")
	if code == 'color red':
		print(cblue + "colour of the text is changed to blue")
	if code == 'color green':
		print(cgreen + "colour of the text is changed to green")
	if code == 'color yellow':
		print(cyellow + "colour of the text is changed to ryellow")
	if code == 'color magenta':
		print(cmg + "colour of the text is changed to magenta")
	if code == 'color white':
		print(cwhite + "colour of the text is changed to white")
	if code == 'exit':
		os.system("exit")
	else: 
		print(cred + "This is not a command , Type 'Help' If You Need Command List" + cwhite)
