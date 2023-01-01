import pandas as pd
import numpy  as np
from scipy.special import comb
from scipy.stats import binom
import matplotlib.pyplot as plt
from scipy.stats import poisson

data = pd.read_csv('dados.csv')

#Em um concurso para preencher uma vaga de cientista de dados temos um total de 10 questões de múltipla escolha com 3 alternativas possíveis em cada questão. Cada questão tem o mesmo valor. Suponha que um candidato resolva se aventurar sem ter estudado absolutamente nada. Ele resolve fazer a prova de olhos vendados e chutar todas as resposta. Assumindo que a prova vale 10 pontos e a nota de corte seja 5, A) obtenha a probabilidade deste candidato acertar 5 questões e B) a probabilidade deste candidato passar para a próxima etapa do processo seletivo

#A
def probability_of_hit_5_questions():
    n = 10
    p = 1/3
    q = 1 - p
    k = 5
    
    #combination = (comb(n, k ) * (p**k) * (q**(n - k))) #Probabilidade de acertar 5 questões 
    #OR
    
    combination = binom.pmf(k, n, p)
    print(f'{combination:.5f}')

#B

def probability_of_success():
    n = 10
    p = 1/3
    q = 1-p
    
    #1° option
    #first_option = 1 - binom.cdf(4, n, p)
    #print(f'{first_option:.5f}')
    
    #2° option + fast
    second_option = binom.sf(4, n, p)
    print(f'{second_option:.5f}')


def probability_exercises():
    choice = int(input(''' Which exercise:
        [1] -> blue eyes
        [2] -> poisson
                       '''))
    
    if choice == 1:
        #Suponha que a probabilidade de um casal ter filhos com olhos azuis seja de 22%. Em 50 famílias, com 3 crianças cada uma, quantas podemos esperar que tenham dois filhos com olhos azuis?
        n = 3
        k = 2
        p = 0.22
        
        blue_eyes = binom.pmf(k, n, p) #probabilidade de exister 2 crianças de olhos azuis
        
        families_with_2_blue_eyes = 50 * blue_eyes # Possivel numero de familias com 2 filhos de olhos azuis
        print(families_with_2_blue_eyes)
        
    elif choice == 2:
        #O número médio de clientes que entram em uma padaria por hora é igual a 20. Obtenha a probabilidade de, na próxima hora, entrarem exatamente 25 clientes
        u = 20
        k = 25
        
        probabilidade = (poisson.pmf(k, u)) * 100
        print(f'{probabilidade} %')
   
    
def average_binomial_distribution():
    
    #Uma cidade do interior realiza todos os anos uma gincana para arrecadar fundos para o hospital da cidade. Na última gincana se sabe que a proporção de participantes do sexo feminino foi de 60%. O total de equipes, com 12 integrantes, inscritas na gincana deste ano é de 30. Com as informações acima responda: Quantas equipes deverão ser formadas por 8 mulheres?
    
    n = 12
    k = 8
    p = 0.6
    
    probabilidade = binom.pmf(k, n, p) #probabilidade de existir uma equipe com 8 mulheres
    
    avg_bin_dist = (30 * probabilidade).round(0) #Grupo com 8 mulheres
    print(avg_bin_dist)
  
    
def poisson_distribution():
    #Um restaurante recebe em média 20 pedidos por hora. Qual a chance de que, em determinada hora escolhida ao acaso, o restaurante receba 15 pedidos?
    u = 20
    k = 15
    
    #chance = ((((np.e**(-u)) * (u ** k))) / np.math.factorial(k))*100 #probabilidade em % de receber 15 pedidos em uma determinada hora 
    #print(f'{chance:.5f}%')
    
    #OR
    
    chance = poisson.pmf(k, u) * 100
    print(f'{chance} %')
    
probability_exercises()