# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:30:56 2016

@author: Jorge

PYTHON VARIABLE 

"""
## Py não é fortemente tipada 
# O intepretador py reconhece o tipo da variável pela sintaxe
# Int -> = # ou int(#) 
# Float -> = #.## 
# String -> = '#' ou "#"
# Tuple -> = #,# ou = (#,#)
# List -> = [#,#]
# Dict -> = {'#': #, '#': #}

# Defaultdict -> 
# Tipo def pelo usuário - > com o método Namedtuple

from collections import namedtuple, defaultdict

# lists vs tuples
i1=0
i2=1.58
i3='str'

l1 = [3, 4, 5]
l2 = [i1, i2, i3]
l3 = [6, 7, l1]        #lista de listas

print('Operadores ->',l1,'+',l2,"-",l3)

l1[0]=333               #listas suportam 'item assignment' 
print(l1)

l1[3]=444               #erro out of range! listas não admitem inserção 
print(l1)

l5=[l1,l2,l3]           #lista de listas
print(l5) 

t1 = (l1, l2, l3)       #Tuple de listas 
print(t1)

t1[0] = l3               #erro!!!! tuple não suporta item assignment 
print(t1)

# Dicionário ??
d = {'q': 1, 'y': 2}
print(d['y'])
print(d['c'])          #erro!!! retorna erro qd não encontra no dict 

d['c'] = 3
print(d)                #dict permite inserção de novos elementos 

dd = defaultdict(int)   # declaração diferente do dict normal
dd['q'] = 1
dd['y'] = 2
print(dd['c'])          #defaultdict retorna 0 qd não encontra 

#----------------------------------------------------------------
a = 3     # carrega var a, carrega instância 3, aponta a para 3  
a = "S"   # carrega instância "s", aponta a para "s" 
print(a)  

l1 = [0, 1, 2]
l2 = [3, 4, 5]
print(l1,l2)
l1 = l2            #aponta l1 para onde aponta l2 (*************)
print(l1,l2)
l1[0] = 6
print(l1,l2)       #
#----------------------------------------------------------------

# Tuple vs NamedTuple vs Classes

f = ("Fred", "Fluminense")
print(f[0])
print(f[1])


Jogador = namedtuple("varjogador", "Posição Time")   #define var tipo varjogador 
Fred = Jogador(Posição="Atacante", Time="Fluminense")      
print(Fred.Posição)
print(Fred.Time)
print(Fred)               


class Player:
    def __init__(self, position, team):
        self.position = position
        self.team = team
    
    def sayName(self):
        print(("My position is {0}").format(self.position))
        
Ozil = Player("Atacante", "Real Madrid")
print(Ozil.position)
print(Ozil.team)
print(Ozil)

Ozil.sayName()



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

mySwicth = { "a": f1, "b":f2, "c":f3 }
mySwicth["a"]()


