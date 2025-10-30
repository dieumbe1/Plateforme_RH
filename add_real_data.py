#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestion_rh.settings')
django.setup()

from rh_app.models import *
from django.contrib.auth.models import User
from datetime import date, datetime, timedelta
from decimal import Decimal

# Créer les départements exacts de votre capture
departements_data = [
    {'nom': 'Ressources Humaines', 'description': 'Gestion du personnel et administration RH', 'budget_annuel': 5000000},
    {'nom': 'Informatique', 'description': 'Développement et maintenance informatique', 'budget_annuel': 8000000},
    {'nom': 'Comptabilité', 'description': 'Gestion financière et comptable', 'budget_annuel': 3000000},
    {'nom': 'Formation', 'description': 'Développement des compétences', 'budget_annuel': 4000000},
    {'nom': 'Administration', 'description': 'Administration générale', 'budget_annuel': 2000000},
]

print("🏢 Création des départements...")
for dept_data in departements_data:
    dept, created = Departement.objects.get_or_create(
        nom=dept_data['nom'],
        defaults=dept_data
    )
    if created:
        print(f"✅ Département créé: {dept.nom}")

# Créer les employés exacts de votre capture
employes_data = [
    {
        'username': 'marie.louise',
        'prenom': 'Marie Louise',
        'nom': 'Dhiédiou',
        'email': 'marie.louise@ecole.sn',
        'telephone': '77 123 45 67',
        'adresse': 'Dakar, Sénégal',
        'date_naissance': date(1985, 3, 15),
        'date_embauche': date(2020, 1, 15),
        'poste': 'Responsable RH',
        'role': 'RH',
        'departement': 'Ressources Humaines',
        'statut': 'ACTIF'
    },
    {
        'username': 'adama.ngom',
        'prenom': 'Adama',
        'nom': 'Ngom',
        'email': 'adama.ngom@ecole.sn',
        'telephone': '77 234 56 78',
        'adresse': 'Dakar, Sénégal',
        'date_naissance': date(1990, 7, 22),
        'date_embauche': date(2021, 3, 10),
        'poste': 'Développeur',
        'role': 'EMPLOYE',
        'departement': 'Informatique',
        'statut': 'ACTIF'
    },
    {
        'username': 'dieumbe.diop',
        'prenom': 'Dieumbe',
        'nom': 'Diop',
        'email': 'dieumbe.diop@ecole.sn',
        'telephone': '77 345 67 89',
        'adresse': 'Dakar, Sénégal',
        'date_naissance': date(1988, 11, 8),
        'date_embauche': date(2021, 6, 1),
        'poste': 'Comptable',
        'role': 'EMPLOYE',
        'departement': 'Comptabilité',
        'statut': 'ACTIF'
    },
    {
        'username': 'daba.ndour',
        'prenom': 'Daba',
        'nom': 'Ndour',
        'email': 'daba.ndour@ecole.sn',
        'telephone': '77 456 78 90',
        'adresse': 'Dakar, Sénégal',
        'date_naissance': date(1992, 4, 12),
        'date_embauche': date(2022, 2, 14),
        'poste': 'Formateur',
        'role': 'EMPLOYE',
        'departement': 'Formation',
        'statut': 'ACTIF'
    },
    {
        'username': 'aminata.diop',
        'prenom': 'Aminata',
        'nom': 'Diop',
        'email': 'aminata.diop@ecole.sn',
        'telephone': '77 567 89 01',
        'adresse': 'Dakar, Sénégal',
        'date_naissance': date(1987, 9, 25),
        'date_embauche': date(2020, 8, 20),
        'poste': 'Secrétaire',
        'role': 'EMPLOYE',
        'departement': 'Administration',
        'statut': 'ACTIF'
    }
]

print("\n👥 Création des employés...")
for emp_data in employes_data:
    # Créer l'utilisateur
    user, user_created = User.objects.get_or_create(
        username=emp_data['username'],
        defaults={
            'email': emp_data['email'],
            'first_name': emp_data['prenom'],
            'last_name': emp_data['nom']
        }
    )
    if user_created:
        user.set_password('password123')
        user.save()
    
    # Obtenir le département
    dept = Departement.objects.get(nom=emp_data['departement'])
    
    # Créer l'employé
    employe, emp_created = Employe.objects.get_or_create(
        user=user,
        defaults={
            'matricule': f"EMP{user.id:04d}",
            'prenom': emp_data['prenom'],
            'nom': emp_data['nom'],
            'email': emp_data['email'],
            'telephone': emp_data['telephone'],
            'adresse': emp_data['adresse'],
            'date_naissance': emp_data['date_naissance'],
            'date_embauche': emp_data['date_embauche'],
            'poste': emp_data['poste'],
            'role': emp_data['role'],
            'departement': dept,
            'statut': emp_data['statut']
        }
    )
    if emp_created:
        print(f"✅ Employé créé: {emp_data['prenom']} {emp_data['nom']} ({emp_data['poste']})")

# Créer des contrats pour chaque employé
print("\n📄 Création des contrats...")
contrats_data = [
    {'employe': 'marie.louise', 'type': 'CDI', 'salaire': 450000, 'date_debut': date(2020, 1, 15)},
    {'employe': 'adama.ngom', 'type': 'CDI', 'salaire': 350000, 'date_debut': date(2021, 3, 10)},
    {'employe': 'dieumbe.diop', 'type': 'CDI', 'salaire': 320000, 'date_debut': date(2021, 6, 1)},
    {'employe': 'daba.ndour', 'type': 'CDD', 'salaire': 300000, 'date_debut': date(2022, 2, 14), 'date_fin': date(2024, 2, 14)},
    {'employe': 'aminata.diop', 'type': 'CDI', 'salaire': 280000, 'date_debut': date(2020, 8, 20)},
]

for contrat_data in contrats_data:
    employe = Employe.objects.get(user__username=contrat_data['employe'])
    dept = employe.departement
    
    contrat, created = Contrat.objects.get_or_create(
        employe=employe,
        defaults={
            'type_contrat': contrat_data['type'],
            'date_debut': contrat_data['date_debut'],
            'date_fin': contrat_data.get('date_fin'),
            'salaire_base': contrat_data['salaire'],
            'poste': employe.poste,
            'departement': dept.nom,
            'statut': 'ACTIF'
        }
    )
    if created:
        print(f"✅ Contrat créé: {employe.get_full_name()} - {contrat.get_type_contrat_display()}")

# Créer des formations
print("\n🎓 Création des formations...")
formations_data = [
    {
        'titre': 'Formation Django Avancé',
        'description': 'Apprenez les concepts avancés de Django pour développer des applications web robustes.',
        'date_debut': date.today() + timedelta(days=30),
        'date_fin': date.today() + timedelta(days=33),
        'lieu': 'Salle de formation A',
        'formateur': 'Marie Martin',
        'capacite': 15,
        'statut': 'PROGRAMMEE'
    },
    {
        'titre': 'Gestion de Projet Agile',
        'description': 'Maîtrisez les méthodologies Agile et Scrum pour gérer vos projets efficacement.',
        'date_debut': date.today() + timedelta(days=45),
        'date_fin': date.today() + timedelta(days=46),
        'lieu': 'Salle de conférence B',
        'formateur': 'Pierre Durand',
        'capacite': 20,
        'statut': 'PROGRAMMEE'
    },
    {
        'titre': 'Communication Interpersonnelle',
        'description': 'Développez vos compétences en communication pour améliorer vos relations professionnelles.',
        'date_debut': date.today() + timedelta(days=60),
        'date_fin': date.today() + timedelta(days=61),
        'lieu': 'Salle de formation C',
        'formateur': 'Fatou Sall',
        'capacite': 12,
        'statut': 'PROGRAMMEE'
    }
]

for formation_data in formations_data:
    formation, created = Formation.objects.get_or_create(
        titre=formation_data['titre'],
        defaults=formation_data
    )
    if created:
        print(f"✅ Formation créée: {formation.titre}")

# Créer quelques demandes de congés
print("\n🏖️ Création des demandes de congés...")
conges_data = [
    {'employe': 'adama.ngom', 'type': 'ANNUEL', 'date_debut': date.today() + timedelta(days=15), 'nombre_jours': 5, 'motif': 'Vacances familiales'},
    {'employe': 'dieumbe.diop', 'type': 'MALADIE', 'date_debut': date.today() - timedelta(days=2), 'nombre_jours': 3, 'motif': 'Grippe'},
    {'employe': 'daba.ndour', 'type': 'ANNUEL', 'date_debut': date.today() + timedelta(days=30), 'nombre_jours': 10, 'motif': 'Congé d\'été'},
]

for conge_data in conges_data:
    employe = Employe.objects.get(user__username=conge_data['employe'])
    conge, created = Conge.objects.get_or_create(
        employe=employe,
        type_conge=conge_data['type'],
        date_debut=conge_data['date_debut'],
        defaults={
            'date_fin': conge_data['date_debut'] + timedelta(days=conge_data['nombre_jours']-1),
            'nombre_jours': conge_data['nombre_jours'],
            'motif': conge_data['motif'],
            'statut': 'EN_ATTENTE'
        }
    )
    if created:
        print(f"✅ Congé créé: {employe.get_full_name()} - {conge.get_type_conge_display()}")

print("\n🎉 Données créées avec succès!")
print("\n📋 Informations de connexion:")
print("  👤 Responsable RH - username: marie.louise, password: password123")
print("  👤 Employé - username: adama.ngom, password: password123")
print("  👤 Employé - username: dieumbe.diop, password: password123")
print("  👤 Employé - username: daba.ndour, password: password123")
print("  👤 Employé - username: aminata.diop, password: password123")
