from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context_dict={'boldmessage':'Crunchy, creamy, cookie, candy, cupcakes!'}
    return render(request, 'rango/index.html', context=context_dict)
