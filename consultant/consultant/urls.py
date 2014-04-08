from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'consultant.views.home', ),
    url(r'^home', 'consultant.views.home', ),
    url(r'^about_us', 'consultant.views.about_us', ),
    url(r'^quick_facts', 'consultant.views.quick_facts', ),
    url(r'^search', 'consultant.views.search', ),
    url(r'^contact_us', 'consultant.views.contact_us', ),
    url(r'^quiz', 'consultant.views.quiz', ),
)
