import re
from django.shortcuts import render
import pandas as pd
import pickle
# Create your views here.


def home(request):
    if request.method == 'POST':
        title = request.POST.get('movieTitle');
        main_actor = request.POST.get('mainActor')
        second_actor = request.POST.get('secondActor')
        director_name = request.POST.get('directorName')
        meta_score = float(request.POST.get('metaScore'))
        imdb = float(request.POST.get('imdb'))
        rotten_tomatoes = float(request.POST.get('rottenTomatoes'))
        
        df = pd.read_csv('movie_class\static\data\labelled_movie_dataset.csv')
        model_pkl = open('movie_class\static\data\dt_model.pkl', 'rb')
        model = pickle.load(model_pkl)
        
        
        main_actor_rate = df.loc[df['Main_actor'] == main_actor, 'Main_actor_rate'].iloc[0]
        second_actor_rate = df.loc[df['Second_actor'] == second_actor, 'Second_actor_rate'].iloc[0]
        director_rate = df.loc[df['Director'] == director_name, 'Director_rate'].iloc[0]
        prediction = model.predict([[imdb, meta_score, rotten_tomatoes, main_actor_rate, second_actor_rate, director_rate]])
        
        print([main_actor_rate, second_actor_rate, director_rate])
        print([title, main_actor, second_actor, director_name, meta_score, imdb, rotten_tomatoes])
        print("Prediction result: ", prediction[0])
    return render(request, 'movie_class/home.html')

def exploreDataset(request):
    df = pd.read_csv('movie_class\static\data\labelled_movie_dataset.csv')
    to_html = df.to_html(index=False, justify='start')
    context = {'data': to_html}
    return render(request, 'movie_class/explore_dataset.html', context)