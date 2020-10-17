#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:46:27 2020

@author: verasong
"""

user_input = "y"
while user_input == "y":
    user_number = int(input("How many numbers?"))
    for user_number in range (0, user_number+1):
        print(user_number)
    user_input = input('If you would like to continue playing, press "y". Otherwise, press "n".')
