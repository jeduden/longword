from django.conf.urls import patterns, include, url
from django.contrib import admin

from game import views

urlpatterns = patterns('',
    url(r'',include('game.urls',namespace='game')),
    url(r'^admin/', include(admin.site.urls))
)

