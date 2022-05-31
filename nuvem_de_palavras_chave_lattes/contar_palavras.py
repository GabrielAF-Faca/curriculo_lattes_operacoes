# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:00:48 2022

@author: Gabri
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

def pode_inserir(palavra):
    palavras_proibidas = "da,de,com,das,do,pelo,em,of,the,an,of,and,for,in,from,on,with,por,como,by,or,para,não,as,pós,um"
    palavras_proibidas = palavras_proibidas.split(",")
    
    if len(palavra) < 2:
        return False
    
    if "&#" in palavra:
        return False
    
    if palavra in palavras_proibidas:
        return False
    
    return True



palavras_titulo = []


arquivo = open(r'C:\Users\Gabri\Desktop\Codigos bolsa\todos_curriculos.txt','r', encoding="utf8")
linhas = arquivo.readlines()

for linha in linhas:
    linha = linha.rstrip().lstrip()
    
    if "Titulo do artigo:" in linha:
        
        linha = linha.replace(".", "")
        
        split_linha = linha.split(": ")
         
        titulo = split_linha[1].lower()
        
        
        titulo = titulo.replace(":", " ")
        titulo = titulo.replace("<scp>", "").replace("</scp>","")
        
   
        if len(split_linha) > 2:
            titulo = titulo + " " + split_linha[2]
        
        elementos_titulo = titulo.split(" ")
        
        for palavra in elementos_titulo:
            if "," in palavra and not "2,3,7,8":
                palavra = palavra.replace(",", " ")
                
            if pode_inserir(palavra.lower()):
                palavras_titulo.append(palavra.rstrip().lstrip())
    
            



ocorrencias = Counter(palavras_titulo)

ocorrencias = dict(sorted(ocorrencias.items(), key=lambda item: item[1]))
#ocorrencias = dict(ocorrencias)
print(ocorrencias)