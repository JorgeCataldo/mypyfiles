# -*- coding: utf-8 -*-
"""
Created on Tue May 10 11:51:24 2016

@author: Jorge Cataldo
"""


print(2+3)

A=[1,2,4,8,10]
print(A)

for i in range(3, 20, 2):
    print(i)
    print("We're on time %d" %(i))
    
#for x in range(3):
#    print (x)
#else:
#    print ('Final x = %d' % (x))
    
#string = "Hello World"
#for x in string:
#    print (x)
    
#print((",,,").format(x))

with open("nomes.txt", "r") as nomes :
    n = list()
    for x in nomes:
        n.append(x)
#        print(x)
    
    for x in n[::-1]:
        print(x)
        
    
    