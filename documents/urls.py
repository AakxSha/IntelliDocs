from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    
    
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('upload/', views.upload_document, name='upload_document'),
    path('documents/', views.list_documents, name='list_documents'),
    path('search/', views.search_documents, name='search_documents'),
    path('documents/delete/<int:document_id>/', views.delete_document, name='delete_document'),

]
