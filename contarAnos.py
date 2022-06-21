# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:00:48 2022

@author: Gabri
"""

from collections import Counter
import matplotlib.pyplot as plt



#abre o arquivo contendo as informações dos artigos
arquivo = open(r'C:\Users\Gabri\Desktop\Codigos bolsa\todos_curriculos.txt','r', encoding="utf8")

#divide o arquivo em linhas individuais
linhas = arquivo.readlines()

#variável para armazenar os títulos únicos dos artigos
titulos_ja_analisados = []

#variável para armazenar os anos dos artigos
anos = []

#passa por todas as linhas do arquivo
for i in range(0, len(linhas)-1):
    
    #armazenando a string da linha em uma variável
    linha = linhas[i]
    #limpando a string da linha para não haver nenhum \t ou \n
    linha = linha.rstrip().lstrip()
    
    
    if "Titulo do artigo:" in linha:
        #se fora linha que contém o título do artigo entra aqui
         
        if linha not in titulos_ja_analisados:
            #se não passamos ainda por esse título
            
            #insere o título na variável criada mais cedo
            titulos_ja_analisados.append(linha)
            
            #variável que armazena a próxima linha
            proxima_linha = linhas[i+1]
            
            #armazena na variável ano o ano desse arigo, limpando a string e retirando "Ano do artigo: "
            ano = proxima_linha.replace("Ano do artigo: ", "").rstrip().lstrip()
            
            #insere o ano do artigo na variável criada mais cedo
            anos.append(ano)
        

#passa os valores da variável anos (do tipo lista) para a variável ocorrencias, que é um Counter(dicionário que conta as ocorrências)
ocorrencias = Counter(anos)

#organiza o dicinário para mostrar os anos em ordem crescente
ocorrencias = dict(sorted(ocorrencias.items(), key=lambda item: item[0]))


#gera e mostra no pyplot um gráfico de barras das ocorrências de artigos por ano

plt.text(6, 16.5, "Relação artigos por ano")
plt.xticks(rotation=90)
plt.bar(ocorrencias.keys(), ocorrencias.values(), 0.9)
plt.savefig('grafico.png',transparent=True, dpi=300)
plt.show()


print(ocorrencias)