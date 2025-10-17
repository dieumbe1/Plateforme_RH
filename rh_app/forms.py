from django import forms
from .models import Employe, Formation, InscriptionFormation, Conge, Contrat, Salaire, Presence

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label='Nom d\'utilisateur',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'})
    )
    password = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'})
    )

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        exclude = ['user']
        widgets = {
            'matricule': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_embauche': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'poste': forms.TextInput(attrs={'class': 'form-control'}),
            'departement': forms.TextInput(attrs={'class': 'form-control'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = '__all__'
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'lieu': forms.TextInput(attrs={'class': 'form-control'}),
            'formateur': forms.TextInput(attrs={'class': 'form-control'}),
            'capacite': forms.NumberInput(attrs={'class': 'form-control'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
        }

class InscriptionFormationForm(forms.ModelForm):
    class Meta:
        model = InscriptionFormation
        fields = ['formation', 'note']
        widgets = {
            'formation': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class CongeForm(forms.ModelForm):
    class Meta:
        model = Conge
        fields = ['type_conge', 'date_debut', 'date_fin', 'nombre_jours', 'motif']
        widgets = {
            'type_conge': forms.Select(attrs={'class': 'form-control'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'nombre_jours': forms.NumberInput(attrs={'class': 'form-control'}),
            'motif': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class ContratForm(forms.ModelForm):
    class Meta:
        model = Contrat
        fields = '__all__'
        widgets = {
            'employe': forms.Select(attrs={'class': 'form-control'}),
            'type_contrat': forms.Select(attrs={'class': 'form-control'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'date_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'salaire_base': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'poste': forms.TextInput(attrs={'class': 'form-control'}),
            'departement': forms.TextInput(attrs={'class': 'form-control'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
            'document': forms.FileInput(attrs={'class': 'form-control'}),
        }

class SalaireForm(forms.ModelForm):
    class Meta:
        model = Salaire
        exclude = ['salaire_net']
        widgets = {
            'employe': forms.Select(attrs={'class': 'form-control'}),
            'mois': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 12}),
            'annee': forms.NumberInput(attrs={'class': 'form-control'}),
            'salaire_base': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'primes': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'deductions': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'date_paiement': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'bulletin': forms.FileInput(attrs={'class': 'form-control'}),
        }

class PresenceForm(forms.ModelForm):
    class Meta:
        model = Presence
        exclude = ['date_creation']
        widgets = {
            'employe': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'heure_arrivee': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'heure_depart': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'statut': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
