from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
    # return HttpResponse('Home')
def analyze(request):
    # Get the text
    djtext = request.POST.get('text','default')

    # Check checkbox values
    rempunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

    # Check which checkbox is on
    if rempunc == "on":
        punctuations = '''!()-[]{}:;'"\,<>./?@#$%^&*_-'''
        analyzed = ""
        for i in djtext:
            if i not in punctuations:
                analyzed+=i
        params = {'purpose' : 'Removed Punctuations', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html', params)
    elif(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed+=char.upper()
        params = {'purpose' : 'Changed to Uppercase', 'analyzed_text' : analyzed}
        return render(request, 'analyze.html',params)
    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            # In network to remove new lines we need to add "\r" along with "\n"
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif (spaceremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != " ":
                analyzed += char
        params = {'purpose': 'Removed Spaces', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else :
        return HttpResponse("Error")