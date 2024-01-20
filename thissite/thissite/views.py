# i have created this file

from django.http import HttpResponse
from django.shortcuts import render
'''def index(request):
    return HttpResponse("<h1>Rinkal</h1> <a href='https://www.youtube.com'> click here </a>")

def about(request):
 
    return HttpResponse("good morning..")'''

'''

def index(request):
    return HttpResponse("Home")

def remove(request):
    return HttpResponse("remove punc ")

def capital(request):
    return HttpResponse("capitalize first")

def newline(request):
    return HttpResponse("newline")

def space(request):
    return HttpResponse("space")

def count(request):
    return HttpResponse("count <a href='http://127.0.0.1:8000/space'> click here </a>")'''

'''
def index(request):
    params={'name':'rinkal','place':'Mars'}
    return render(request,'index.html',params)'''

'''def index(request):
        return render(request,'index.html')

def remove(request):
    #get the text
    djtext=request.GET.get('text','default')
    print(djtext)
    #analys the text
    return HttpResponse("remove punc ")'''


def index(request):
        return render(request,'index.html')

def analyze(request):
    djtext=request.GET.get('text','default')
    jtext=request.GET.get('removepunc','off')
    fullcap=request.GET.get('fullcap','off')
    print(jtext)
    print(djtext)
    if jtext=="on":
    # analyze=jtext
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                    analyzed=analyzed+char
        params={'purpose':'removed punc','analyzed_text':analyze}
        #analys the text
        return render(request,"analyze.html",params)
    elif fullcap=="on":
         analyzed=""
         for char in djtext:
              analyzed=analyzed+char.upper()
              params={'purpose':'uppercase','analyzed_text':analyzed}
        #analys the text
              return render(request,"analyze.html",params)
    
    else:
          return HttpResponse("error")
    
def ex1(request):
    return HttpResponse('''<h2> navigation bar</h2>
    <a href "https://www.youtube.com">youtube</a></br>
    
    <a href "https://www.facebook.com">facebook</a></br>
    ''')