from django.db import models
from django.forms import ModelForm

# Create your models here.

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

class Clan(models.Model):
    name = models.CharField(max_length=20)
    habitat = models.CharField(max_length=1,
                               choices=HABITAT_CHOICES,
                               default=FOREST)
    def __str__(self):
        return self.name

class Cat(models.Model):
    name = models.CharField(max_length=20)
    photo = models.ImageField(upload_to="cats",null=True, blank=True)
    age = models.IntegerField(default=12)
    clan = models.ForeignKey(Clan,  on_delete=models.CASCADE)
    position = models.CharField(max_length=3,
                                choices=POSITION_CHOICES,
                                default=WARRIOR)
    strength = models.IntegerField(default=35)
    intelligence = models.IntegerField(default=35)
    agility = models.IntegerField(default=35)
    health = models.IntegerField(default=35)
    speed = models.IntegerField(default=35)
    perception = models.IntegerField(default=35)
    sensitivity = models.IntegerField(default=35)

    hunting = models.IntegerField(default=35)
    fighting = models.IntegerField(default=35)
    running = models.IntegerField(default=35)
    jumping = models.IntegerField(default=35)
    obedience = models.IntegerField(default=35)
    climbing = models.IntegerField(default=35)
    leadership = models.IntegerField(default=25)
    cleverness = models.IntegerField(default=35)
    stealth = models.IntegerField(default=35)
    attentiveness = models.IntegerField(default=35)

    def __str__(self):
        return self.name

class CatForm(ModelForm):
    class Meta:
        model = Cat
        fields = '__all__'
        #fields = ['name', 'age', 'clan', 'position']
        
