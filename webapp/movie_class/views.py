import re
from django.shortcuts import render
import pandas as pd
import pickle
# Create your views here.


def home(request):
    context = {}
    if request.method == 'POST':
        title = request.POST.get('movieTitle');
        main_actor = request.POST.get('mainActor')
        second_actor = request.POST.get('secondActor')
        director_name = request.POST.get('directorName')
        meta_score = float(request.POST.get('metaScore'))
        imdb = float(request.POST.get('imdb'))
        rotten_tomatoes = float(request.POST.get('rottenTomatoes'))
        #Reading the dataset and laoding the model
        df = pd.read_csv('movie_class\static\data\labelled_movie_dataset.csv')
        model_pkl = open('movie_class\static\data\\adb_model.pkl', 'rb')
        model = pickle.load(model_pkl)
        # getting rates from dataset
        main_actor_rate = df.loc[df['Main_actor'] == main_actor, 'Main_actor_rate'].iloc[0]
        second_actor_rate = df.loc[df['Second_actor'] == second_actor, 'Second_actor_rate'].iloc[0]
        director_rate = df.loc[df['Director'] == director_name, 'Director_rate'].iloc[0]
        
        prediction = model.predict([[imdb, meta_score, rotten_tomatoes, main_actor_rate, second_actor_rate, director_rate]])
        
        # print([main_actor_rate, second_actor_rate, director_rate])
        # print([title, main_actor, second_actor, director_name, meta_score, imdb, rotten_tomatoes])
        # print("Prediction result: ", prediction[0])
        if prediction[0] == 0:
            result = "Blockbuster"
        elif prediction[0] == 1:
            result = "Flop"
        elif prediction[0] == 2:
            result = "Hit"
        context = {'title': title, 'result': result, 'director':director_name}
    return render(request, 'movie_class/home.html', context)

def exploreDataset(request):
    df = pd.read_csv('movie_class\static\data\labelled_movie_dataset.csv')
    to_html = df.to_html(index=False, justify='start')
    context = {'data': to_html}
    return render(request, 'movie_class/explore_dataset.html', context)