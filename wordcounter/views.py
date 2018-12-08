from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    full_text = request.GET['fulltext']
    words = full_text.split()

    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    sorted_list = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'text':full_text, 'count':len(word_dictionary), 'wordlist':sorted_list})

def about(request):
    return render(request, 'about.html')
