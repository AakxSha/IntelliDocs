from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    
    path('accounts/logout/', views.custom_logout, name='logout'),

    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('accounts/register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('upload/', views.upload_document, name='upload_document'),
    path('documents/', views.list_documents, name='list_documents'),
    path('search/', views.search_documents, name='search_documents'),
    path('documents/delete/<int:document_id>/', views.delete_document, name='delete_document'),

]
