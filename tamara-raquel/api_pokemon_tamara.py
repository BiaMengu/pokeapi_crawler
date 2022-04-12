# -*- coding: utf-8 -*-
"""API-POKEMON-TAMARA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14a1HZ1r2Z1N08rz0dMxuu0D3JxjZubGA

INSTITUTO FEDERAL DE EDUCAÇÃO, CIÊNCIA E TECNOLOGIA DE SÃO PAULO <br>
TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS <br>
GSOI5 - GERENCIAMENTO DE SISTEMAS OPERACIONAIS SERVIDORES <br>
PROF. LUCAS VENEZIAN <br>
JC3009025 - TAMARA RAQUEL DA SILVA

Desenvolva um código em Python, utilizando o paradigma orientado a objetos, que recupere os dados básicos de um Pokemon a partir das APIs disponíveis no repositório https://pokeapi.co/.
<br>
Consulte a documentação para identificar os atributos. É necessário ao menos considerar 4 atributos da raiz do payload da API.
"""

import requests

def main():
  #criar uma variável global para receber o input de qual pokemon buscar
  global pokemon
  pokemon = str(input('Informe o pokemon pelo seu nome: '))
  api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
  resp = requests.get(api)
  poke = resp.json() #retorna o dicionário
  busca_especie(poke)
  busca_peso(poke)
  busca_itens(poke)
  busca_habilidades(poke)

if __name__ == '__main__':
  main()

#função para recuperar as habilidades do pokemon
#a api retorna uma lista pois pode ter mais de uma habilidade
def busca_habilidades(poke):
  print(f'Habilidades de {pokemon}')
  for habilidade in poke['abilities']:
    print(habilidade['ability']['name'])

#função para recuperar os itens possuídos do pokemon
#a api retorna uma lista pois pode ter mais de um item
def busca_itens(poke):
  print(f'Itens de {pokemon}')
  for item in poke['held_items']:
    print(item['item']['name'])

#função para recuperar a espécie do pokemon
def busca_especie(poke):
  print(f'Espécie de {pokemon}')
  print(poke['species']['name'])

#função para recuperar o peso do pokemon
def busca_peso(poke):
  print(f'Peso de {pokemon}')
  print(poke['weight'])