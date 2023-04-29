from django.db import models
from django.urls import reverse
import uuid
import datetime


class Etablissements (models.Model):
    
    NATURE_LISTE=(
        ('UN','Université'),
        ('CU','Centre Universitaire'),
        ('ENS','Ecole Nationale Supérieure'),
        ('ENRS','Ecole Normale Supérieure'),
        ('IN','Institut Nationale'),   
    )
    code_etablissement=models.CharField(max_length=10,verbose_name="Code établissement",help_text="Le code de l'établissement exemple:UMAB")
    intitule_etabilissement_fr = models.CharField(max_length=200,verbose_name="Nom de l'établissement (en latin)")
    intitule_etablissement_ar = models.CharField (max_length=200, verbose_name="Nom de l'établissement (en arabe)")
    nature_etablissement = models.CharField(max_length=4,verbose_name="Nature de l'établissement",choices=NATURE_LISTE)
    site_etablissement = models.CharField(max_length=200,verbose_name="Site de l'établissement")
    wilaya = models.ForeignKey('Wilaya',on_delete=models.CASCADE,verbose_name = "Wilaya")
    
    class Meta:
        verbose_name = ("Etablissement")
        verbose_name_plural = ("Etablissements")
        
    def __str__(self):
         return '%s:%s' %(self.code_etablissement,self.intitule_etabilissement_fr)
         
class Facultes(models.Model):
    STATUT_STRUCTURE_LISTE= (
        ('FAC','Faculté'),
        ('INS','Institut'),
    )

    code_faculte=models.CharField(max_length=8,verbose_name="Code de la faculté",help_text="Entrer le code de la faculté")
    intitule_faculte_fr = models.CharField(max_length=200,verbose_name="Intitulé de la faculté (en latin)")
    intitule_faculte_ar = models.CharField (max_length=200, verbose_name="Intitulé de la faculté (en arabe)")
    statut = models.CharField(max_length=3,verbose_name="Statut",choices=STATUT_STRUCTURE_LISTE)
    pseudo_faculte= models.CharField(max_length=8,verbose_name="Pseudo code de la faculté ")
    etablissement = models.ForeignKey('Etablissements',on_delete=models.SET_NULL,verbose_name="Etablissement",null= True)
    
    class Meta:
        verbose_name = ("Faculté")
        verbose_name_plural = ("Facultés")
    
    def __str__(self):
        return '%s : %s' %(self.pseudo_faculte,self.intitule_faculte_fr)
   

class Domaines (models.Model):

    code_domaine=models.CharField(max_length=3,verbose_name="code du domaine",help_text="Entrer le code du domaine")
    intitule_domaine_fr = models.CharField(max_length=200,verbose_name="Intitulé du domaine (En latin) ")
    intitule_domaine_ar = models.CharField (max_length=200, verbose_name="Intitulé du domaine (En arabe)")
    pseudo_domaine= models.CharField(max_length=8,verbose_name="Pseudo code du domaine ",null=True)
    
    
    class Meta:
        verbose_name = ("Domaine")
        verbose_name_plural = ("Domaines")
        
    def __str__(self):
        return '%s : %s' %(self.pseudo_domaine, self.intitule_domaine_fr)

class Cycles(models.Model):
    
    code_cycle =models.CharField(max_length=3,verbose_name="Code du Cycle")
    intitule_cycle_fr = models.CharField(max_length=25,verbose_name="Intitulé du Cycle (En latin)")
    intitule_cycle_ar = models.CharField (max_length=25, verbose_name="Intitulé du Cycle (En arabe)")
    
    class Meta:
        verbose_name = ("Cycle")
        verbose_name_plural = ("Cycles")
        
    def __str__(self):
        return '%s - %s' %(self.code_cycle,self.intitule_cycle_fr)

class TypesFormation (models.Model):
    
    code_TF =models.CharField(max_length=3,verbose_name="Code type de formation")
    intitule_TF_fr = models.CharField(max_length=35,verbose_name="Intitulé de type de formation (En latin)")
    intitule_TF_ar = models.CharField (max_length=35, verbose_name="Intitulé de type de formation (En arabe)")
    
    class Meta:
        verbose_name = ("Type de formation")
        verbose_name_plural = ("Types de formation")
        
    def __str__(self):
        return '%s - %s' %(self.code_TF,self.intitule_TF_fr)

class Filieres (models.Model):
  
    
    code_filiere=models.CharField(max_length=3,verbose_name="Code du filiere",help_text="Entrer le code du filiere")
    intitule_filiere_fr = models.CharField(max_length=200,verbose_name="Intitulé du filiere (En latin)")
    intitule_filiere_ar = models.CharField (max_length=200, verbose_name="Intitulé du filiere (En arabe)",null=True)
    cycle = models.ForeignKey('Cycles',verbose_name="Cycle de filière",on_delete = models.SET_NULL,null=True)
    pseudo_filiere= models.CharField(max_length=8,verbose_name="Pseudo code de la filiere ")
    type_formation = models.ForeignKey('TypesFormation',verbose_name="Type de la formation",on_delete = models.SET_NULL,null=True)
    domaine= models.ForeignKey('Domaines',on_delete=models.SET_NULL,null=True)
    faculté= models.ForeignKey('Facultes',on_delete=models.SET_NULL,null=True)
    bac= models.ManyToManyField ('Bac',through='FiliereBac')
    description_filière= models.TextField(verbose_name='Description de la filière')
    debouchés_filière = models.TextField(verbose_name='Débouchés de la filière')
    responsable_formation = models.CharField(max_length=50,verbose_name="Responsable de la formation",null=False)
    email_responsable = models.EmailField(max_length=50,verbose_name="E-mail responsable",null=False)
    
    class Meta:
        verbose_name = ("Filière")
        verbose_name_plural = ("Filières")
        
    def __str__(self):
        return '%s:%s' %(self.code_filiere,self.intitule_filiere_fr)
        
    @property
    def full_filiere(self):
        return  '%s : %s' %(self.code_filiere,self.intitule_filiere_fr)
    
class Specialites (models.Model):
    
    CYCLE_LISTE=(
        ('L','LICENCE'),
        ('M','MASTER'),
        ('D','DOCTEUR'),
        ('DM','Docteur en Médecine'),
        ('ING','Ingénieur'),
    )
    TYPE_FORMATION_LISTE=(
        ('ACA','Académique'),
        ('PRO','Professionnalisante'),
    )
    
    code_specialite = models.CharField(max_length=3,verbose_name="Code de la specialité ",help_text="Entrer le code de la spécialité ")
    intitule_specialite_fr = models.CharField(max_length=200,verbose_name="Intitulé de la spécialité (En latin)")
    intitule_specialite_ar = models.CharField (max_length=200, verbose_name="Intitulé de la spécialité (En arabe)",null=True)
    cycle = models.ForeignKey('Cycles',verbose_name="Cycle de spécialité",on_delete = models.SET_NULL,null=True)
    pseudo_specialite= models.CharField(max_length=8,verbose_name="Pseudo code de la specialité",null=True)
    type_formation = models.ForeignKey('TypesFormation',verbose_name="Type de la formation",on_delete = models.SET_NULL,null=True)
    filiere = models.ForeignKey('Filieres',on_delete=models.SET_NULL,null=True)
    description_specialite= models.TextField(verbose_name='Description de la spécialité')
    debouchés_specialite = models.TextField(verbose_name='Débouchés de la spécialité')
    responsable_formation = models.CharField(max_length=50,verbose_name="Responsable de la formation",null=False)
    email_responsable = models.EmailField(max_length=50,verbose_name="E-mail responsable",null=False)
    
    class Meta:
        verbose_name = ("Spécialité")
        verbose_name_plural = ("Spécialités")
        
    def __str__(self):
        return '%s:%s' %(self.code_specialite,self.intitule_specialite_fr)
        
    @property
    def full_specialite(self):
        return  '%s : %s' %(self.code_specialite,self.intitule_specialite_fr)
 
class Modules(models.Model):
    
    code_module = models.CharField(max_length=3,verbose_name="Code module")
    intitule_module_fr = models.CharField(max_length=50,verbose_name="Intitulé du module (En latin)",blank = True)
    intitule_module_ar = models.CharField (max_length=50, verbose_name="Intitulé du module (En arabe)",blank = True)
    coef_module = models.IntegerField (verbose_name="Coef module")
    unite_enseignement = models.ForeignKey('UnitesEnseignements',verbose_name='Unité Enseignement',on_delete=models.SET_NULL,null = True)
    filiere = models.ForeignKey('Filieres',verbose_name='Filière',on_delete=models.SET_NULL,null = True)
    specialite = models.ForeignKey('Specialites',verbose_name='Spécialité',on_delete=models.SET_NULL,null = True)

    
    class Meta:
        verbose_name = ("Module")
        verbose_name_plural = ("Modules")
        
    def __str__(self):
        return '%s:%s' %(self.code_module,self.intitule_module_fr)
    
    
class UnitesEnseignements(models.Model):
    
    code_ue_fr = models.CharField(max_length=3,verbose_name="Code UE (latin)")
    code_ue_ar = models.CharField(max_length=6,verbose_name="Code UE (arabe)")
    intitule_ue_fr = models.CharField(max_length=200,verbose_name="Intitulé UE (En latin)")
    intitule_ue_ar = models.CharField (max_length=200, verbose_name="Intitulé UE (En arabe)")

    class Meta:
        verbose_name = ("Unité Enseignement")
        verbose_name_plural = ("Unités Enseignement")
        
    def __str__(self):
        return '%s:%s' %(self.code_ue_fr,self.intitule_ue_fr)


class Bac (models.Model):
    SERIE_BAC_FR_LISTE=(
        ('SE','Sciences Experimentales'),
        ('TM','Technique Mathématique'),
        ('MATH','Mathématique'),
        ('GE','Gestion et Economie'),
        ('LPH','Lettres et Philosophie'),
        ('LLE','Lettres et Langues Etrangères'),
        ('SNV','Science de la Nature et de la Vie'),
        ('LSH','Lettres et Sciences Humaines'),
        ('TC','Technique Comptable'),
        ('FM','Fabrication Mécanique'),
        ('ELECT','Electronique'),
        ('ELECTROTECH','Electrotechnique'),
        ('CHIMIE','Chimie'),
        ('TPB','Travaux Publiques et Batiments'),
        ('ETR','Bac Etranger'),
        ('Autre','Autre')
    )

    pseudo_bac = models.CharField(max_length=15,verbose_name="Pseudo Bac",null=True)
    serie_bac_fr = models.CharField(max_length=80,choices=SERIE_BAC_FR_LISTE,verbose_name="Serie du Bac")
    
    class Meta:
        verbose_name = ("Bac")
        verbose_name_plural = ("Bacs")
        
    def __str__(self):
        return  '%s' %(self.pseudo_bac)

    @property
    def code_bac(self):
        return '%s' %(self.pseudo_bac)

    


class FiliereBac (models.Model):

    YEAR_CHOICES = [(r,r) for r in range(2000, datetime.date.today().year)]

    PRIORITE_LISTE = (
        ('0','Priorité 0'),
        ('1','Priorité 1'),
        ('2','Priorité 2'),
        ('3','Priorité 3')
    )

    STATUT_FILIERE_LISTE=(
        ('G','Gelée'),
        ('O','Ouverte')
    )

    filiere = models.ForeignKey('Filieres',on_delete = models.CASCADE)
    bac = models.ForeignKey('Bac',on_delete = models.CASCADE)
    moyenne_min = models.DecimalField(null=True,max_digits=5 ,decimal_places=2)
    condition_matiere = models.TextField(max_length=100, null = True)
    autorized = models.BooleanField(verbose_name="Filieres Autorisée",default=False)
    priorite= models.CharField(max_length=1,choices=PRIORITE_LISTE,verbose_name="Priorité",null = True)
    zone = models.CharField (max_length=30,default='27',verbose_name='Zone autorisée')
    annee_bac = models.IntegerField(('Année Bac'), choices=YEAR_CHOICES, default = 2019 )
    statut_filiere = models.CharField(max_length=1,choices=STATUT_FILIERE_LISTE ,verbose_name="Statut de la filière",default='O')

    class Meta:
        ordering=['-moyenne_min','priorite']

    def __str__(self):
        return '%s,%s' %(self.filiere,self.bac)


class Wilaya(models.Model):
    code_wilaya = models.IntegerField( verbose_name='Matricule Wilaya' )
    libelle_wilaya_fr=models.CharField(max_length=50,verbose_name="Wilya FR")
    libelle_wilaya_ar=models.CharField(max_length=50,verbose_name="Wilya AR")

    class Meta:
        verbose_name = ("Wilaya")
        verbose_name_plural = ("Wilayas")
        
    def __str__(self):
        return '%s:%s' %(self.code_wilaya,self.libelle_wilaya_fr)
