# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:00:48 2022

@author: Gabri
"""

from collections import Counter


palavras_titulo = []


arquivo = open(r'C:\Users\Gabri\Desktop\Codigos bolsa\lattes_leitor_xml\saidas\todos_curriculos.txt','r')
linhas = arquivo.readlines()


for linha in linhas:
    linha = linha.rstrip().lstrip()
    
    if "Titulo do artigo:" in linha:
        
        linha = linha.replace(".", "")
        
        split_linha = linha.split(": ")
         
        titulo = split_linha[1].lower()
        
        
        titulo = titulo.replace(":", " ")
        titulo = titulo.replace("<scp>", "").replace("</scp>","")
        
        palavras_unicas = []

        for palavra in titulo.split(" "):
            if palavra not in palavras_unicas:
                print(palavra + " nao esta nas utilizadas")                
                palavras_unicas.append(palavra)
            else:
                print("\n" + palavra + " esta nas utilizadas\n")
        
        for palavras in palavras_unicas:
            if len(palavras) > 1:
                palavras_titulo.append(palavras)

        

            
            
ocorrencias = Counter(palavras_titulo)
ocorrencias = dict(sorted(ocorrencias.items(), key=lambda item: item[1]))
print(ocorrencias)


conta_palavras = 0

for elementos in ocorrencias:
    conta_palavras += ocorrencias[elementos]

print(conta_palavras)


