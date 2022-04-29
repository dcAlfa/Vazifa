
from django.contrib import admin
from django.urls import path
from todoapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', asosiy),
    path('studentlar/', student),
    path('rejalar/', project),
    path('reja/<int:son>/', reja_o),
]
