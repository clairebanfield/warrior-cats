from django import forms
from .models import Clan

HILLS = 'H'
PINES = 'P'
GORGE = 'G'
MOOR = 'M'
RIVER = 'R'
LAKE = 'L'
FOREST = 'F'
HABITAT_CHOICES =(
    (HILLS, 'Hills'),
    (PINES, 'Pines'),
    (GORGE, 'Gorge'),
    (MOOR, 'Moor'),
    (RIVER, 'River'),
    (LAKE, 'Lake'),
    (FOREST, 'Forest'),
    )

LEADER = 'LD'
DEPUTY = 'DY'
WARRIOR =  'WR'
APPRENTICE = 'AP'
MEDICINE_CAT = 'MC'
MEDICINE_CAT_APPRENTICE = 'MCA'
ELDER = 'ED'
QUEEN = 'QU'
KIT = 'KT'
POSITION_CHOICES =(
    (LEADER, 'Leader'),
    (DEPUTY , 'Deputy'),
    (WARRIOR,  'Warrior'),
    (APPRENTICE, 'Apprentice'),
    (MEDICINE_CAT , 'Medicine Cat'),
    (MEDICINE_CAT_APPRENTICE, 'Medicine Cat Apprentice'),
    (ELDER, 'Elder'),
    (QUEEN, 'Queen'),
    (KIT, 'Kit'  ),
)

class ClanForm(forms.Form):
    name = forms.CharField(label='Name:', max_length=20)
    habitat = forms.ChoiceField(label='Habitat:', choices=HABITAT_CHOICES)

#class CatForm(forms.Form):
#    name = forms.CharField(label='Name:', max_length=20)
#    age = forms.IntegerField(label='Age:')
#    clan = forms.ModelChoiceField(label='Clan:', queryset=Clan.objects.all())
#    position = forms.ChoiceField(label="Status:", choices=POSITION_CHOICES)
    
