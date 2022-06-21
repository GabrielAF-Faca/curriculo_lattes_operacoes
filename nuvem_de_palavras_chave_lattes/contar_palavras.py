# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:00:48 2022

@author: Gabri
"""

from collections import Counter
from googletrans import Translator



translator = Translator()



def is_en(palavra):
    tradutor = translator.detect(palavra)
    
    lingua = tradutor.lang
    precisao = tradutor.confidence
    
    if lingua == "en" and precisao > 0.5:
        return True
    
    return False



def traduzir(palavra):
    
    return translator.translate(palavra, dest="pt").text
    
    
  
def pode_inserir(palavra):
    palavras_proibidas = "da,de,com,das,do,pelo,em,of,the,an,"
    palavras_proibidas+= "of,and,for,in,from,on,with,por,como,"
    palavras_proibidas+= "by,or,para,não,as,pós,um,numa,ao,via,"
    palavras_proibidas+= "nas,nos,na,no,use,non,a,to,uma,meio,"
    #palavras_proibidas+= ""
    
    palavras_proibidas = palavras_proibidas.split(",")
    
    if len(palavra) < 2:
        return False
    
    if "&#" in palavra:
        return False
    
    if palavra in palavras_proibidas:
        return False
    
    if palavra.isnumeric():
        return False
    
    return True



palavras_titulo = []

arquivo = open(r'C:\Users\Gabri\Desktop\Codigos bolsa\lattes_leitor_xml\saidas\todos_curriculos.txt','r')

linhas = arquivo.readlines()

quant_artigos = 0

titulos = []

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
        
        titulos.append(titulo)


    

titulos_traduzidos = []
'''
for titulo in titulos:
    if is_en(titulo):
        titulo = traduzir(titulo)
        
    titulos_traduzidos.append(titulo)
    print(quant_artigos*100/len(titulos))

print(titulos_traduzidos)
'''


titulos_traduzidos = ['interação não covalente de benzonitrila com nanotubos de carbono de parede simples', 'cálculos de primeiros princípios de radicais de alanina adsorvidos em nanotubos de carbono pristinos e funcionalizados', 'modelo de segregação de impurezas em nanofitas de grafeno', 'produção e divulgação de material instrucional sobre câncer de pele direcionado para a população de agudo   rs', 'modelagem computacional de co-exposição ambiental na sobrecarga de hidrocarbonetos derivados de petróleo usando proteína de transporte específica de substrato (todx) com nanoestruturas de grafeno', 'estudo ab initio de moléculas de so2 interagindo com fulerenos revestidos de metais de transição como uma possível rota para nanofiltros', 'ensino e aprendizagem de conceitos matemáticos relacionados à nanociência por meio da modelagem matemática', 'interação da hemoglobina com dióxido de enxofre e monóxido de carbono via simulação computacional', 'nanotubos de carbono dopados com metal interagindo com vitamina c', 'a adsorção de 17β estradiol em nanoestruturas de carbono', 'simulação de primeiros princípios de temozolamida interagindo com nanoestruturas', 'nanotubos de carbono interagindo com vitaminas cálculo de primeiros princípios', 'atividade neuroprotetora dos fulerenos uma revisão de literatura', 'adsorção física do fulereno com o 5 fluoruoracil um estudo teórico', 'Propriedades eletrônicas e estruturais de nanotubos de carbono dopados com silício', 'formação de nanoemulsões do tipo óleo em água contendo óleo de semente de romã', 'modelagem de nanobiossensor não intrusivo para detecção precoce do câncer de mama', 'analisando compensações de confiabilidade e desempenho de projetos baseados em hls em fpgas baseados em sram sob erros leves', 'modelo atomístico derivado de cálculos ab initio testado em potencial de interação benzeno benzeno', 'desenvolvimento de objetos de aprendizagem nas áreas de lingua portuguesa e matemática', 'as implicações da epistemologia de popper no ensino de ciências', 'clorofila a e feofitina a como sensores de gás de moléculas de co2 e o2', 'nanotubos de carbono funcionalizados com complexos de titânio para adsorção de cromo hexavalente uma abordagem ab initio', '1,2 diclorobenzeno interagindo com nanotubos de carbono', 'simulando o modelo orch or através de autômatos celulares quânticos', 'principais nanocarreadores utilizados em óleos essenciais com finalidade antioxidante uma revisão de literatura', 'interação de α</i> tocoferol com α</i> e β</i> ciclodextrinas uma investigação de primeiros princípios', 'ticl3 e ticl4 adsorvido em grafeno via modelagem molecular', 'estudo ab initio de um átomo de ferro interagindo com nanotubos de carbono de parede simples', 'conhecimento produzido em nanociência e a análise de internacionalização resultante da teoria das redes.', 'adsorção de nicotina em nanotubos de carbono de parede simples', 'vacinas contra covid 19 usando nanotecnologia uma revisão de literatura', 'interação da ciclodextrina com ácido acetilsalicílico um estudo de primeiros princípios', 'preparação, caracterização, atividade antimicrobiana e simulação computacional do  complexo de inclusão de sulfadiazina de prata com &#914; ciclodextrina', 'adsorção de bisfenol a e dibutil ftalato em óxido de grafeno um estudo ab inito', 'átomos de fe e mn interagindo com nanotubos de carbono', 'estudo ab initio de nanotubos de carbono de parede dupla sob pressão uniaxial', 'interação de nanotubos de carbono de parede simples (swcnt) e saxitoxina ab initio simulações e respostas biológicas na linhagem celular do hipocampo ht 22', 'fácil e rápida obtenção da celulose nanocristalina magnética', 'propriedades eletrônicas e magnéticas de cadeias de ferro em nanotubos de carbono', 'adsorção do fármaco nimesulida em nanoestruturas de carbono', 'propriedades energéticas e estruturais de átomos e moléculas adsorvidos em nanotubos de carbono dopados com silício', 'interação de nanotubos de carbono de parede simples e saxitoxina ab initio simulações e respostas biológicas na linhagem celular do hipocampo ht 22', 'nanomarcador para detecção precoce da doença de alzheimer combinando simulações ab initio dft e abordagem de docking molecular', 'cálculo ab initio para um material hipotético nanotubos de silício', 'história e iniciativas nacionais de pesquisa de nanotubos de carbono e grafeno no brasil', 'objetos de aprendizagem para o ensino de física custo do banho e código de cores', 'efeito de válvula de rotação aprimorado em nanotubos de carbono dopados magneticamente', 'comparando linguagens para representação de ontologias', 'estudo ab initio de uma molécula orgânica interagindo com um nanotubo de carbono dopado com silício', 'propriedades eletrônicas e magnéticas de ti e fe na superfície do grafeno', 'Investigação teórica da intercalação de lítio em nanotubos de carbono de parede simples', 'estudo teórico do ácido ascórbico com complexos c61(cooh)2', 'c59si na superfície do monohidreto si(100) h (2x1)', 'propriedades eletrônicas de parede única preenchida com ag e cro3', 'c61(cooh)2 interagindo com o antiviral ribavirina', 'a influência dos locais de concentração e adsorção de diferentes grupos químicos no grafeno através de simulações de primeiros princípios', 'objetos de aprendizagem no ensino de tópicos de eletrodinâmica', 'nanotubos de carbono carboxilados interagindo com moléculas de nimesulida efeitos de campos elétricos aplicados', 'adsorção de corantes orgânicos em grafeno um estudo ab initio', 'um olhar sobre a matemática no ensino integrado', 'interação de uma molécula de metanol com c60 sob pressão', 'um estudo ab initio de átomos de manganês e fios interagindo com nanotubos de carbono', 'nanotubos de carbono carboxilados sob campo elétrico externo uma investigação ab initio', 'nanotubos de carbono capeados e funcionalizados sob campos elétricos', 'membranas de nanocelulose bacteriana como potencial de curativos crônicos de feridas crônicas influência de meios de cultura alternativos no diâmetro de nanofibras uma breve revisão', 'adsorção de diclofenaco de sódio em grafeno um estudo experimental e teórico combinado', 'adsorção de 17 β estradiol em óxido de grafeno através do co-solvente metanol concorrente análise experimental e computacional', 'objetos de aprendizagem na educação infantil', 'ambiente de simulação para banco de dados de experimentos de nanopartículas poliméricas', 'estudo ab initio de nanotubos de carbono funcionalizados covalentemente', 'fundamentos de docking para simulação em nanociência', 'o uso de nanocarreadores no tratamento do câncer de cólon uma revisão de literatura', 'nanofiltro baseado em nanoestruturas de carbono funcionalizadas para adsorção de moléculas de pentaclorofenol', 'um estudo de primeiros princípios da interação da doxorrubicina com o grafeno', 'funcionalização de nanotubos de carbono de parede simples através da teoria e experimento de adsorção de clorofórmio', 'funcionalização de nanotubos de carbono', 'uma abordagem in silico dft para aplicações de nanotubos de carbono como nanopartículas direcionadas a mitos em doenças neurodegenerativas', 'interação de nanofitas de grafeno e siliceno armchair com bases de dna um estudo ab initio', 'modelagem computacional em interações de ligação de ciclodextrinas com a glicoproteína p de resistência a múltiplas drogas humana para aplicações eficientes de sistemas de entrega de drogas', 'estudo ab initio da deformação radial mais vacância em propriedades energéticas e eletrônicas de nanotubos de carbono', 'interação da &#946; ciclodextrina com diferentes metilxantinas', 'uma estratégia de extração nova e verde para determinação sensível de ftalatos em amostras aquosas estudos analíticos e computacionais', 'adsorção de corante reativo red m 2be de soluções aquosas por nanotubos de carbono de paredes múltiplas e carvão ativado', 'o ensino de tópicos de física clássica, em cursos presenciais, com o auxilio do moodle, numa perspectiva de incentivo a aprendizagem independente', 'influências de lipopolissacarídeos na toxicidade de nanotubos de carbono de paredes múltiplas oxidados para esplenócitos murinos in vitro</i>', 'simulações de primeiros princípios de mangiferina interagindo com beta ciclodextrina', 'espectroscopia raman de ressonância em nanotubos de carbono de parede dupla implantados com íons si e c', 'Primeiros Princípios Estudo de Campos Elétricos Transversais em Nanotubos de Carbono', 'estudo ab initio de nanotubos de carbono capeados dopados e dopados com si interagindo com moléculas de nimesulida', 'caracterização estrutural e química do revestimento protetor ti zro2 po4 3 para aplicações biomédicas', 'ciclodextrinas interagindo com metotrexato via modelagem molecular', 'adsorção de silício em nanotubos de carbono defeituosos um estudo de primeiros princípios', 'avaliação da atividade antimicrobiana do óleo de orégano livre e em nanoemulsões', 'propriedades estruturais e eletrônicas do fulerol funcionalizado com radiofármacos1', 'nanoestruturas de carbono interagindo com vitaminas a, b3 e c ab initio simulação', 'estudo teórico do no3 interagindo com nanotubos de carbono', 'simulações de primeiros princípios de moléculas de zidovudina (azt) interagindo com nanoestruturas de carbono', 'ia descrição e aplicação de regras de evasão no curso de  ciência da computação em ies', 'investigação de estabilidade e comportamento térmico de um hipotético nanotubo de silício', 'estudo de primeiros princípios da adsorção de 1,2 diclorobenzeno em nanotubos de carbono metálico', 'propriedades estruturais e eletrônicas do fulerol funcionalizado com radiofármacos', 'adsorção de corantes sintéticos laranja de acridina e azul de metileno e antraceno em nanotubos de carbono de parede simples uma abordagem de primeiro princípio', 'aprendizagem significativa com enfoque no desenvolvimento autônomo do estudante', 'propriedades eletrônicas de nanotubos de carbono de parede simples adsorvidos fecl3', 'influência da concentração e sítios de adsorção de diferentes grupos químicos no grafeno através de simulações de primeiros princípios', 'um estudo ab initio de grafeno carboxilado e fosforeno preto e azul', 'funcionalização de nanotubos de carbono por grupo carboxila sob deformação radial', 'adsorção de corante reativo azul 4 de soluções aquosas por experimento e teoria de nanotubos de carbono', 'desenvolvimento e avaliação de um objeto de aprendizagem sobre o custo do banho para ensino de física', 'nanopartículas lipídicas naturais contendo síntese de nimesulida, caracterização e atividades anti-inflamatórias e antinociceptivas in vivo', 'funcionalização de nanotubos de carbono de paredes simples com 6 aminofluoresceina', 'estudo ab initio da adsorção de dibenzo p dioxina 2,3,7,8 tetraclorada em nanotubos de carbono de parede simples', 'monômeros e fios de titânio adsorvidos em nanotubos de carbono um estudo de primeiros princípios', 'produção de nanotubos de carbono via técnica de deposição química de vapor', 'cálculos ab initio das propriedades estruturais e eletrônicas de cacu3ti4o12 sob alta pressão', 'ancoragem de radicais silanóis em nanotubos de carbono', 'gerenciamento e compatibilização de projetos simples aplicada em autocad', 'adsorção de metilfenidato em teoria e experimento de derivados de grafeno', 'dopagem substitucional em nanotubos de carbono deformados', 'modelagem de interações medicamentosas de azd1208 com vincristina e daunorrubicina em domínios tmd de ligação de extrusão de ligantes da glicoproteína p de resistência a múltiplas drogas (abcb1)', 'simulação ab initio de fulerenos puros e carboxilados interagindo com vitaminas', 'atividades biológicas do compósito 1,8 cineol associado a sistemas nanoestruturados uma breve revisão', 'modelagem matemática de perfis de liberação de fármacos a partir de nanocarreadores', 'um estudo ab initio de grafeno carboxilado e fosforeno preto e azul', 'nanoestruturas de carbono interagindo com vitaminas a, b3 e c ab initio simulações', 'glifosato adsorvido em nanotubos de carbono via modelagem molecular', 'estudo das propriedades estruturais e eletrônicas do nanotubo bc2n interagindo com antiinflamatórios', 'estudo de primeiros princípios de nanotubos de carbono revestidos de titânio como sensores para moléculas de monóxido de carbono', 'citoproteção do ácido lipóico contra a toxicidade induzida pela saxitoxina em linhagem celular hipocampal ht 22 através de modelagem in silico e ensaios in vitro', 'toxicidade de nanotubos de carbono associada a problemas do sistema respiratório uma revisão de literatura', 'encapsulamento de metalocenos em nanotubos de carbono de parede simples um estudo ab initio', 'interações de derivados de grafeno com neurotransmissor glutamato uma investigação paralela de docking de primeiros princípios', 'estudo teórico da interação de nanotubos de  carbono funcionalizados com aminoácidos', 'revisão de literatura de estudos teóricos de fosforeno e grafeno como sensor de gás para dióxido de carbono', 'síntese verde de nanopartículas inorgânicas como propostas terapêuticas para o câncer uma revisão', 'simulação ab initio de β12 borofeno funcionalizado', 'Abertura de gap induzida por doping químico e polarização de spin em grafeno', 'intercalação de lítio em feixes de nanotubos de carbono de parede única', 'nanoparticulas de plga carregadas com curcumina eficácia no tratamento do câncer de mama em modelos in vitro', 'adsorção de benzonitrila em nanotubos de carbono dopados com fe', 'adsorção de alaranjado de metila em titanatos nanoestruturados', 'ensino de nanociência e nanotecnologia perspectivas manifestadas por professores da educação básica e superior', 'Propriedades de transporte eletrônico de ácido ascórbico e nicotinamida adsorvidos em nanotubos de carbono de parede simples', 'nanoestruturas de selênio adsorvidas em nanotubos de carbono uma investigação dft', 'adsorção de nimesulida anti-inflamatória por materiais de grafeno um estudo teórico e experimental combinado', 'ensino e aprendizagem de conceitos matemáticos relacionados à nanociência por meio da  modelagem matemática', 'avanços recentes em equipamentos de proteção individual utilizando a nanotecnologia como escudo contra o sars cov 2', 'interação de nanofitas grafeno e siliceno armchair com bases de dna um estudo ab initio', 'adsorção de um corante têxtil a partir de soluções aquosas por nanotubos de carbono', 'pós de óxido de zinco nanoestruturados produzidos pelo método de síntese por combustão em solução utilizando glicina como combustível', 'módulo para mensuração do desempenho competitivo de nanomateriais aplicados ao setor cosmético', 'estudo teórico de funcionalização de nanotubos com grupo amida', 'visando interações medicamentosas de betabloqueador com proteína do plasma sanguíneo de fibrinogênio um estudo computacional e experimental', 'as nanotecnologias no ensino', 'propriedades eletrônicas e estruturais de nanotubos de carbono dopados com metais', 'estudo ab initio de sensores de nanotubos de carbono deformados para moléculas de monóxido de carbono', 'metodologia de análise de suscetibilidade a erros suaves de projetos hls em fpgas baseados em sram', 'adsorção do corante vermelho de alizarina por nanotubos de carbono uma investigação experimental e teórica', 'quercetina nanoencapsulada para o tratamento do câncer de fígado uma revisão de literatura', 'o ensino de nanociências por meio de objetos de aprendizagem', 'ligando o magnetismo em cálculos funcionais de densidade de grafeno dopado com ni', 'interações de nanotubos de carbono cheios de óxido de ferro com moléculas de gás', 'simulações ab initio de fosforeno preto e azul funcionalizado com grupos químicos para ancoragem de biomoléculas', 'funcionalização de nanotubos de carbono através da ligação química de átomos e moléculas', 'perfil de magnetização para impurezas em nanofitas de grafeno', 'cálculos ab initio do ácido ascórbico interagindo com o complexo c61(cooh)2 sob pressão', 'escaneamento computacional de mitoalvo baseado em vacâncias topológicas de nanotubos de carbono de parede simples com canal hvdac1 mitocondrial humano', 'análise das tendências globais e latino-americanas em nanotoxicologia com foco em nanomateriais de carbono uma abordagem cienciométrica', 'Influência da concentração e posição de grupos carboxila nas propriedades eletrônicas de nanotubos de carbono de parede simples', 'c61(cooh)2 interagindo com o antiviral ribavirina', 'desenvolvimento de um objeto de aprendizagem sobre a poluição global', 'adsorção de resveratrol em nanotubos de carbono um estudo de primeiros princípios', 'estudos de espalhamento raman e difração de raios X de cacu3ti4o12 policristalino sob alta pressão', 'pós de óxido zinco nanoestruturado produzidos pelo método de síntese por combustão em solução utilizando glicina como combustível', 'teoria funcional da densidade estudo da interação aromática π de dímeros isolados de benzeno, fenol, catecol, dopamina e adsorvidos na superfície do grafeno', 'preparação de monólitos de nanotubos de carbono por compactação a alta pressão', 'abordagem de nanociência no ensino médio', 'propriedades eletrônicas e estruturais de nanotubos de carbono e aplicação como carreadores de fármacos', 'estudo teórico da interação de nanotubos de carbono funcionalizados com aminoácidos', 'um estudo teórico e experimental dft sobre adsorção de tetraciclina em óxido de grafeno magnético', 'desenvolvimento de nanopartículas contendo melanina para aumentar a eficácia de depilação através de luz pulsada intensa', 'propriedades eletrônicas e estruturais de c59si na superfície do monohidreto si(100)', 'um ambiente de simulação para nanopartículas poliméricas baseado em sistemas multiagentes', 'estudo teórico de pequenas moléculas aromáticas adsorvidas em grafeno puro e funcionalizado', 'estudo teórico de adsorção de si em nanotubos de carbono', 'avaliação do efeito crônico da administração ip de &#946; ciclodextrinas sobre  paramêtros hepáticos e renais em ratos', 'nanopartículas de prata contra staphylococcus aureus resistente a meticilina uma revisão de literatura', 'desenvolvimento de nanocápsulas poliméricas carregadas de mangiferina', 'síntese, caracterização e avaliação da citotoxicidade da nanossílica magnética na linhagem celular l929', 'estudo ab initio das propriedades estruturais eletrônicas e magnéticas do grafeno carboxilado', 'efeitos de transferência de carga em nanotubos de carbono de parede simples tratados com ácido', 'agente de ferro zero valente em escala nano em áreas contaminadas uma revisão']

contador = 0



    
for elemento in titulos_traduzidos:
    
    elemento = elemento.lower()
    
    if "teoria funcional da densidade" in elemento:
        elemento = elemento.replace("teoria funcional da densidade", "dft")
    
    if "nanotubos de  carbono"  in elemento:
        elemento = elemento.replace("nanotubos de  carbono", "nanotubos de carbono")
        
    if "co-exposição" in elemento or "co-solvente" in elemento:
        elemento = elemento.replace("-", " ")
    
    if "nanotubo de carbono" in elemento:
        elemento = elemento.replace("nanotubo de carbono", "nanotubos de carbono")
    
    if "ab inito" in elemento:
        elemento = elemento.replace("ab inito", "ab initio")
    
    if "nanotubos de carbono" in elemento:
        
        palavras_titulo.append("nanotubos de carbono")
        elemento = elemento.replace("nanotubos de carbono", "")
        
    if "ab initio" in elemento:
        palavras_titulo.append("ab initio")
        elemento = elemento.replace("ab initio", "")
    
    elementos_titulo = elemento.split(" ")

    
    for palavra in elementos_titulo:
             
        if "," in palavra:
            palavra = palavra.replace(",", "")
             
            
        if "</i>" in palavra:
            palavra = palavra.replace("</i>", "")
            
        
        if pode_inserir(palavra):
            
            palavra = palavra.rstrip().lstrip()
            palavras_titulo.append(palavra)



ocorrencias = Counter(palavras_titulo)
ocorrencias = dict(sorted(ocorrencias.items(), key=lambda item: item[1]))
#print(ocorrencias)


for elementos in ocorrencias:
    rep = ocorrencias[elementos]
    if rep > 3:
        
        print(elementos, rep, str(round(rep*100/len(titulos_traduzidos)))+"%")


arquivo.close()
