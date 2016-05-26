# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:30:56 2016

@author: Jorge

PYTHON VARIABLES

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

a=2          # carrega var a, carrega instância 3, aponta a para 3  
b=3
print(a+b)
a="S"        # carrega instância "s", aponta a para "s" 
print(a)  
print(a+b)   #Erro!!!

l1 = [0, 1, 2]
l2 = [3, 4, 5]
print(l1,l2)
l1 = l2            #aponta l1 para onde aponta l2 (*************)
print(l1,l2)
l1[0] = 6
print(l1,l2)       #

#----------------------------------------------------------------

i1=0
i2=1.58
i3='str'

l1 = [3, 4, 5]
l2 = [i1, i2, i3]
l3 = [6, 7, l1]        #lista de listas

print('Operadores ->',l1,'+',l2,"-",l3)


t1 = (l1, l2, l3)       #Tuple de listas 
print(t1)

t1[0]=333               #tuple não suporta item assignment Erro!!!! 
print(t1)

l1[0]=333               #listas suportam 'item assignment' 
print(l1)

l1[3]=444               #erro!! listas não admitem inserção 
print(l1)

l5=[l1,l2,l3]           #lista de listas
print(l5) 


l1 = [3, 4, 5]
d = {'pi': 3.14, 'cs': 'casa', 'lst' : l1}
print(d['lst'])         #printa a definição de... 

print(d['c'])           #erro!!! qd não encontra no dict uma def.

d['c'] = 3              #dict permite inserção
print(d)                 

dd = defaultdict(int)   # declaração diferente do dict normal
dd['q'] = 1
dd['y'] = 2
print(dd['c'])          #defaultdict retorna 0 qd não encontra def no dic


#----------------------------------------------------------------

# Tuple vs NamedTuple vs Classes

jog=("Atacante", "Fluminense")                    #var tipo tupla
print(jog[0])
print(jog[1])

from collections import namedtuple
Jogador=namedtuple("varjogador", "Posição Time")  #define var tipo 'varjogador' 
Fred = Jogador(Posição="Atacante", Time="Fluminense")      
print(Fred.Posição)
print(Fred.Time)
print(Fred)               

class Player:                                     #cria uma classe
    def __init__(self, position, team):
        self.position = position
        self.team = team
    
    def sayName(self):
        print(("My position is {0}").format(self.position))
        
Ozil = Player("Meia", "Real Madrid")
print(Ozil.position)
print(Ozil.team)
#print(Ozil)                                    #não é uma variável?!

Ozil.sayName()



