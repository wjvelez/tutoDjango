from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'daw.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^diagrams/','web.views.diagrams'),
    url(r'^login/', 'web.views.login'),
    url(r'^$','web.views.home'),
]
