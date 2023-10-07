"""TextUility URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.index,name='index'),
    # path('remove',views.removefunc,name='removefunc'),
    # path('cap',views.capfirst,name='capfirst'),
    # path('newline',views.newlineremove,name='newlineremove'),
    # path('space',views.spaceremove,name='spaceremove'),
    # path('char',views.charcount,name='charcount')
    path('',views.index,name='index'),
    path('analyze',views.Analyze,name='analyze'),
    path('copytext',views.copytext,name='copytext'),
    path('playlist/',views.ExtractPlaylistVideos,name='playlist'),
    path('videos/',views.LoadVideos,name='playlist')
    
]
