#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 14:58:05 2020

@author: verasong
"""

#  create lists to store data
month = []
net_value = []

#  open csv file as reader, skip header
import os
import csv

budget_data_path = '/Users/verasong/Python-Challenge/Case Assignment/PyBank/Resources/PyBank_budget_data.csv'

with open(budget_data_path, 'r') as csv_reader:
     csv_reader = csv.reader(csv_reader, delimiter=",")
     headers = next(csv_reader, None)

# Calcuate total number of months and net total amount     
     for row in csv_reader:
         new_month = row[0]
         month.append(new_month)
         
         new_value = row[1]
         net_value.append(int(new_value))

     total_month = len(month)
     total_net = sum(net_value)
     
# Calcuate the average in change in "Profit/Losses" 
     average_total = total_net / total_month        
     
# Calcuate the greatest increase in Profits
     maximum_value = max(net_value)
     minimum_value = min(net_value)

# Zip two lists into dictionary
# Search for the months for greatest increase and greatest decrease
     dictionary = dict(zip(month, net_value))
     for key1, value1 in dictionary.items():
         if value1 == maximum_value:
             maximum_month = key1
     for key2, value2 in dictionary.items():
         if value2 == minimum_value:
             minimum_month = key2

# Print analysis
print("Finacial Analysis\n-------------------\n")
print(f"Total Months: {total_month}\n")
print(f'Tota: ${total_net}\n')
print(f"Average Change: ${average_total}\n")
print(f"Greatest Increase in Profits: {maximum_month} (${maximum_value})\n")
print(f"Greatest Decrease in Profits: {minimum_month} (${minimum_value})\n")

# export text file with budget analysis
text_path = '/Users/verasong/Python-Challenge/Case Assignment/PyBank/Resources/PyBank_budget_analysis.txt'
with open(text_path, "w") as textfile:
    textfile.write("Finacial Analysis\n-------------------\n")
    textfile.write(f"Total Months: {total_month}\n")
    textfile.write(f'Tota: ${total_net}\n')
    textfile.write(f"Average Change: ${average_total}\n")
    textfile.write(f"Greatest Increase in Profits: {maximum_month} (${maximum_value})\n")
    textfile.write(f"Greatest Decrease in Profits: {minimum_month} (${minimum_value})\n")
    