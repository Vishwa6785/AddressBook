from django.shortcuts import render

# Create your views here.
def newtest_html(request):
	context = {}
	return render(request, 'newtest_app/test.html', context)
