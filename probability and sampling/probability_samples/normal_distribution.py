import pandas as pd
import numpy as np
from scipy.stats import norm

data = pd.read_csv('dados.csv')

#Em um estudo sobre as alturas dos moradores de uma cidade verificou-se que o conjunto de dados segue uma distribuição aproximadamente normal, com média 1,70 e desvio padrão de 0,1. Com estas informações obtenha o seguinte conjunto de probabilidades:

# A) probabilidade de uma pessoa, selecionada ao acaso, ter menos de 1,80 metros.

# B) probabilidade de uma pessoa, selecionada ao acaso, ter entre 1,60 metros e 1,80 metros.    

# C) probabilidade de uma pessoa, selecionada ao acaso, ter mais de 1,90 metros.

tabela_normal_padronizada = pd.DataFrame(
    [], 
    index=["{0:0.2f}".format(i / 100) for i in range(0, 400, 10)],
    columns = ["{0:0.2f}".format(i / 100) for i in range(0, 10)])

for index in tabela_normal_padronizada.index:
    for column in tabela_normal_padronizada.columns:
        Z = np.round(float(index) + float(column), 2)
        tabela_normal_padronizada.loc[index, column] = "{0:0.4f}".format(norm.cdf(Z))

tabela_normal_padronizada.rename_axis('Z', axis = 'columns', inplace = True)


def prob_de_obter_uma_pessoa_menor_que_180cm():
    x = 1.8
    media = 1.7
    desvio_padrao = 0.1

    z = (x - media) / desvio_padrao

    menos_de_1_metro_e_80 = norm.cdf(z) #Probabilidade de obter uma pessoa com menos de 1,8m
    return menos_de_1_metro_e_80
    

def prob_de_obter_uma_pessoa_entre_160_e_180cm(probabilidade_da_pessoa_ser_menor_que_180cm):
    
    probabilidade = (probabilidade_da_pessoa_ser_menor_que_180cm - 0.5) * 2
    print(probabilidade)

def prob_de_obter_uma_pessoa_maior_que_190cm():
    
    x, media, desvio_padrao = 1.9, 1.7, 0.1
    z = (x - media) / desvio_padrao
    #maior_que_190cm = 1 - norm.cdf(z) 
    #OU
    #maior_que_190cm = norm.cdf(-z) 
    complemento = norm.sf(z) #More Accurate

    print(complemento)
 
prob_de_obter_uma_pessoa_entre_160_e_180cm(prob_de_obter_uma_pessoa_menor_que_180cm())