import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

movie = pd.read_csv('arquivos/movies.csv')
rate = pd.read_csv('arquivos/ratings.csv')
tmdb = pd.read_csv('arquivos/tmdb_5000_movies.csv')

#ploting = rate.rating.plot(kind = 'hist')
#sns.boxplot(data = rate.rating)
#plt.show()

def analising_specific_movies():
    #selection_mean = rate.query('movieId==1').rating.mean()
    selection_df = rate.query('movieId==1')
    print(selection_df)
 
def analising_by_groupId():
    average_movies = rate.groupby('movieId').mean().rating
    #print(mean_movies.head(10))
    #mean_movies.plot(kind = 'hist')
    #sns.displot(average_movies)
    plt.hist(average_movies)
    plt.title("Film average histogram")
    plt.show()
    
 
def languages():
    #language_selection = tmdb["original_language"].value_counts().to_frame().reset_index()
    #language_selection.columns = ["original_language", "total"]
    #print(language_selection.head())
    
    #sns.catplot(x = "original_language", kind = "count", data = tmdb)
    #plt.show()
    
    total_por_lingua = tmdb["original_language"].value_counts()
    total_por_lingua.loc["en"]
    total_por_lingua = tmdb["original_language"].value_counts()
    total_geral = total_por_lingua.sum()
    total_de_ingles = total_por_lingua.loc["en"]
    total_do_resto = total_geral - total_de_ingles
    
    dados = {
        'lingua' : ['ingles', 'outros'],
        'total' : [total_de_ingles, total_do_resto]
    }
    
    new_df = pd.DataFrame(dados)
    sns.barplot(x = 'lingua', y = 'total', data = new_df)
    plt.show()

def languages_without_english():
    other_language_but_english = tmdb.query("original_language != 'en'")
    language_count = tmdb.query("original_language != 'en'").original_language.value_counts()
    sns.catplot(x = "original_language", order = language_count.index ,kind = "count", data = other_language_but_english, aspect=2, palette = "GnBu_d")
    plt.show()  
     
def rate_two_films():
    rate_toy_story = rate.query("movieId==1")
    rate_jumanji = rate.query("movieId==2")
    #print(f'Toy Story average grade: {rate_toy_story.rating.mean():.2f}')
    #print(f'Jumanji average grade: {rate_jumanji.rating.mean():.2f}')
    sns.boxplot(x = "movieId", y = "rating", data = rate.query("movieId in [1, 2]"))
    plt.show()
    
rate_two_films()
    
    