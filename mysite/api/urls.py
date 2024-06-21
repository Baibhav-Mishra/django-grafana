from . import views
from django.urls import path

#URLConf
urlpatterns = [
    path('data/<str:var>', views.page),
    path('list/<str:var>', views.list_query)
]