from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('', lambda request: redirect('/list/'), name='index'),
    path('list/', views.ListView.as_view(), name='list'),
    path('view/', views.ViewView.as_view(), name='view'),
    path('upload/', views.UploadView.as_view(), name='upload'),
]

def menus(request):
    return {'menus': [{
        'path': _path,
        'name': _name.title(),
        'active': request.resolver_match.url_name == _name,
        } for _path, _name in [
            ('/list/', 'list'),
            ('/view/', 'view'),
            ('/upload/', 'upload'),
        ]]
    }
