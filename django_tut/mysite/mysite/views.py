# I have created this file


# <---------------- code for printing hello_world and link --------------------------->
# from django.http import HttpResponse
# def index(request):
#     return HttpResponse('''<h1>Hello World</h1><a href="https://www.youtube.com"> dekhata kidhar hai? Tuze jo chaiye wo idhar hai?</a>''')
#
# def about(request):
#     return HttpResponse("This is all about page!!!")



#<-----------------------------code for laying the pipline--------------------------------------->
# from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Home")

# def removepunc(request):
#     return HttpResponse("Remove Punc")

# def capfirst(request):
#     return HttpResponse("Capitalize First")

# def newlinerem(request):
#     return HttpResponse("newlinerem First")

# def spaceremove(request):
#     return HttpResponse("spaceremove")

# def characterat(request):
#     return HttpResponse("Characterat")



# <-----------------------------code for adding a template--------------------------------------->
# from django.http import HttpResponse
# from django.shortcuts import render

# def index(request):
#     return render(request, 'index.html')

# def removepunc(request):
#     '''Get the text form name and textarea of index.html and analyze the input to removepunc page'''
#     djname = request.GET.get('name','default')
#     djyourviews = request.GET.get('yourviews','default')
#     print(djname,djyourviews)
#     return HttpResponse("Remove Punc")

# def capfirst(request):
#     return HttpResponse("Capitalize First")

# def newlinerem(request):
#     return HttpResponse("newlinerem First")

# def spaceremove(request):
#     return HttpResponse("spaceremove")

# def characterat(request):
#     return HttpResponse("Characterat")


#<-----------------------------code to perform different operations on text--------------------------------------->
# from django.http import HttpResponse
# from django.shortcuts import render

# def index(request):
#     return render(request, 'index1.html')

# def analyze(request):
#     '''Get the text form name and textarea of index.html and analyze the input to removepunc page'''
    
#     # get values of name and views from index1.html
#     djname = request.GET.get('name','default')
#     djyourviews = request.GET.get('yourviews','default')
    
#     #verify from user which operation should be performed using checkbox
#     removepunc = request.GET.get('removepunc','off')
#     capitalise = request.GET.get('capitalise','off')
#     print(djname,djyourviews,removepunc)

#     # conditions for functions working
#     punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_`~'''
#     analyzed=""
#     if removepunc=='on' and capitalise=='on':
#         for char in  djyourviews:
#             if char not in punctuations:
#                 analyzed = analyzed + char.upper()
#     elif removepunc=='on' and capitalise=='off':
#         for char in  djyourviews:
#             if char not in punctuations:
#                 analyzed = analyzed + char
#     elif removepunc=='off' and capitalise=='on':
#         for char in  djyourviews:
#             analyzed = analyzed + char.upper() 
#     else:
#         analyzed= djyourviews

#     # parameters given to analyze.html to print answer after performing operations
#     params={'name': djname,'analyzed_text': analyzed, 'checked1':removepunc, 'checked2':capitalise}

#     return render(request, 'analyze.html', params)

# def link(request):
#     return HttpResponse(''' <center><h1>Welcome to links</h1><table border="1"><tr><td>Website_Links</td></tr><tr><td><a href="https://www.google.com">Google</a></td></tr><tr><td><a href="https://www.facebook.com">Facebook</a></td></tr></table></center>''')



#<-----------------------------code to secure website by not showing all informattion in url ,modifications in previuos code--------------------------------------->
from django.http import HttpResponse
from django.shortcuts import render

def index1(request):
    return render(request, 'index1.html')

def analyze(request):
    '''Get the text form name and textarea of index.html and analyze the input to removepunc page'''
    
    # get values of name and views from index1.html
    djname = request.POST.get('name','default')
    djyourviews = request.POST.get('yourviews','default')
    
    #verify from user which operation should be performed using checkbox
    removepunc = request.POST.get('removepunc','off')
    capitalise = request.POST.get('capitalise','off')
    print(djname,djyourviews,removepunc)

    # conditions for functions working
    punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_`~'''
    analyzed=""
    if removepunc=='on' and capitalise=='on':
        for char in  djyourviews:
            if char not in punctuations:
                analyzed = analyzed + char.upper()
    elif removepunc=='on' and capitalise=='off':
        for char in  djyourviews:
            if char not in punctuations:
                analyzed = analyzed + char
    elif removepunc=='off' and capitalise=='on':
        for char in  djyourviews:
            analyzed = analyzed + char.upper() 
    else:
        analyzed= djyourviews

    # parameters given to analyze.html to print answer after performing operations
    params={'name': djname,'analyzed_text': analyzed, 'checked1':removepunc, 'checked2':capitalise}

    return render(request, 'analyze.html', params)