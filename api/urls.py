from django.urls import path,include
from .views import *
from .user_views import *

urlpatterns = [
     path('api/', SorovApiView.as_view()),
     path('hokim/',hokimpaneli,name='home'),
     path("hokim/1124424434354235412425/", hbarchasi, name="hammasi"),
     # user views
     path('signup/',singup,name='signup'),
     path('',include('django.contrib.auth.urls')),
     path('',CreateBlog.as_view(),name='new'),
     path('rahmat/',ramat,name='rahmat')
]