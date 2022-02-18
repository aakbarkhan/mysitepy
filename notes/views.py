from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

HTML_STR = '''
<h1>Hello World</h1>
'''

def home_view(request):
    return HttpResponse(HTML_STR)
