# -*- coding: utf-8 -*-
"""intro_to_python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aE_L8xb8oR2WX5E2oe6n1gGPxX4o6YHr
"""

i = 1
print(i)

a: int = True

print(a)

str_001 = 'aasdad asdasda'
str_002 = "adasdad adadasd adasdas adasdasdasda  asdasd"

valor_verdade = True
valor_falso = False

valor_null = None

ponto_flutuante = .1

j = 0

while j < 10:
  print(j)
  j = j + 1

j = -1

while j < 10:

  j = j + 1

  if j == 1:
    continue

  print(j)

minha_lista = [1, 2, 3, 4, 4, 4, 4, 4]

minha_lista

meu_conjunto_001 = {1, 2, 3, 4, 4, 4, 4, 4, 1, 1, 1, 2, 2, 2, 2}
meu_conjunto_002 = {1, 5, 7}

meu_conjunto_001.union(meu_conjunto_002)

len(minha_lista)

len(meu_conjunto_001)

meu_conjunto_001.isdisjoint({1, 7, 8})

[1, 2, 3, 4] + [4, 5, 6]

lista = [1, 2, 3, 4]
lista

lista.remove(1)
lista

lista.index(3)

lista[-1]

lista[0:-1]

lista[1:-1]

tupla = (1, 2, 3)
type(tupla)

tupla_001 = (1,)
type(tupla_001), tupla_001

meu_mapa = {
    'chave': 'valor',
    1: True,
    False: 99
}

meu_mapa

False == 0

meu_mapa['chave']

meu_mapa[0]

meu_mapa.keys()

meu_mapa.values()

meu_mapa.items()

valores = [9, 5, 32]

for v in valores:
  print(v)

for t in meu_mapa.items():
  print(t)

for k, v in meu_mapa.items():
  print(k)
  print(v)
  print('=========================')

{1, 2, 3, 4}

{1: 1, 'a': 3}

[1, 2, 3, 4, 5]

for i in iterable:
  print(i)

json = {
    's': 1,
    'list': []
}

class Pessoa:

  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

p = Pessoa('K', 29)

json_p = {
    'nome': 'K',
    'idade': 29
}

class NomeDaClasse(object):

  def __init__(self, atributo_1, atributo_2):
    self.atributo_1 = atributo_1
    self.atributo_2 = atributo_2


class Casa:
  pass

class Pessoa(object):
  
  def __init__(self, casa: Casa):
    self.casa: Casa = casa


class PessoaFisica(Pessoa):
  def __init__(self, casa: Casa):
    self.casa: Casa = casa

pe = PessoaFisica()

isinstance(pe, Pessoa)

def funcao(a):
  return a + a

type(funcao)

def funcao(a):
  return a + a

def funcao_os(fn, a):
  return fn(a + 10)

funcao_os(lambda x: x / 2, 2)

type(lambda x: x / 2)

import requests

# URL -> GET, POST, DELETE, PATCH, PUT
response = requests.get("https://pokeapi.co/api/v2/pokemon/1")

response.json()['name']

a = 1
b = 2

print(a, b)

tmp = a
a = b
b = tmp

print(a, b)

a, b = 3, 4

print(a, b)

a, b = b, a
print(a, b)

def f1(p1, p2, p3):
  return p1 + p2 - p3

mapa = {
    'p1': 1,
    'p2': 2,
    'p3': -3
}

# **mapa == p1=1, p2=2

f1(**mapa) # f1(p1=1, p2=2)

lista = [2, 1]

f1(*lista) # f1(1, 2)

def fx(*l):
  for i in l:
    print(i)

fx(*lista)

def fx2(**kargs):
  for k, v in kargs.items():
    print(k, '=', v)

mapa2 = {
    'meup1': 1, 
    'k': 'a', 
    'w': 'b', 
    'j': 10,
    'Claudio': '10 na cabeça'
}

fx2(**mapa2) # meup1=1, k=a, w=b, j=10, Claudio=10 na cabeça

import requests

def get_pokemon_names_from_ids(*ids):

  result = []

  for _id in ids:
    url = 'https://pokeapi.co/api/v2/pokemon/' + str(_id)
    response = requests.get(url)
    r = response.json()

    abilities = [s['ability']['name'] for s in r['abilities']]

    name = r['name']
    weight = response.json()['weight']
    result.append((name, abilities))

  return result

get_pokemon_names_from_ids(1, 2, 3, 4)

def my_super_python_function(*ids):
  return [requests.get('https://pokeapi.co/api/v2/pokemon/{}'.format(_id)).json()['name'] for _id in ids if _id > 2]

lista = my_super_python_function(1, 2, 3, 4, 5)

for i in lista:
  if 'c' in i:
    print(i)
