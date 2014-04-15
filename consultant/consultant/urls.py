from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'consultant.views.home', ),
    url(r'^home', 'consultant.views.home', ),
    url(r'^college_search', 'consultant.views.college_search', ),
    url(r'^common_myths', 'consultant.views.common_myths', ),
    url(r'^about_us', 'consultant.views.about_us', ),
    url(r'^contact_us', 'consultant.views.contact_us', ),
)
