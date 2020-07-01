from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage,name="homepage"),
    path('bank/<bank_name>/<city>/',views.banklist.as_view()),
    path('branch/<ifsc>',views.branchlist.as_view()),
    
]
