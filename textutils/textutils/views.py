# i have created thsi file- vanshika

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from translate import Translator

def index2(request):
    return render(request, 'index2.html')

def analyze(request):

    djtext = request.GET.get('text', 'default')
    translator = Translator(to_lang='Hindi')
    analyzed = translator.translate(djtext)





    params = {'purpose': 'Translated', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)

