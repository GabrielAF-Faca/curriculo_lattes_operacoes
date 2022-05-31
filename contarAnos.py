# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:00:48 2022

@author: Gabri
"""

from collections import Counter
import matplotlib.pyplot as plt

anos = []
palavras_chave = []
palavras_titulo = {}
curriculo = {}

arquivo = open(r'C:\Users\Lasimon\Desktop\Gabriel\Códigos\leitor xml lattes\lattes_leitor_xml\saidas\todos_curriculos.txt','r', encoding="utf8")
linhas = arquivo.readlines()

for linha in linhas:
    linha = linha.rstrip().lstrip()

    if linha.startswith("Ano do artigo:"):
        ano = linha.split(": ")[1]
        
        anos.append(ano)
        
                

ocorrencias = Counter(anos)

ocorrencias = dict(sorted(ocorrencias.items(), key=lambda item: item[0]))

#ocorrencias = sorted(ocorrencias.keys())

print(ocorrencias)
plt.xticks(rotation=90)
plt.bar(ocorrencias.keys(), ocorrencias.values(), 0.9)
plt.show()