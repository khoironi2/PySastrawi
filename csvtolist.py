# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:40:14 2019

@author: who
"""
import csv

with open('output.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)

print(your_list)