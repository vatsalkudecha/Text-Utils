from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     # return HttpResponse("Home")
#     # params = {'name':'Vatsal', 'place': 'Place Nahi bataunga'}
#
#     return render(request, 'index.html')

def index2(request):

    return render(request, 'index2.html')

def analyze(request):

    # Get the text
    djtext = request.POST.get('text','default')
    print(djtext)

    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    countchar = request.GET.get('countchar', 'off')

    #Analyze the text
    # analyzed = djtext

    # Check which checkbox is on
    if removepunc=="on":
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps =="on":
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'FULL CAPS', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)


    if (newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!= "\r":
                analyzed = analyzed + char

        params = {'purpose':'New Lines Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]=="space"):

                analyzed = analyzed + char

        params = {'purpose':'Extra Spaces Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)


    if(removepunc!="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("Error")

    return render(request, 'analyze2.html', params)