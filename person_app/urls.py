from django.urls import path
from .views import CreatePersonView, RetrievePersonView

urlpatterns = [
    path('', CreatePersonView.as_view(), name='create_person'),
    path('<int:pk>/', RetrievePersonView.as_view(), name='retrieve_person'),
]

