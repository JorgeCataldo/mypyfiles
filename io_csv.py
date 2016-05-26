# -*- coding: utf-8 -*-
"""
Created on Wed May 11 19:17:57 2016

@author: Jorge
"""

from collections import namedtuple, defaultdict

DATA_PATH = "./data/"

#importação de txt 
with open(DATA_PATH + "nomes.txt", "r") as nomes:
    n = list()                              #cria uma lista n
    for i in nomes:                         #percorre as linhas de nomes.txt
        n.append(i)                         #adiciona à lista
        print(i)
    
    for x in n[::-1]:                      #pecorre lista na ordem inversa
        print(x)

#---------------------------------------------------------------------
#IMPORTA DE UMA BASE SQL

#carrega o método da biblioteca 
from sqlalchemy import create_engine

#conexão com banco de dados (url, login, senha)
conn = "mysql+pymysql://inf2290:^inf2290$@mysql.mosconi.eti.br/cartola"
engine = create_engine(conn)

#monta a string de busca sql 
atleta_sql='''
SELECT 
    at.atleta_id AS player,
    at.nome_txt AS name,
    at.apelido_txt AS nickname,
    at.preco_editorial_num AS price,
    at.foto_txt AS linkfoto
FROM 
    atleta_2015 AS at
ORDER BY 
    price ASC
'''

# importa dados para um dicionário
for row in engine.execute(atleta_sql):
    atleta = dict(row)                          # monta um dicinário 
    print(atleta['price'], atleta['nickname'])


# importa dados para uma tupla
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
    
    
#importa dados para uma lista
atletas = []
for row in engine.execute('select * from atleta_2015'):
    atletas.append(Atleta(Id=row[0], Nome=row[2]))
    
clubes = []
for row in engine.execute('select * from clube'):
    clubes.append(Clube(Id=row[0], Nome=row[1]))


#IMPORTA PARA CSV

#teste sintaxe. Duvida ***** !!!! pq qd abre excel pula linha
import csv
with open(DATA_PATH + "out4.csv", "w") as f:
    escreve_f = csv.writer(f)
    escreve_f.writerow(['name2', 'address2', 'phone2', 'etc2'])
    escreve_f.writerow(['bob', '2 main st', '703', 'yada'])
    escreve_f.writerow(['mary', '3 main st', '704', 'yada'])
    
# Dúvida *****!!!! pq de primeira não vai... somente leitura  
import csv
escreve_f = csv.writer(open(DATA_PATH + "out3.csv", 'w'))
escreve_f.writerow(['name', 'address', 'phone', 'etc'])
escreve_f.writerow(['bob', '2 main st', '703', 'yada'])
escreve_f.writerow(['mary', '3 main st', '704', 'yada'])


# dump para csv
with open(DATA_PATH + "atletas.csv", "w") as f:
    for id_atleta, atleta in atletas.items():
        line = atleta.Nome + ";"
        for clube in movAtleta[atleta]:
            line += clube.Nome + ";"
        line += "\n"
        f.write(line)


# com uso da classe 

class ItemScout:
    def __init__(self, id, nome, desc, valor):
        self.id = id
        self.nome = nome
        self.desc = desc
        self.valor = valor
        
scoutItems = {}                                          #dict
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
    

#---------------------------------------------------------------------

import pylab                                      #módulo de visualização
    
def Relatorio(jogador_id):
    pylab.legend(loc='upper right')
    pylab.plot(HistoricoPreco(jogador_id), '-b', label='preço')
    pylab.plot(HistoricoPontos(jogador_id), '-g', label='pontos')
    pylab.xlabel('Rodadas')
    pylab.ylabel('Preço/Pontos')
    pylab.title(("{0} - {1}").format(atletas[jogador_id].Id, atletas[jogador_id].Nome))
    
    
import random                                    #módulo randômico
random.seed(0)                                   #
print(random.random())
print(random.choice([1, 2, 3, 4, 5, 6]))
        
    
    
# git, continuous integration/delivery, tdd, orm
