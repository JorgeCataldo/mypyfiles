# -*- coding: utf-8 -*-
"""
Created on Wed May 25 21:20:09 2016

@author: Jorge
"""

import modulo

print(modulo.a_do_modulo)


#--------------------------------------------------
def metodo_1(lista):
    assert(type(lista) == list)
    for item in lista:
        print(item)
        
metodo_1(5)                     # erro 
metodo_1([1, 2, 3])




#        players_position = filter(player -> has_position(player, position), players)

selectedPlayers = []
for player in players:
    if player.position == position:
        selectedPlayers.append(player)
        
# pesquisar Lambda Expressions (Python, Julia)
        
# Procura e entende a classe Player
# Procura e entende a classe Formations
# Procura e entende a classe Team
# todos em model.jl e traduz para python
        
def random_team(a, b):
    return a + b
    
assert(random_team(5, 4) == 9)


# Procura e entende a classe PlayerPrice
# em model.jl e traduz para python

def random_team(...):