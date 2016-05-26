# -*- coding: utf-8 -*-
"""
Created on Wed May 18 17:49:58 2016

@author: Jorge
"""

s='hit'
print(s[2])          ## Erro se o indexador cai fora 
print(len(s))        ## 3
print( s + ' there') ## hit there


pi = 3.14                                #não mistura var str com var float
##text = 'The value of pi is ' + pi      ## NO, does not work
text = 'The value of pi is '  + str(pi)  ## yes
print(text) 


# % operator
text = ("%d little pigs come out or I'll %s and %s and %s" 
       % (3, 'huff', 'puff', 'blow down'))
print(text)                                  ## 