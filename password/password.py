# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 18:12:43 2022

@author: user
"""

x = 5
while x < 10:
    print('x <10')
    print('x is still < 10')
    x = x + 1
    print('x =', str(x))
    print('-----------')
print('exit while loop')

while True:
    mode = input('please key in mode: ') #input context is string by default
    if mode == 'q':
      break
    elif mode == '1':
      print('mode 1')
    elif mode == '2':
      print('mode 2')
    else:
      print('only 1/2/q is allowed')
      
password = 'a123456'
N = 8 #test time
i = N
while i >= 1:
    InputPD = input('please key in password: ')
    if InputPD == password:
      print('log in succesfully')
      #i = N+1
      break
    #elif InputPD != password:
    else:
     i = i-1
     print('your password is incorrect, there is', i,'more chances')

  
  
    