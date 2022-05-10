from django.shortcuts import render
import pandas as pd
import pickle
# Create your views here.


def home(request):
    return render(request, 'movie_class/home.html')

def exploreDataset(request):
    df = pd.read_csv('movie_class\static\data\labelled_movie_dataset.csv')
    to_html = df.to_html(index=False, justify='start')
    context = {'data': to_html}
    return render(request, 'movie_class/explore_dataset.html', context)