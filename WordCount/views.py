from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html',{'hithere':"we are known for what we do ,still fuck you too"})

def count(request):
    myinfo=request.GET['infotext']
    wordcountlist=myinfo.split()
    dictionaryword={}
    for word in wordcountlist:
        if word in dictionaryword:
            dictionaryword[word]+=1
        else :
            dictionaryword[word]=1

    sortedwords=sorted(dictionaryword.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'info':myinfo,'number':len(wordcountlist),'dictionaryword':sortedwords})
def about(request):
    return render(request,'about.html')
    
