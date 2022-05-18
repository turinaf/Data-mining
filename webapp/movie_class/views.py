from os import O_SHORT_LIVED
import re
from django.shortcuts import render, redirect
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
        
        if prediction[0] == 0:
            result = "Blockbuster"
            explanation = "The movie si successful"
        elif prediction[0] == 1:
            result = "Flop"
            explanation = "The movie Lost i.e Box office is less than Budget"
        elif prediction[0] == 2:
            result = "Hit"
            explanation = "The movie has no profit"
        context = {'title': title, 'director':director_name, 'm_actor': main_actor, 's_actor': second_actor,'metascore': meta_score, 
                   'imdb': imdb, 'rotten_tomatoes': rotten_tomatoes,  
                   'result': result, 'explanation': explanation }
        # redirect('result', context)
    return render(request, 'movie_class/home.html', context)

def result(request):
    return render(request, 'movie_class/result.html')

def exploreDataset(request):
    df1 = pd. read_csv('movie_class\static\data\disney_movies.csv')
    ori_dataset = df1.drop('Unnamed: 0', axis=1, inplace=True)
    ori_dataset = df1.to_html()
    o_summary = df1.describe(include=['int', 'float'])
    o_summary = o_summary.to_html()
    df = pd.read_csv('movie_class\static\data\labelled_movie_dataset.csv')
    df = df.sort_values(by=['Budget', 'Box_office'], ascending=False)
    p_summary = df.describe(include=['int', 'float'])
    p_summary = p_summary.to_html()
    cat_count = df['Category'].value_counts() 
    cat_count = cat_count.to_frame()
    cat_count = cat_count.to_html(header=False)
    to_html = df.to_html( justify='start')
    context = {'original': ori_dataset,'o_summary': o_summary, 'data': to_html, 'p_summary': p_summary, 'cat_count': cat_count}
    return render(request, 'movie_class/explore_dataset.html', context)