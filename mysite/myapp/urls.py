from django.urls import path

from myapp.views import index, indexItem
from django.contrib.auth.views import LoginView, LogoutView

from myapp.views import register, profile_view

from myapp.views import add_item, update_item, delete_item

app_name = "myapp"

urlpatterns = [
    path("", index, name="index"),
    path("<int:my_id>/", indexItem, name="detail"),
    path("additem/", add_item, name="add_item"),
    path("updateitem/<int:my_id>/", update_item, name="update_item"),
    path("deleteitem/<int:my_id>/", delete_item, name="delete_item"),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='myapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='myapp/logout.html'), name='logout'),
    path('profile/', profile_view, name='profile'),

]