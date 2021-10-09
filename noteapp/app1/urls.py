from django.urls import path
from . import views
urlpatterns = [
    path('',views.MyApp.as_view(),name='mynotes'),
    path('<int:pk>/',views.MyAppDetail.as_view(),name='mynotesdetail')
]
