from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'base.views.home', name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.md'), name="about"),
    url(r'^gettingstarted/$', TemplateView.as_view(template_name='gettingstarted.md'), name="getting_started"),
    url(r'^news_signup/$', 'base.views.email_thanks', name='email_thanks'),
    # url(r'^wwwdocker/', include('wwwdocker.foo.urls')),
    url(r'^tutorial/', include('tutorial.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
