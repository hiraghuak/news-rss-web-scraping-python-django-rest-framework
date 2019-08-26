from django.urls import path
from .views import Timesofindia, AbpRss, news18 , Bhaskar, Ndtv, allRss


urlpatterns = [
    path('timesofindia/', Timesofindia.as_view()),
    path('abpnews/', AbpRss.as_view()),
    path('news18/', news18.as_view()),
    path('bhaskar/', Bhaskar.as_view()),
    path('ndtv/', Ndtv.as_view()),
    path('allrss/', allRss.as_view()),
]

