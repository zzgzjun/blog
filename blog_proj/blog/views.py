from django.shortcuts import render
from django.http import HttpResponse
import logging
logger=logging.getLogger("blog.views")

# Create your views here.

def index(request):
    try:
        file=open("ss.txt","r")
    except Exception as e:
        logger.error(e)

    return HttpResponse("test")
