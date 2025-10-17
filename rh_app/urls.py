from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('connexion/', views.connexion, name='login'),
    path('deconnexion/', views.deconnexion, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/rh/', views.dashboard_rh, name='dashboard_rh'),
    path('dashboard/employe/', views.dashboard_employe, name='dashboard_employe'),
    
    path('employes/', views.liste_employes, name='liste_employes'),
    path('employes/ajouter/', views.ajouter_employe, name='ajouter_employe'),
    path('employes/<int:pk>/', views.detail_employe, name='detail_employe'),
    path('employes/<int:pk>/modifier/', views.modifier_employe, name='modifier_employe'),
    
    path('formations/', views.liste_formations, name='liste_formations'),
    path('formations/ajouter/', views.ajouter_formation, name='ajouter_formation'),
    path('formations/<int:pk>/', views.detail_formation, name='detail_formation'),
    path('formations/<int:pk>/modifier/', views.modifier_formation, name='modifier_formation'),
    path('formations/<int:pk>/inscrire/', views.inscrire_formation, name='inscrire_formation'),
    
    path('conges/', views.liste_conges, name='liste_conges'),
    path('conges/demander/', views.demander_conge, name='demander_conge'),
    path('conges/<int:pk>/traiter/', views.traiter_conge, name='traiter_conge'),
    
    path('contrats/', views.liste_contrats, name='liste_contrats'),
    path('contrats/ajouter/', views.ajouter_contrat, name='ajouter_contrat'),
    
    path('salaires/', views.liste_salaires, name='liste_salaires'),
    path('salaires/ajouter/', views.ajouter_salaire, name='ajouter_salaire'),
    
    path('presences/', views.liste_presences, name='liste_presences'),
    path('presences/ajouter/', views.ajouter_presence, name='ajouter_presence'),
]
