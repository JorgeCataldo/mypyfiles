# -*- coding: utf-8 -*-
"""
Created on Mon May 16 18:06:05 2016

@author: Jorge

FUNCTIONS

"""

# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """
    result = s + s + s # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + '!!!'
    return result
    
def main():
    print(repeat('Yay', False))      ## YayYayYay
    print(repeat('Woo Hoo', True))   ## Woo HooWoo HooWoo Hoo!!!
    
main()


# Functions as Objects
a = 3
b = "string"
def fc():
    print(a, b)
   
c = fc
c()

Ozil.sayName = fc
Ozil.sayName()


# Dictionary as swicth
def f1():
    print("A")
def f2():
    print("B")
def f3():
    print("C")

f1()

a = f1                                   #a recebe a função f1    
a()                                      #chama a como uma função 

a = f1()                                 #???
a

mySwicth = { "a": f1, "b":f2, "c":f3 }
mySwicth["a"]()
