#!/usr/bin/env python3
# -*- coding: utf-8 -*-
b_g = int(input("Hva er befolkningen nå? (B-nåværende) "))
p = int(input("Hva er prosent? "))
t = int(input("Hva er tiden? " ))

for x in range (1,t+1):
    b_ny = b_g*(1-(p/100))
    b_g = b_ny
    print("Befolkningen etter",x,"år er",int(b_ny))
    

