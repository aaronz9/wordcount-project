#now what we will do is we shall put new words in a dictionary

from django.http import HttpResponse
from django.shortcuts import render #this is a library used for the templates

import operator #we will need this to use sorted and itemgetter

def homepage(request):
    return render(request, 'home.html')  #two parameters reuquest and page name # dict also can pass

def about(request):
    return render(request,'about.html')



def count(request):
    fulltext = request.GET['fulltext']  #we will GET value of fulltext and put in variable fulltext

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:

        if word in worddictionary:
            worddictionary[word] += 1

        #increase in dictionary

        else:
            #we will add it to the dictionary
            worddictionary[word] = 1

    sortedWords = sorted(worddictionary.items(), key =operator.itemgetter(1), reverse = True)


    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedWords':sortedWords})

#if we pass it as a dictionary then we have tpo pass it as a dictionary outs
