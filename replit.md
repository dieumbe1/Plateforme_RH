# Application de Gestion des Ressources Humaines (RH)

## Vue d'ensemble

Application web complète de gestion RH développée avec Django 5.2.7, permettant la gestion des employés, formations, congés, contrats, salaires et présences. Interface en français avec design moderne utilisant Bootstrap 5.

## État actuel du projet

✅ **Projet opérationnel** - Dernière mise à jour: 17 octobre 2025

### Fonctionnalités implémentées

#### Système d'authentification
- Deux types d'utilisateurs: Responsable RH et Employé
- Login/logout sécurisé
- Redirections automatiques selon le rôle

#### Module Responsable RH
- **Gestion des employés**: CRUD complet (Créer, Lire, Modifier)
- **Gestion des formations**: Création et suivi des formations
- **Gestion des congés**: Validation/refus des demandes
- **Gestion des contrats**: Suivi des contrats employés
- **Gestion des salaires**: Enregistrement des bulletins de paie
- **Gestion des présences**: Suivi des jours de travail

#### Module Employé
- Consultation du dossier personnel
- Consultation des salaires et bulletins
- Demande de congés
- Inscription aux formations disponibles
- Consultation de la présence

### Architecture technique

#### Backend
- **Framework**: Django 5.2.7
- **Base de données**: SQLite (development)
- **Authentification**: Django Auth System
- **Langues**: Français (fr-fr)
- **Timezone**: Europe/Paris

#### Frontend
- **Framework CSS**: Bootstrap 5.3.0
- **Icons**: Bootstrap Icons
- **Responsive**: Mobile-first design
- **Templates**: Django Templates

#### Structure du projet
```
gestion_rh/
├── gestion_rh/          # Configuration du projet
│   ├── settings.py      # Configuration Django
│   ├── urls.py          # URLs principales
│   └── wsgi.py
├── rh_app/              # Application principale
│   ├── models.py        # Modèles de données
│   ├── views.py         # Vues et logique métier
│   ├── forms.py         # Formulaires Django
│   ├── urls.py          # URLs de l'application
│   ├── admin.py         # Interface admin
│   ├── templates/       # Templates HTML
│   │   ├── base.html
│   │   └── rh_app/
│   │       ├── accueil.html
│   │       ├── connexion.html
│   │       ├── dashboard_rh.html
│   │       ├── dashboard_employe.html
│   │       └── [modules]/
│   └── management/
│       └── commands/
│           └── init_data.py
├── static/              # Fichiers statiques
├── media/               # Fichiers uploadés
└── manage.py
```

### Modèles de données

1. **Employe**: Profil employé avec rôle (RH/Employé)
2. **Formation**: Formations disponibles avec capacité
3. **InscriptionFormation**: Inscriptions des employés aux formations
4. **Conge**: Demandes de congés avec validation
5. **Contrat**: Contrats de travail (CDI, CDD, etc.)
6. **Salaire**: Bulletins de paie mensuels
7. **Presence**: Suivi des présences quotidiennes

### Configuration serveur

- **Port**: 5000
- **Host**: 0.0.0.0 (accessible depuis Replit)
- **Workflow**: `python manage.py runserver 0.0.0.0:5000`

## Guide d'utilisation

### Première utilisation

1. **Initialiser les données de test**:
```bash
python manage.py init_data
```

2. **Comptes de test créés**:
   - **Responsable RH**: 
     - Username: `admin`
     - Password: `admin123`
   - **Employé**: 
     - Username: `employe1`
     - Password: `employe123`

3. **Accéder à l'application**:
   - Cliquer sur "Run" ou ouvrir le port 5000
   - Se connecter avec les identifiants ci-dessus

### Interface Admin Django

Accès: `/admin`
- Créer un superuser: `python manage.py createsuperuser`
- Gestion complète de tous les modèles

### Fonctionnalités par rôle

#### Responsable RH
- Gérer tous les employés (ajout, modification, consultation)
- Créer et gérer les formations
- Valider ou refuser les demandes de congés
- Enregistrer les contrats et salaires
- Suivre les présences

#### Employé
- Consulter son dossier personnel
- Visualiser ses salaires
- Demander des congés
- S'inscrire aux formations disponibles
- Consulter son historique de présence

## Changements récents

### 17 octobre 2025
- ✅ Création complète du projet Django
- ✅ Implémentation des 7 modèles de données
- ✅ Système d'authentification avec 2 rôles
- ✅ Interfaces RH et Employé
- ✅ Design moderne avec Bootstrap 5
- ✅ Script d'initialisation des données
- ✅ Templates pour tous les modules
- ✅ Configuration du workflow sur port 5000

## Préférences de développement

- **Langue**: Français (interface et code)
- **Style de code**: PEP 8 pour Python
- **Base de données**: SQLite pour développement
- **Design**: Bootstrap 5, moderne et responsive
- **Architecture**: MVT (Model-View-Template) Django

## Prochaines étapes recommandées

1. **Notifications**: Système d'alertes pour les validations
2. **Rapports**: Génération de statistiques et graphiques
3. **Export**: PDF pour bulletins de paie et documents
4. **Pointage**: Module de pointage automatique
5. **Documents**: Upload et gestion de documents RH

## Commandes utiles

```bash
# Démarrer le serveur
python manage.py runserver 0.0.0.0:5000

# Créer les migrations
python manage.py makemigrations

# Appliquer les migrations
python manage.py migrate

# Initialiser les données de test
python manage.py init_data

# Créer un superuser
python manage.py createsuperuser

# Collecter les fichiers statiques
python manage.py collectstatic
```

## Support et dépannage

### Problèmes courants

1. **Erreur de migration**: 
   ```bash
   python manage.py migrate --run-syncdb
   ```

2. **Port déjà utilisé**: Le serveur utilise le port 5000 (configuré pour Replit)

3. **Fichiers statiques non chargés**: 
   ```bash
   python manage.py collectstatic
   ```

## Notes techniques

- Tous les mots de passe par défaut sont simples pour le développement
- Les erreurs LSP dans models.py sont normales (type checking Django ORM)
- Le serveur utilise le mode DEBUG=True (development only)
- Les fichiers médias sont stockés dans `/media`
