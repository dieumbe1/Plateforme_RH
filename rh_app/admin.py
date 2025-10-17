from django.contrib import admin
from .models import Employe, Formation, InscriptionFormation, Conge, Contrat, Salaire, Presence

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ['matricule', 'nom', 'prenom', 'poste', 'role', 'statut', 'date_embauche']
    list_filter = ['role', 'statut', 'departement']
    search_fields = ['matricule', 'nom', 'prenom', 'email']
    ordering = ['nom', 'prenom']

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ['titre', 'date_debut', 'date_fin', 'formateur', 'capacite', 'statut']
    list_filter = ['statut', 'date_debut']
    search_fields = ['titre', 'formateur']
    ordering = ['-date_debut']

@admin.register(InscriptionFormation)
class InscriptionFormationAdmin(admin.ModelAdmin):
    list_display = ['employe', 'formation', 'date_inscription', 'statut']
    list_filter = ['statut', 'date_inscription']
    search_fields = ['employe__nom', 'employe__prenom', 'formation__titre']
    ordering = ['-date_inscription']

@admin.register(Conge)
class CongeAdmin(admin.ModelAdmin):
    list_display = ['employe', 'type_conge', 'date_debut', 'date_fin', 'nombre_jours', 'statut']
    list_filter = ['type_conge', 'statut', 'date_debut']
    search_fields = ['employe__nom', 'employe__prenom']
    ordering = ['-date_demande']

@admin.register(Contrat)
class ContratAdmin(admin.ModelAdmin):
    list_display = ['employe', 'type_contrat', 'date_debut', 'date_fin', 'salaire_base', 'statut']
    list_filter = ['type_contrat', 'statut']
    search_fields = ['employe__nom', 'employe__prenom']
    ordering = ['-date_debut']

@admin.register(Salaire)
class SalaireAdmin(admin.ModelAdmin):
    list_display = ['employe', 'mois', 'annee', 'salaire_base', 'salaire_net', 'date_paiement']
    list_filter = ['annee', 'mois']
    search_fields = ['employe__nom', 'employe__prenom']
    ordering = ['-annee', '-mois']

@admin.register(Presence)
class PresenceAdmin(admin.ModelAdmin):
    list_display = ['employe', 'date', 'heure_arrivee', 'heure_depart', 'statut']
    list_filter = ['statut', 'date']
    search_fields = ['employe__nom', 'employe__prenom']
    ordering = ['-date']
