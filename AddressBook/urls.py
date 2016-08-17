from django.conf.urls import include, url
from django.contrib import admin
from address.views import hello_world, test_html, address_html, contact, thanks
from newtest_app.views import newtest_html


#from address.views import 
urlpatterns = [
    # Examples:
    # url(r'^$', 'AddressBook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'address.views.hello_world', name='home'),
    url(r'^test_html',test_html, name='html'),
    url(r'^address',address_html, name='html'),
    url(r'^newtest_html', newtest_html, name='newtest_html'), 
    url(r'^contact', contact,name="contact"),
    url(r'^thanks', thanks, name="thanks")

]
