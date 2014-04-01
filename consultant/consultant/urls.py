from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'consultant.views.home', ),
    url(r'^link1$', 'consultant.views.llink1', ),
    url(r'^link2$', 'consultant.views.llink2', ),
    url(r'^link3$', 'consultant.views.llink3', ),
    url(r'^link4$', 'consultant.views.llink4', ),
)
