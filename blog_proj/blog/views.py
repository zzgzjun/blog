from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import logging
logger=logging.getLogger("blog.views")

# Create your views here.

def global_setting(request):
    return {
    "SITE_NAME":settings.SITE_NAME,
    "SITE_DESC":settings.SITE_DESC,
    "SITE_SINA" : settings.SITE_SINA,
    "SITE_TENCENT" :settings.SITE_TENCENT,
    "PRO_RSS" :settings.PRO_RSS,
    "PRO_EMAIL":settings.PRO_EMAIL,
    }

def index(request):
    # try:
    #     file=open("ss.txt","r")
    # except Exception as e:
    #     logger.error(e)

    # return HttpResponse("test")
    return render(request,"index.html",locals())
