from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='home_page'),
    path('homepage_week', views.homepageweek, name='home_page_week'),
    path('homepage_late', views.homepagelate, name='home_page_late'),

    path('list_clients', views.list_clients, name='list_clients'),
    path('list_deals', views.list_deals, name='list_deals'),
    path('list_calls', views.list_calls, name='list_calls'),
    path('list_reminders', views.list_reminders, name='list_reminders'),

    path('create_client', views.create_client, name='create_client'),
    path('create_call', views.create_call, name='create_call'),
    path('create_deal', views.create_deal, name='create_deal'),
    path('create_reminder', views.create_reminder, name='create_reminder'),

    path('detail_call/<int:pk>', views.DetailCall.as_view(), name='detailed_call'),
    path('detail_client/<int:pk>', views.DetailClient.as_view(), name='detailed_client'),
    path('detail_deal/<int:pk>', views.DetailDeal.as_view(), name='detailed_deal'),
    path('detail_reminder/<int:pk>', views.DetailReminder.as_view(), name='detailed_reminder'),

    path('update_client/<int:pk>', views.ClientUpdate.as_view(), name='update_client'),
    path('update_call/<int:pk>', views.CallUpdate.as_view(), name='update_call'),
    path('update_deal/<int:pk>', views.DealUpdate.as_view(), name='update_deal'),
    path('update_reminder/<int:pk>', views.ReminderUpdate.as_view(), name='update_reminder'),

    path('delete_call/<int:pk>', views.CallDelete.as_view(), name='delete_call'),
    path('delete_deal/<int:pk>', views.DealDelete.as_view(), name='delete_deal'),
    path('delete_reminder/<int:pk>', views.ReminderDelete.as_view(), name='delete_reminder'),

    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]