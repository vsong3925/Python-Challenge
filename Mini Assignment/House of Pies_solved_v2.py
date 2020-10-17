#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 08:45:47 2020

@author: verasong
"""

print("Welcome to the House of Pies! Here are our pies: \
      ------------------------------------------------")

pie_list = ["Not Pie", "Pecan","Apple Crisp","Bean","Banoffee","Black Bun","Blueberry","Buko","Burek","Tamale","Steak"]

for index, pie in enumerate(pie_list):
    print("({}) {}".format(index +1, pie))
    
user_order = int(input("Which pie would you like to order? Type the number."))

pie_cart1 = []
pie_cart1.append(pie_list[user_order])

print(f"Great! We'll have that {pie_cart1} right out for you.")

response = input("Would you like to make another order?")

response = "Yes"
while response.lower() == "yes":
    more_order = int(input("Which pie would you like to order?"))
    response = input("Would you like to make another order?")
    pie_cart1.append(pie_list[more_order])

print(f"You have ordered {len(pie_cart1)} pies.")