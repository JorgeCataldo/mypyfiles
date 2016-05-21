# -*- coding: utf-8 -*-
"""
Created on Wed May 11 19:17:57 2016

@author: Jorge
"""

# git, continuous integration/delivery, tdd, orm



from collections import namedtuple, defaultdict
from sqlalchemy import create_engine
conn = "mysql+pymysql://inf2290:^inf2290$@mysql.mosconi.eti.br/cartola"
engine = create_engine(conn)

#for row in engine.execute('select * from atleta_2015'):
#    atleta = dict(row)
#    print(atleta["nome_txt"])

#atletas = []
#for row in engine.execute('select * from atleta_2015'):
#    atletas.append(Atleta(Id=row[0], Nome=row[2]))
#    
#clubes = []
#for row in engine.execute('select * from clube'):
#    clubes.append(Clube(Id=row[0], Nome=row[1]))

Atleta = namedtuple("Atleta", "Id Nome")
Clube = namedtuple("Clube", "Id Nome")

atletas = defaultdict(Atleta)
for row in engine.execute('select * from atleta_2015'):
    atletas[row[0]] = Atleta(row[0], row[2])
    
clubes = defaultdict(Clube)
for row in engine.execute('select * from clube'):
    clubes[row[0]] = Clube(row[0], row[1])
    
movAtleta = defaultdict(list)
for row in engine.execute('select * from atleta_rodada_2015'):
    movAtleta[atletas[row[1]]].append(clubes[row[3]])
    
#with open("atletas.csv", "w") as f:
#    for id_atleta, atleta in atletas.items():
#        line = atleta.Nome + ";"
#        for clube in movAtleta[atleta]:
#            line += clube.Nome + ";"
#        line += "\n"
#        f.write(line)

class ItemScout:
    def __init__(self, id, nome, desc, valor):
        self.id = id
        self.nome = nome
        self.desc = desc
        self.valor = valor
        
scoutItems = {}
for row in engine.execute('select * from item_scout'):
    scoutItems[row[0]] = ItemScout(row[0], row[1], row[2], row[4])
    
def CalcularPontos(jogador_id, rodada):
    total = 0
    query = 'select * from atleta_scout_2015 where atleta_id={0} and rodada_id={1}'
    for row in engine.execute(query.format(jogador_id, rodada)):
        total += scoutItems[row[3]].valor * int(row[4])
    return total
    
def HistoricoPontos(jogador_id):
    pontos = []
    query = 'select * from atleta_rodada_2015 where atleta_id={0} order by rodada_id'
    for row in engine.execute(query.format(jogador_id)):
        pontos.append(row[6])
    return pontos
    
def HistoricoPreco(jogador_id):
    precos = []
    query = 'select * from atleta_rodada_2015 where atleta_id={0} order by rodada_id'
    for row in engine.execute(query.format(jogador_id)):
        precos.append(row[7])
    return precos
    
import pylab
    
def Relatorio(jogador_id):
    pylab.legend(loc='upper right')
    pylab.plot(HistoricoPreco(jogador_id), '-b', label='preço')
    pylab.plot(HistoricoPontos(jogador_id), '-g', label='pontos')
    pylab.xlabel('Rodadas')
    pylab.ylabel('Preço/Pontos')
    pylab.title(("{0} - {1}").format(atletas[jogador_id].Id, atletas[jogador_id].Nome))
    
    
import random

random.seed(0)
print(random.random())
print(random.choice([1, 2, 3, 4, 5, 6]))
        
    
    

