from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'articles'


urlpatterns = [
    url(r'^$', views.homepage, name="list"),
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^hotelReview/$', views.hotelReview, name="hotelReview"),
    url(r'^hotelReviewShow/$', views.hotelReviewShow, name="hotelReviewShow"),
    path('deleteHotelReview/<str:pk>/$', views.deleteHotelReview, name="deleteHotelReview"),
    url(r'^resturantReview/$', views.resturantReview, name="resturantReview"),
    url(r'^resturantReviewShow/$', views.resturantReviewShow, name="resturantReviewShow"),
    path('deleteResturantReview/<str:pk>/$', views.deleteresturantReview, name="deleteResturantReview"),


    url(r'^hotel_booking/$', views.hotel_booking, name="hotel_booking"),
    path('hotel_bookingPdf', views.hotel_bookingPdf, name="hotel_bookingPdf"),

]
