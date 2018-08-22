#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import urllib.request,os
os.system('clear')
print("\u001b[32m")
print("            ___ __   ______ ____ ____ __  ____  __")
print("           / __|\ \ / /| _ )|__ (| _ \| \/ |\ \/ /")
print("           | (__ \ V / | _ \ |_ \| / ||\/| | >  <")
print("           \___|  |_|  |___/|___/|_|_\|_||_|/_/\_\___")
print("\u001b[33m")
print('         《"""""""""""""""""""""""""""""""""""""""""""》')
print("         《    CYB3RMX_ PROGRAMMING & CYBERSECURITY   》")
print("         《       ~~~~~MX Security Corporation~~~~~   》")
print("         《             SOURCE CODE DRAINER           》")
print('         《___________________________________________》')
print("//////////////////////////")
print("[1] SOURCE CODE DRAIN")
print("[154] UPDATE SOURCE CODE DRAINER")
option = int(input("CHOOSE AN OPTION"))
if option == 1:
  req=urllib.request.urlopen(target)
  print(req.read())
  print("//////////////////////////")
  ret = int(input("RETURN BACK [1/0] ?: "))
  if ret == 1:
    os.system('clear')
    os.system('python sourcedrainer.py')
  elif ret == 0:
    print("\u001b[31m[!] PROGRAM IS SHUTTING DOWN...")
    os.system('clear')
  else:
    print("\u001b[31m[!] YOU SELECTED WRONG OPTION!!")
elif option == 154:
   print("\u001b[32m[*] UPDATING SOURCE DRAINER...")
   os.system('git clone https://github.com/CYB3RMX/Source-Code-Drainer')
   print("[*] UPDATE COMPLETED...")
   os.system('python sourcedrainer.py')
else:
   print("\u001b[31m[!] YOU SELECTED WRONG OPTION...")