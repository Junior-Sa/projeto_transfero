from django.urls import path
from sistema import views

# informa qual sera a rota que ira chamr determinada view(funçao)
urlpatterns = [
    path('sistema/', views.index),
]
