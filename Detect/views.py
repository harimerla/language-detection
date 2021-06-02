from django.shortcuts import render
from django.http import HttpResponse
import os
import pickle
import pandas as pd
import sklearn

# Create your views here.
def index(request):
    if request.method=="POST":
        print('POST')
        query = request.POST['input']
        lang = Predict(query)
        return render(request, 'index.html', {'text': query, 'lang': lang})
    else:
        print('GET')
        return render(request, 'index.html')

def Predict(text):
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_name = 'language_detect.pkl'
    print(os.path.join(base_path,file_name))
    text = pd.Series(text)
    pipe = pickle.load(open(os.path.join(base_path,file_name), 'rb'))
    result = pipe.predict(text)
    print("Text: ", text.iloc[0], " Result: ",result)
    return result[0]
    