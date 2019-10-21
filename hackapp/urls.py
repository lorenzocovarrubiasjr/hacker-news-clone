from django.contrib.auth import views
from django.urls import path
from django.contrib.auth import views as user_views
from . import views


urlpatterns = [
    path('signup/', views.signUp, name='signup'),
    path('login/', user_views.LoginView.as_view(template_name="hackapp/login.html"), name="login"),
    path('home/', views.view_post, name="home"),
    path('newest/', views.newest, name='newest'),
    path('newestcomments/', views.newest_comments, name='newestcomments'),
    path('welcome/', views.welcome, name='welcome'),
    path('post/create_post/', views.create_post, name='create_post'), 
    path('post/create_post_action/', views.create_post_action, name='create_post_action'),
    path('post/<post_id>/', views.view_one_post, name='view_post'),
    path('post/<post_id>/delete_post/', views.delete_post, name='delete_post'),
    path('post/<post_id>/delete_post_action/', views.delete_post_action, name='delete_post_action'),
    path('logout/', user_views.LogoutView.as_view(template_name="hackapp/logout.html"), name="logout"),
    path('accounts/profile/', views.profile, name='profile'),
    path('post/<post_id>/create_comment', views.create_comment, name='create_comment'),
    path('', views.redirect_home, name='redirect_home')
    #path('user/view/<user_id>', views.view_user, name='view'),
    #path('user/delete_user', views.delete_user, name='delete_user'),
    #path('post/<post_id>/edit', views.edit_post, name='edit_post'),
    # path('post/<post_id>', views.view_post, name='view_post'),
    # path('post/<post_id>/edit', views.edit_post, name='edit_post'),
]