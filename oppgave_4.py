#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n_input = int(input("Hva er n? "))
if n_input < 0:
    print("Error")
elif n_input == 0:
    print("0! = 1 ")
    

else:
    n = n_input

    for x in range(1,n_input):
        n *= x
    
    

    print(n_input,"! =",n)