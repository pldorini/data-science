import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

data = pd.read_csv('dataset/dados.csv')

sexo = {
    0: 'Masculino', 
    1: 'Feminino'
}
cor = {
    0: 'Indígena', 
    2: 'Branca', 
    4: 'Preta', 
    6: 'Amarela', 
    8: 'Parda', 
    9: 'Sem declaração'
}
anos_de_estudo = {
    1: 'Sem instrução e menos de 1 ano', 
    2: '1 ano', 
    3: '2 anos', 
    4: '3 anos', 
    5: '4 anos', 
    6: '5 anos', 
    7: '6 anos', 
    8: '7 anos', 
    9: '8 anos', 
    10: '9 anos', 
    11: '10 anos', 
    12: '11 anos', 
    13: '12 anos', 
    14: '13 anos', 
    15: '14 anos', 
    16: '15 anos ou mais', 
    17: 'Não determinados'
}
uf = {
    11: 'Rondônia', 
    12: 'Acre', 
    13: 'Amazonas', 
    14: 'Roraima', 
    15: 'Pará', 
    16: 'Amapá', 
    17: 'Tocantins', 
    21: 'Maranhão', 
    22: 'Piauí', 
    23: 'Ceará', 
    24: 'Rio Grande do Norte', 
    25: 'Paraíba', 
    26: 'Pernambuco', 
    27: 'Alagoas', 
    28: 'Sergipe', 
    29: 'Bahia', 
    31: 'Minas Gerais', 
    32: 'Espírito Santo', 
    33: 'Rio de Janeiro', 
    35: 'São Paulo', 
    41: 'Paraná', 
    42: 'Santa Catarina', 
    43: 'Rio Grande do Sul', 
    50: 'Mato Grosso do Sul', 
    51: 'Mato Grosso', 
    52: 'Goiás', 
    53: 'Distrito Federal'
}

def bar_plot_frequency_and_percentual():
    classes = [
    data.Renda.min(),
    2 * 788,
    5 * 788,
    15 * 788,
    25 * 788,
    data.Renda.max()
    ]
    
    labels = ['E', 'D', 'C', 'B', 'A']
    
    frequency = pd.value_counts(
        pd.cut(x = data.Renda,
        bins = classes,
        labels = labels,
        include_lowest = True)
    )
    
    percentual = pd.value_counts(
        pd.cut(x = data.Renda,
            bins = classes,
            labels = labels,
            include_lowest= True
        ), normalize= True
    )*100
    
    dist_freq_wage = pd.DataFrame({'Frequency': frequency, 'Percentual %': percentual}).sort_index(ascending = False)
    
    dist_freq_wage['Frequency'].plot.bar(width = 1, color = 'blue', alpha = 0.2, figsize=(14, 6))
    plt.show()
    
def dist_plot_quantitative_variables_Age():
    gp = sns.distplot(data['Idade'])
    gp.figure.set_size_inches(14, 6)
    gp.set_title('Frequency Distribution - AGE', fontsize=18)
    gp.set_xlabel('Years', fontsize=14)
    plt.show()
    
def dist_plot_quantitative_variables_Height():
    gp = sns.distplot(data['Altura'])
    gp.figure.set_size_inches(14, 6)
    gp.set_title('Frequency Distribution - HEIGHT', fontsize=18)
    gp.set_xlabel('Meter', fontsize=14)
    plt.show()
    
def dist_plot_quantitative_variables_income():
    gp = sns.distplot(data.query('Renda < 15000')['Renda'])
    gp.figure.set_size_inches(14, 6)
    gp.set_title('Frequency Distribution - WAGE', fontsize=18)
    gp.set_xlabel('R$', fontsize=14)
    plt.show()
    
def crosstab_mf_color():
    frequency = pd.crosstab(data.Sexo,
                         data.Cor
                        )
    frequency.rename(index = sexo, inplace = True)
    frequency.rename(columns = cor, inplace = True)
    
    percentual = (pd.crosstab(data.Sexo,
                             data.Cor,
                             normalize= True
                            )*100).round(2)
    percentual.rename(index = sexo, columns= cor, inplace= True)

def descriptive_analysis_by_income():
    media = data.Renda.mean().round(2)
    mediana = data.Renda.median().round(2)
    moda = data.Renda.mode().round(2)
    std_mean_var = data.Renda.mad().round(2)
    variance = data.Renda.var().round(2)
    stand_variation = data.Renda.std().round(2)
    
    print(f'\033[31mMean:\033[m\n{media}\n\033[32mMedian:\033[m\n{mediana}\n\033[33mMode:\033[m\n{moda}\n\033[34mStandart Mean Variation:\033[m\n{std_mean_var}\n\033[35mVariance:\033[m\n{variance}\n\033[36mStandart Variation:\033[m\n{stand_variation}')
    
def income_by_sex_color():
    income_statistics = pd.crosstab(
                            data.Sexo,
                            data.Cor,
                            values= data.Renda,
                            aggfunc=['mean', 'median', 'max']
                        )
    income_statistics.rename(index = sexo, inplace= True)
    income_statistics.rename(columns= cor, inplace= True)
    print(income_statistics)
    
def dispersion_measure_by_sex_color():
    renda_dispersao_por_sexo_e_cor = pd.crosstab(data.Cor, 
                                         data.Sexo,
                                         aggfunc = {'mad', 'var', 'std'},
                                         values = data.Renda).round(2)
    renda_dispersao_por_sexo_e_cor.rename(index = cor, inplace = True)
    renda_dispersao_por_sexo_e_cor.rename(columns = sexo, inplace = True)
    print(renda_dispersao_por_sexo_e_cor)
    
def box_plot_by_income_between_sex_color():
    gp = sns.boxplot(x = 'Renda', y = 'Cor', hue = 'Sexo', data=data.query('Renda < 10000'), orient='h')

    gp.figure.set_size_inches(14, 8)    # Personalizando o tamanho da figura

    gp.set_title('Box-plot da RENDA por SEXO e COR', fontsize=18)    # Configurando o título do gráfico

    gp.set_xlabel('R$', fontsize=14)    # Configurando o label do eixo X

    gp.set_ylabel('Cor', fontsize=14)    # Configurando o label do eixo Y
    gp.set_yticklabels(['Indígena', 'Branca', 'Preta', 'Amarela', 'Parda'], fontsize=12)    # Configurando o label de cada categoria do eixo Y

    # Configurações da legenda do gráfico (Sexo)
    handles, _ = gp.get_legend_handles_labels()
    gp.legend(handles, ['Masculino', 'Feminino'], fontsize=12)
    
    plt.show()
    
def income_less_than_789():
    from scipy import stats

    percentual = stats.percentileofscore(data.Renda, 788, kind = 'weak')
    print("{0:.2f}%".format(percentual))
    
def maximum_value_earned_by_99percent():
    valor = data.Renda.quantile(.99)
    print("R$ {0:.2f}".format(valor))

def descriptive_analysis_by_income_betweem_years_of_study():
    renda_estatisticas_por_sexo_e_estudo = pd.crosstab(data['Anos de Estudo'], 
                                         data.Sexo,
                                         aggfunc = {'mean', 'median', 'max', 'std'},
                                         values = data.Renda).round(2)
    renda_estatisticas_por_sexo_e_estudo.rename(index = anos_de_estudo, inplace = True)
    renda_estatisticas_por_sexo_e_estudo.rename(columns = sexo, inplace = True)
    print(renda_estatisticas_por_sexo_e_estudo)
 
def box_plot_by_income_between_years_of_study():
    gp = sns.boxplot(x = 'Renda', y = 'Anos de Estudo', hue = 'Sexo', data=data.query('Renda < 10000 and Idade == 50'), orient='h')

    gp.figure.set_size_inches(14, 8)    # Personalizando o tamanho da figura

    gp.set_title('Box-plot da RENDA por SEXO e ANOS DE ESTUDO', fontsize=18)    # Configurando o título do gráfico

    gp.set_xlabel('R$', fontsize=14)    # Configurando o label do eixo X

    gp.set_ylabel('Anos de Estudo', fontsize=14)    # Configurando o label do eixo Y
    gp.set_yticklabels([key for key in anos_de_estudo.values()], fontsize=12)    # Configurando o label de cada categoria do eixo Y

    # Configurações da legenda do gráfico (Sexo)
    handles, _ = gp.get_legend_handles_labels()
    gp.legend(handles, ['Masculino', 'Feminino'], fontsize=12)
    plt.show()
   
def analysis_between_income_and_UF():
    renda_estatisticas_por_uf = data.groupby(['UF']).agg({'Renda': ['mean', 'median', 'max', 'std']})
    renda_estatisticas_por_uf.rename(index = uf, inplace= True)
    print(renda_estatisticas_por_uf)

def box_plot_between_income_and_UF():
    gp = sns.boxplot(x = 'Renda', y = 'UF', data=data.query('Renda < 10000'), orient='h')

    gp.figure.set_size_inches(14, 8)    # Personalizando o tamanho da figura

    gp.set_title('Box-plot da RENDA por ESTADOS', fontsize=18)    # Configurando o título do gráfico

    gp.set_xlabel('R$', fontsize=14)    # Configurando o label do eixo X

    gp.set_ylabel('Estados', fontsize=14)    # Configurando o label do eixo Y
    gp.set_yticklabels([key for key in uf.values()], fontsize=12)    # Configurando o label de cada categoria do eixo Y
    plt.show()

