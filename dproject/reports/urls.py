from django.urls import path, include

urlpatterns = [
    path('', include('reports.api.urls')),
]