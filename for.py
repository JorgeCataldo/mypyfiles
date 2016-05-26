# -*- coding: utf-8 -*-
"""
Created on Tue May 10 11:51:24 2016

@author: Jorge Cataldo

"""

for i in range(3, 20, 2):                 # de 3 a 19 a cada 2
    print(i)
    print("We're on time %d" %(i))
    
for x in range(20):                       # de 0 a 19 a cada 1
    print (x)
else:
    print ('Final x = %d' %(x))
    
string = "Hello World"             
for x in string:                          #for nos caracteres da string
    print (x)
    
print((",,,").format(x))                  # ???

list=[1,2,3,4,5,6]
for i in list[::-1]:                     #for na lista + de tras para frente
    print(i)   