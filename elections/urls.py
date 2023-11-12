from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'), 
    path('signin/', views.signin, name='signin'),            
    path('logout/', views.custom_logout, name='logout'),         
    path('update_profile/', views.update_profile, name='update_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('view-elections/', views.view_elections, name='view_elections'),
    path('view-candidates/<int:election_id>/', views.view_candidates, name='view_candidates'),
    path('cast-vote/<int:election_id>/<int:candidate_id>/', views.cast_vote, name='cast_vote'),
    path('election-results/', views.election_results, name='election_results'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
