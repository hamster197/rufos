from django.urls import path

from fl.views import PageDetailView

app_name = "fl"
urlpatterns = [
    #path('index/', PageIndexView.as_view(), name='index'),
    path('<pk>/', PageDetailView.as_view(), name='detail'),
]