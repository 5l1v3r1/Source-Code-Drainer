#!/usr/bin/env python
#-*- coding: utf-8 -*-
import urllib.request
print("SOURCE DRAINER by CYB3RMX_")
print("//////////////////")
target=str(input("TARGET URL:"))
req=urllib.request.urlopen(target)
print(req.read())
print("//////////////////")