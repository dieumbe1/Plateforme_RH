from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q, Count
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Employe, Formation, InscriptionFormation, Conge, Contrat, Salaire, Presence
from .forms import (
    LoginForm, EmployeForm, FormationForm, CongeForm, 
    ContratForm, SalaireForm, PresenceForm, InscriptionFormationForm
)

def accueil(request):
    return render(request, 'rh_app/accueil.html')

def connexion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    else:
        form = LoginForm()
    return render(request, 'rh_app/connexion.html', {'form': form})

@login_required
def deconnexion(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté avec succès.')
    return redirect('accueil')

@login_required
def dashboard(request):
    try:
        employe = request.user.employe
        if employe.role == 'RH':
            return redirect('dashboard_rh')
        else:
            return redirect('dashboard_employe')
    except Employe.DoesNotExist:
        messages.error(request, 'Profil employé non trouvé.')
        return redirect('accueil')

@login_required
def dashboard_rh(request):
    employe = request.user.employe
    if employe.role != 'RH':
        messages.error(request, 'Accès non autorisé.')
        return redirect('dashboard_employe')
    
    employes = Employe.objects.all()
    conges_en_attente = Conge.objects.filter(statut='EN_ATTENTE').count()
    formations = Formation.objects.all()
    
    context = {
        'employe': employe,
        'total_employes': employes.count(),
        'conges_en_attente': conges_en_attente,
        'total_formations': formations.count(),
        'employes_recents': employes.order_by('-date_embauche')[:5],
    }
    return render(request, 'rh_app/dashboard_rh.html', context)

@login_required
def dashboard_employe(request):
    employe = request.user.employe
    
    mes_conges = Conge.objects.filter(employe=employe).order_by('-date_demande')[:5]
    mes_formations = InscriptionFormation.objects.filter(employe=employe).order_by('-date_inscription')[:5]
    mes_presences = Presence.objects.filter(employe=employe).order_by('-date')[:10]
    mon_dernier_salaire = Salaire.objects.filter(employe=employe).first()
    
    context = {
        'employe': employe,
        'mes_conges': mes_conges,
        'mes_formations': mes_formations,
        'mes_presences': mes_presences,
        'mon_dernier_salaire': mon_dernier_salaire,
    }
    return render(request, 'rh_app/dashboard_employe.html', context)

@login_required
def liste_employes(request):
    employe = request.user.employe
    if employe.role != 'RH':
        messages.error(request, 'Accès non autorisé.')
        return redirect('dashboard')
    
    employes = Employe.objects.all()
    context = {'employes': employes}
    return render(request, 'rh_app/employes/liste.html', context)

@login_required
def ajouter_employe(request):
    employe = request.user.employe
    if employe.role != 'RH':
        messages.error(request, 'Accès non autorisé.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = EmployeForm(request.POST, request.FILES)
        if form.is_valid():
            employe_obj = form.save(commit=False)
            user = User.objects.create_user(
                username=form.cleaned_data['matricule'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['prenom'],
                last_name=form.cleaned_data['nom'],
                password='motdepasse123'
            )
            employe_obj.user = user
            employe_obj.save()
            messages.success(request, f'Employé {employe_obj.get_full_name()} ajouté avec succès.')
            return redirect('liste_employes')
    else:
        form = EmployeForm()
    
    return render(request, 'rh_app/employes/form.html', {'form': form, 'action': 'Ajouter'})

@login_required
def modifier_employe(request, pk):
    employe = request.user.employe
    if employe.role != 'RH':
        messages.error(request, 'Accès non autorisé.')
        return redirect('dashboard')
    
    employe_obj = get_object_or_404(Employe, pk=pk)
    
    if request.method == 'POST':
        form = EmployeForm(request.POST, request.FILES, instance=employe_obj)
        if form.is_valid():
            form.save()
            messages.success(request, f'Employé {employe_obj.get_full_name()} modifié avec succès.')
            return redirect('liste_employes')
    else:
        form = EmployeForm(instance=employe_obj)
    
    return render(request, 'rh_app/employes/form.html', {'form': form, 'action': 'Modifier'})

@login_required
def detail_employe(request, pk):
    employe = request.user.employe
    employe_obj = get_object_or_404(Employe, pk=pk)
    
    if employe.role != 'RH' and employe != employe_obj:
        messages.error(request, 'Accès non autorisé.')
        return redirect('dashboard')
    
    contrats = employe_obj.contrats.all()
    conges = employe_obj.conges.all()
    salaires = employe_obj.salaires.all()[:6]
    
    context = {
        'employe_obj': employe_obj,
        'contrats': contrats,
        'conges': conges,
        'salaires': salaires,
    }
    return render(request, 'rh_app/employes/detail.html', context)

@login_required
def liste_formations(request):
    formations = Formation.objects.all()
    context = {'formations': formations}
    return render(request, 'rh_app/formations/liste.html', context)

@login_required
def ajouter_formation(request):
    employe = request.user.employe
    if employe.role != 'RH':
        messages.error(request, 'Accès non autorisé.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = FormationForm(request.POST)
        if form.is_valid():
            formation = form.save()
            messages.success(request, f'Formation "{formation.titre}" ajoutée avec succès.')
            return redirect('liste_formations')
    else:
        form = FormationForm()
    
    return render(request, 'rh_app/formations/form.html', {'form': form, 'action': 'Ajouter'})

@login_required
def modifier_formation(request, pk):
    employe = request.user.employe
    if employe.role != 'RH':
        messages.error(request, 'Accès non autorisé.')
        return redirect('dashboard')
    
    formation = get_object_or_404(Formation, pk=pk)
    
    if request.method == 'POST':
        form = FormationForm(request.POST, instance=formation)
        if form.is_valid():
            form.save()
            messages.success(request, f'Formation "{formation.titre}" modifiée avec succès.')
            return redirect('liste_formations')
    else:
        form = FormationForm(instance=formation)
    
    return render(request, 'rh_app/formations/form.html', {'form': form, 'action': 'Modifier'})

@login_required
def detail_formation(request, pk):
    formation = get_object_or_404(Formation, pk=pk)
    inscriptions = formation.inscriptions.all()
    
    employe = request.user.employe
    est_inscrit = InscriptionFormation.objects.filter(employe=employe, formation=formation).exists()
    
    context = {
        'formation': formation,
        'inscriptions': inscriptions,
        'est_inscrit': est_inscrit,
        'places_disponibles': formation.places_disponibles(),
    }
    return render(request, 'rh_app/formations/detail.html', context)

@login_required
def inscrire_formation(request, pk):
    formation = get_object_or_404(Formation, pk=pk)
    employe = request.user.employe
    
    if InscriptionFormation.objects.filter(employe=employe, formation=formation).exists():
        messages.warning(request, 'Vous êtes déjà inscrit à cette formation.')
    elif formation.places_disponibles() <= 0:
        messages.error(request, 'Cette formation est complète.')
    else:
        InscriptionFormation.objects.create(employe=employe, formation=formation)
        messages.success(request, f'Inscription à la formation "{formation.titre}" enregistrée.')
    
    return redirect('detail_formation', pk=pk)

@login_required
def liste_conges(request):
    employe = request.user.employe
    
    if employe.role == 'RH':
        conges = Conge.objects.all()
    else:
        conges = Conge.objects.filter(employe=employe)
    
    context = {'conges': conges}
    return render(request, 'rh_app/conges/liste.html', context)

@login_required
def demander_conge(request):
    if request.method == 'POST':
        form = CongeForm(request.POST)
        if form.is_valid():
            conge = form.save(commit=False)
            conge.employe = request.user.employe
            conge.save()
            messages.success(request, 'Votre demande de congé a été enregistrée.')
            return redirect('liste_conges')
    else:
        form = CongeForm()
    
    return render(request, 'rh_app/conges/form.html', {'form': form, 'action': 'Demander'})

@login_required
def traiter_conge(request, pk):
    employe = request.user.employe
    if employe.role != 'RH':
        messages.error(request, 'Accès non autorisé.')
        return redirect('dashboard')
    
    conge = get_object_or_404(Conge, pk=pk)
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action in ['APPROUVE', 'REFUSE']:
            conge.statut = action
            conge.date_reponse = timezone.now()
            conge.commentaire_rh = request.POST.get('commentaire', '')
            conge.save()
            messages.success(request, f'Congé {action.lower()}.')
            return redirect('liste_conges')
    
    context = {'conge': conge}
    return render(request, 'rh_app/conges/traiter.html', context)

@login_required
def liste_contrats(request):
    employe = request.user.employe
    
    if employe.role == 'RH':
        contrats = Contrat.objects.all()
    else:
        contrats = Contrat.objects.filter(employe=employe)
    
    context = {'contrats': contrats}
    return render(request, 'rh_app/contrats/liste.html', context)

@login_required
def ajouter_contrat(request):
    employe = request.user.employe
    if employe.role != 'RH':
        messages.error(request, 'Accès non autorisé.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = ContratForm(request.POST, request.FILES)
        if form.is_valid():
            contrat = form.save()
            messages.success(request, f'Contrat pour {contrat.employe.get_full_name()} ajouté avec succès.')
            return redirect('liste_contrats')
    else:
        form = ContratForm()
    
    return render(request, 'rh_app/contrats/form.html', {'form': form, 'action': 'Ajouter'})

@login_required
def liste_salaires(request):
    employe = request.user.employe
    
    if employe.role == 'RH':
        salaires = Salaire.objects.all()
    else:
        salaires = Salaire.objects.filter(employe=employe)
    
    context = {'salaires': salaires}
    return render(request, 'rh_app/salaires/liste.html', context)

@login_required
def ajouter_salaire(request):
    employe = request.user.employe
    if employe.role != 'RH':
        messages.error(request, 'Accès non autorisé.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = SalaireForm(request.POST, request.FILES)
        if form.is_valid():
            salaire = form.save()
            messages.success(request, f'Salaire pour {salaire.employe.get_full_name()} ajouté avec succès.')
            return redirect('liste_salaires')
    else:
        form = SalaireForm()
    
    return render(request, 'rh_app/salaires/form.html', {'form': form, 'action': 'Ajouter'})

@login_required
def liste_presences(request):
    employe = request.user.employe
    
    if employe.role == 'RH':
        presences = Presence.objects.all()[:100]
    else:
        presences = Presence.objects.filter(employe=employe)[:50]
    
    context = {'presences': presences}
    return render(request, 'rh_app/presences/liste.html', context)

@login_required
def ajouter_presence(request):
    employe = request.user.employe
    if employe.role != 'RH':
        messages.error(request, 'Accès non autorisé.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = PresenceForm(request.POST)
        if form.is_valid():
            presence = form.save()
            messages.success(request, f'Présence pour {presence.employe.get_full_name()} ajoutée.')
            return redirect('liste_presences')
    else:
        form = PresenceForm()
    
    return render(request, 'rh_app/presences/form.html', {'form': form, 'action': 'Ajouter'})
