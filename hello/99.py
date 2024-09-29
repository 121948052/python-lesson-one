'''
Author: Bug Router
Date: 2024-09-27 11:10:49
Description: Default
'''
# -*- coding: UTF-8 -*-
 
# Filename : test.py
# author by : www.runoob.com
 
# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()