from django.urls import path
from .views import home, atualizar, deletar, detalhado

urlpatterns = [ 
    path('', home), 
    path('atualizar/<str:id>/', atualizar, name="atualizar"),
    path('deletar/<str:id>/', deletar, name="deletar"),
    path('detalhado/', detalhado, name='detalhado')
]