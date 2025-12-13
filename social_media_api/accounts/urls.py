# accounts/urls.py
from django.urls import path
from .views import RegisterView, LoginView, ProfileView, FollowView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', FollowView.as_view(), name='follow'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('following/', MyFollowingListView.as_view(), name='my-following'),
    path('followers/', MyFollowersListView.as_view(), name='my-followers'),
]

]