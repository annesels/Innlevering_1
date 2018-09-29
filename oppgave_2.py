#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

a = input("Vil du finne (m), (v) eller (E)? " )
if a == "E":
    m = float(input("Hva er massen (m)? "))
    v = float(input("Hva er farten (v)? "))
    E =(m*v**2)/2
    print("Den kinetiske enegien til legemet er",E,"J")
elif a == "m":
    E = float(input("Hva er energien (E)? "))
    v = float(input("Hva er farten (v)? "))
    m = 2*E/v**2
    print("Massen til legemet ditt er",m,"kg")
elif a == "v":
    E = float(input("Hva er energien? "))
    m = float(input("Hva er massen?"))
    math.sqrt(v) = math.sqrt((2*E)/m)
    

