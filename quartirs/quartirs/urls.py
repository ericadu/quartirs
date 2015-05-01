from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'quartirs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^quartirs_app/', include('quartirs_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
