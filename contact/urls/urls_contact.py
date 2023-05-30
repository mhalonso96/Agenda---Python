from django.urls import path
from contact import views

app_name = 'contact'
urlpatterns = [
    path('', views.index, name= 'index'),
    path('search/', views.search, name= 'search'),

    # Contact (CRUD) -> (C)reate, (R)ead, (U)pdate, (D)elete
    path('contact/<int:contact_id>/detail/', views.contact, name= 'contact'),
    path('contact/create/', views.create, name= 'create',),
    path('contact/<int:contact_id>/update/', views.update, name= 'update'),
    path('contact/<int:contact_id>/delete/', views.delete, name= 'delete'),

    #Register user (CRU)
    path('user/create/', views.register, name= 'register'),
    path('user/login/', views.login_view, name = 'login'),
    path('user/logout/', views.logout_view, name = 'logout'),
    path('user/update', views.user_update, name='user_update')
  
]
 