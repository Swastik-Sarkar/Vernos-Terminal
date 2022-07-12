import sys
import os
import subprocess
import json
import random
import time

path = 'C:/'
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
print("Vernos Terminal v0.1 Stable ")
while True:
	code = input("$ ")
	if code == 'ip':
		print("IP: " + host_ip)
		print("Machine Name is " + host_name)
