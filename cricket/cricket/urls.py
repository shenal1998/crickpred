from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('edit_profile/', user_views.edit_profile, name='edit_profile'),
    path('batsman_list/<int:runs_id>/delete', user_views.runs_delete,name='runs_delete'),
    path('batsman_list/', user_views.runs_list, name='runs_list'),
    path('batsman_runs/', user_views.runs_form, name='runs_form'),
    path('bowlers_list/<int:wickets_id>/delete', user_views.wickets_delete,name='wickets_delete'),
    path('bowlers_list/', user_views.wickets_list, name='wickets_list'),
    path('bowlers_wickets/', user_views.wickets_form, name='wickets_form'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('',include('webfront.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
