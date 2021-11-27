from django.urls import path
from .views import mainappView, aboutView, cantactView,blogView

urlpatterns = [
    path('', mainappView.as_view(), name='home'),
    path('about/', aboutView.as_view(), name="about"),
    path('cantact/', cantactView.as_view(), name='cantact'),
    path('blog/', blogView.as_view(), name='blog')

]
