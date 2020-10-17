#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 23:06:12 2020

@author: verasong
"""

user_input = "y"
while user_input == "y":
    user_number = int(input("How many numbers?"))
    for user_number in range (user_number):
        print(user_number)
    user_input = input('If you would like to continue playing, press "y". Otherwise, press "n".')
