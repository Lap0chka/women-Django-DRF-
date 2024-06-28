from django.shortcuts import render

def index(reqeust):
    return render(reqeust, 'women/base.html')
