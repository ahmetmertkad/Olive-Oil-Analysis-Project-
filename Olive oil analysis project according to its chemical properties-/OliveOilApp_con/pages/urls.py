from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 
from django.contrib import admin

urlpatterns = [
    path('',views.index, name="index"),
    path('styles/',views.styles, name="styles"),
    path('search/', views.search, name='search'),
    path('table/', views.table, name='table'),
    path('user/', views.user, name='user'),
    path('logout/', views.logout_user, name='logout'),
    path('change-password/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('', views.user_oils_view, name='user_oils_view'),
    path('delete-oil/<int:oil_id>/', views.delete_oil, name='delete_oil'),
    path('admin/', admin.site.urls),
    path('export_olive_oil/', views.export_olive_oil_to_excel, name='export_olive_oil'),
    ]