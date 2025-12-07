
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/',views.accueil, name='dashboard'),
    path('animaux/',views.dashboard, name='animaux'),
    path('profil/',views.dashboard, name='profil'),
    path('visites/',views.dashboard, name='visites'),
    path('soigneurs/',views.dashboard, name='soigneurs'),

]

urlpatterns += [
    path('animal/add/', views.add_animal, name='add_animal'),
    path('animal/edit/<int:id>/', views.edit_animal, name='edit_animal'),
    path('animal/delete/<int:id>/', views.delete_animal, name='delete_animal'),
]

