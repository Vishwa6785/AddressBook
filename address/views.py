from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Address
from address.forms import ContactForm
from django.core.mail import EmailMessage


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

#def contact(request):
	#form_class = ContactForm
	#context = {'form':form_class}
	#return render(request, 'contact.html', context)

def thanks(request):
	return HttpResponse("Thank you and Have a great day!!!")

#email logic: getting data from form and sending mail 

def contact(request):
	form_class = ContactForm
	print dir(form_class)
	context = {'form':form_class}

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			print dir(form)
			subject = "A new contact/lead"
			contact_name = form.cleaned_data['contact_name']
			contact_email = form.cleaned_data['contact_email']
			content = form.cleaned_data['content']
			email = EmailMessage(subject, contact_name + '\n'
				+ contact_email + '\n' + content
				)
			email.send()
		return HttpResponseRedirect('/thanks/')
	return render(request, 'contact.html', context)

