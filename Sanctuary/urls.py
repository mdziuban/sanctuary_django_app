from . import views
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from . views import Images, PlayerList, PlayerDetails, PostList, PlayerUpdate, PostDetail, PostLike, ReplyList, ReplyAdd, ReplyDetail, GameDataList, GameDataDetail, Register

urlpatterns = [
    path('player/', PlayerList.as_view(), name='player_list'),
    path('post/', PostList.as_view(), name='post_list'),
    path('reply/', ReplyList.as_view(), name='reply_list'),
    path('replyadd/', ReplyAdd.as_view(), name='reply_add'),
    path('images/', Images.as_view(), name='images'),
    path('gamedata/', GameDataList.as_view(), name='game_data'),
    path('player/<int:pk>', PlayerDetails.as_view(), name='player_details'),
    path('update/<int:pk>', PlayerUpdate.as_view(), name='player_update'),
    path('postdetail/', PostDetail.as_view(), name='post_details'),
    path('postlike/<int:pk>', PostLike.as_view(), name="post_like"),
    path('reply/<int:pk>', ReplyDetail.as_view(), name='reply_details'),
    path('gamedata/<int:user_id>', GameDataDetail.as_view(), name='game_data_details'),
    path('register/', Register.as_view(), name='register'),
    path('playgame/', views.playGame),

    path('api-token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api-token-refresh/', TokenRefreshView.as_view(), name='token_refresh')
] 