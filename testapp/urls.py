from django.urls import path, re_path
from . import views

app_name = 'testapp1'

urlpatterns=[
    re_path(r'^about/$',views.about, name='about'),
    path('def/',views.test1, name='test1'),

]