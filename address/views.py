from django.shortcuts import render
from django.http import HttpResponse
from .models import Address


# Create your views here.
# request (url)->view(function)->response(url)

def hello_world(request):
	return HttpResponse('hello world!!!')



#def test_html(request):
#	f = open("/root/Documents/Addressbook/src/address/templates/test.html")
#	content = f.read()
#	return HttpResponse(content)

def test_html(request):
	context={}
	return render(request,'address/test.html',context)


def address_html(request):
	context={}
	return render(request,'address/address.html',context)



#def address_html(request):
#	context={'name1':'student1','name2':'student2','email1':'student1@edu.com','email2':'student2@edu.com'}
#	return render(request,'address.html',context)


#def address_html(request):
#	context={'namesdb':[{'name':'student1','email':'stu1@edu.com'},{'name':'student2','email':'stu2@edu.com'}]}
#	return render(request,'address.html',contex

def address_html(request):
	values = Address.objects.all()
	context = {'namesdb':values}
	return render(request,'address.html',context)