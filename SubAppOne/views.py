from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):

	return HttpResponse("This is the stOry of a grrl...")

