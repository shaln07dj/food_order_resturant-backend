from django.urls import path

from resturantdata.views import user_views as views


urlpatterns=[
      
     path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

     path('register/',views.registerUser.as_view(),name="register"),

    
     path('profile/', views.getUserProfile.as_view(),name="user-profile"),

     path('', views.getUsers.as_view()),
    
]