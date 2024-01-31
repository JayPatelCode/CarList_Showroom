from django.urls import path
from .views import *

urlpatterns=[
    path('list/',car_list_view,name="car_list"),
    path('<int:pk>',car_detail_view,name="car_detail"),
    path('showroom/',showroom_view.as_view(),name="showroom_view"),
    path('showroom/<int:pk>',showroom_detail_view.as_view(),name='showroom_details')
]