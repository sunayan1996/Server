from django.conf.urls import include, url
from . import views

urlpatterns = [
    
    url( r'^$' , views.index , name='index' ),
    url( r'^farmerdetail/' , views.farmerdetail , name='farmerdetail' ),
    url( r'^landlorddetail/' , views.landlorddetail , name='landlorddetail' ),
]

