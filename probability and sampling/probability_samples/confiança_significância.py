import pandas as pd
import numpy as np
from scipy.stats import norm

data = pd.read_csv('dados.csv')

#Suponha que os pesos dos sacos de arroz de uma indústria alimentícia se distribuem aproximadamente como uma normal de desvio padrão populacional igual a 150 g. Selecionada uma amostra aleatório de 20 sacos de um lote específico, obteve-se um peso médio de 5.050 g. Construa um intervalo de confiança para a média populacional assumindo um nível de significância de 5%

tabela_normal_padronizada = pd.DataFrame(
    [], 
    index=["{0:0.2f}".format(i / 100) for i in range(0, 400, 10)],
    columns = ["{0:0.2f}".format(i / 100) for i in range(0, 10)])

for index in tabela_normal_padronizada.index:
    for column in tabela_normal_padronizada.columns:
        Z = np.round(float(index) + float(column), 2)
        tabela_normal_padronizada.loc[index, column] = "{0:0.4f}".format(norm.cdf(Z))

tabela_normal_padronizada.rename_axis('Z', axis = 'columns', inplace = True)

#grafico no arquivo Curso_de_Estatística 4.2

def intervalos():
    #Anotando dados do exercício
    media_amostra = 5050
    significancia = 0.05
    confianca = 1 - significancia
    desvio_padrao = 150
    n = 20 

    #calculando z
    prob = 0.5 + (confianca / 2)
    z = norm.ppf(prob)

    #Calculando o erro 
    sigma = desvio_padrao / np.sqrt(n)
    e = z * sigma

    #Calculo do intervalo de confiança para media de amostras
    intervalo_de_confianca = norm.interval(alpha = 0.95, loc = media_amostra, scale = sigma)
    print(intervalo_de_confianca)
    
def calculo_populacao(): # População Infinita/Indeterminada
    
    #Estamos estudando o rendimento mensal dos chefes de domicílios no Brasil. Nosso supervisor determinou que o erro máximo em relação a média seja de R$\$$ 100,00. Sabemos que o desvio padrão populacional deste grupo de trabalhadores é de R$\$$ 3.323,39. Para um nível de confiança de 95%, qual deve ser o tamanho da amostra de nosso estudo?
    
    # e = z * (sigma/sqrt(n)) isolando n -> n = (z * (sigma/e)) ** 2 onde sigma = desvio padrao
    
    e = 100
    sigma = 3323.39
    confianca = 0.95
    prob = 0.5 + (confianca / 2)
    z = norm.ppf(prob)
    
    #Calculando n (tamanho necessario da amostra para que esses dados sejam validos)
    n = (z * (sigma / e)) ** 2
    print(n.round())

def standard_sample_deviation(): #Populacao Finita
    
    #Em um lote de 10.000 latas de refrigerante foi realizada uma amostra aleatória simples de 100 latas e foi obtido o desvio padrão amostral do conteúdo das latas igual a 12 ml. O fabricante estipula um erro máximo sobre a média populacional de apenas 5 ml. Para garantir um nível de confiança de 95% qual o tamanho de amostra deve ser selecionado para este estudo?
    
    #N = tamanho da população

    #z = variável normal padronizada

    #\sigma = desvio padrão populacional

    #s = desvio padrão amostral

    #e = erro inferencial   
    
    N = 2000
    z = norm.ppf((0.5 + (0.95 / 2))) 
    s = 480 #Desvio e erro sempre na mesma medida
    e = 300 

    tamanho_da_amostra = ((z**2) * (s**2) * (N)) / (((z**2) * (s**2)) + ((e**2) * (N - 1)))
    
    print(tamanho_da_amostra.round())
    
standard_sample_deviation()