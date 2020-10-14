from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import logging
logger=logging.getLogger("blog.views")

# Create your views here.

def global_setting(request):
    return {
    "SITE_NAME":"鸟飘零的个人博客",
    "SITE_DESC":"专注python开发，欢迎和大家交流",
    "SITE_SINA" : "http://weibo.sina.com/yopeiying",
    "SITE_TENCENT" :"http://weibo.qq.com/yopeiying",
    "PRO_RSS" :"http://www.baidu.com",
    "PRO_EMAIL":"2589641825@qq.com"
    }

def index(request):
    # try:
    #     file=open("ss.txt","r")
    # except Exception as e:
    #     logger.error(e)

    # return HttpResponse("test")
    return render(request,"index.html",locals())
