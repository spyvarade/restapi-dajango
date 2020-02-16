from django.urls import path
from .views import article_list, aritcle_detail

urlpatterns = [
    path('article/',article_list),
    path('detail/<int:pk>/',aritcle_detail)

]
