import pandas as pd   
from scipy.stats import norm, binom
import numpy as np   

data = pd.read_csv('dados.csv')


def problema_A_B():
    #Avaliando nosso dataset é possível verificar que a proporção de homens como chefes de domicílios é de quase 70%. Precisamos selecionar aleatoriamente grupos de 10 indivíduos para verificar as diferenças entre os rendimentos em cada grupo. Qual a probabilidade de selecionarmos um grupo que apresente a mesma proporção da população, ou seja, selecionarmos um grupo que seja composto por 7 homens e 3 mulheres?

    numero_pessoas_por_sexo = data.Sexo.value_counts()

    n = 10
    p = 0.7
    k = 7
    
    probabilidade_de_sucesso = binom.pmf(k, n, p)
    print(f'Probabilidade de haver um grupo com 7 homens e 3 mulheres: {probabilidade_de_sucesso*100:.2f} %')
    
    #quantos grupos de 10 indivíduos nós precisaríamos selecionar, de forma aleatória, para conseguir 100 grupos compostos por 7 homens e 3 mulheres?
    
    #u = numero_de_grupos * prob onde u = 100, prob = probabilidade de sucesso
    numero_de_grupos = (100 / probabilidade_de_sucesso).round(0)
    print(f'Número de grupos de 10 indivíduos: {numero_de_grupos}')
    

   
def problema_C():
        #Olhar o arquivo "Estimativas.ipynb"
        dataset = data.Renda.sample(n = 200, random_state= 101)  
        
        media = dataset.mean()
        desvio_padrao = dataset.std()
        e = 0.1 * media
        confianca_de_90 = 0.9
        confianca_de_95 = 0.95
        confianca_de_99 = 0.99
            
        z_90 = norm.ppf(0.5 + (confianca_de_90 / 2))
        z_95 = norm.ppf(0.5 + (confianca_de_95 / 2))
        z_99 = norm.ppf(0.5 + (confianca_de_99 / 2))
            
        n_com_90_de_confianca = ((z_90 * (desvio_padrao / e)) ** 2).round()
        n_com_95_de_confianca = ((z_95 * (desvio_padrao / e)) ** 2).round()
        n_com_99_de_confianca = ((z_99 * (desvio_padrao / e)) ** 2).round()
        
        while True:    
            choice = int(input('''Selecione o item para ser analisado: 
                [1] -> Media e desvio padrao da amostra
                [2] -> Tamanho da amostra com o erro fornecido para confiança de 90%, 95%, 99%
                [3] -> Custo de pesquisa para os três níveis de confiança
                [4] -> Para o maior nível de confiança viável (dentro do orçamento disponível), obtenha um intervalo de confiança para a média da população
                [5] -> Assumindo o nível de confiança escolhido no item anterior, qual margem de erro pode ser considerada utilizando todo o recurso disponibilizado pelo cliente?
                [6] -> Assumindo um nível de confiança de 95%, quanto a pesquisa custaria ao cliente caso fosse considerada uma margem de erro de apenas 5% em relação a média estimada?
                '''))
            
            if choice == 1:
                
                print(f'Media: {media:.2f}\n')
                print(f'Desvio: {desvio_padrao:.2f}')
    
            elif choice == 2:
        
                print(f'Para um nível de 90% de confiança, devemos selecionar {n_com_90_de_confianca} elementos\nPara um nível de 95% de confiança, devemos selecionar {n_com_95_de_confianca} elementos\nPara um nível de 99% de confiança, devemos selecionar {n_com_99_de_confianca} elementos ')
            
            elif choice == 3:
                
                print(f'O custo de pesquisa para o nivel de confianca de 90% é de R${n_com_90_de_confianca*100}\n O custo de pesquisa para o nivel de confianca de 95% é de R${n_com_95_de_confianca*100}\n O custo de pesquisa para o nivel de confianca de 99% é de R${n_com_99_de_confianca*100} ')
                
            elif choice == 4:
                intervalo = norm.interval(alpha= 0.95, loc = dataset.mean(), scale = desvio_padrao / np.sqrt(n_com_95_de_confianca))
                print(f'Intervalo de confiança para a média da poulação: {intervalo}')
                            
            elif choice == 5:
                recurso = 150000
                custo_entrevista = 100
                n_com_95 =  recurso / custo_entrevista
                
                z = norm.ppf(0.975)
                e = z * (desvio_padrao / np.sqrt(n_com_95))
                
                nova_margem_de_erro = ((e / media) * 100).round(2)
                print(f'A nova margem de erro é de {nova_margem_de_erro} %')
            
            elif choice == 6:
                custo_entrevista = 100
                e = 0.05 * media
                z = norm.ppf(0.975)
                n_com_95_de_confianca = ((z * (desvio_padrao / e)) ** 2).round()
                
                custo_para_95 = n_com_95_de_confianca * custo_entrevista
                
                print(f'Para um nivel de 95% de confiança, nossa amostra deverá conter {n_com_95_de_confianca} elementos, com um custo de R${custo_para_95:,.2f}')

            continuar_ou_sair = str(input('''Deseja continuar?
                [S] -> SIM
                [N] -> NÃO
                '''))
            if continuar_ou_sair in 'Ss':
                continue
            else: 
                break
            
        print('Muito obrigado por ter reservado seu tempo para olhar meu programa, até a próxima!')


problema_C()
