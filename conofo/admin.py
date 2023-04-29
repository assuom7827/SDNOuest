from django.contrib import admin
from conofo.models import *
from django.contrib.admin.options import TabularInline

admin.site.site_header ='Connaitre Nos Formation CONFO'

class ModuleForFilliereAdminInline(TabularInline):
        extra = 3
        exclude = ('specialite',)
        model = Modules

class ModuleForSpecialiteAdminInline(TabularInline):
        extra = 3
        exclude = ('filiere',)
        model = Modules

class EtablissementAdmin(admin.ModelAdmin):
    list_display=('code_etablissement','intitule_etabilissement_fr','intitule_etablissement_ar','nature_etablissement','wilaya')
    
class FaculteAdmin(admin.ModelAdmin):
    list_display=('statut','intitule_faculte_fr','pseudo_faculte')

class DomaineAdmin(admin.ModelAdmin):

    list_display=('pseudo_domaine','intitule_domaine_fr')
    list_filter = ('pseudo_domaine',)

class CycleAdmin(admin.ModelAdmin):

    list_display=('code_cycle','intitule_cycle_fr','intitule_cycle_ar')
    
class TypesFormationAdmin(admin.ModelAdmin):

    list_display=('code_TF','intitule_TF_fr','intitule_TF_ar')

class FiliereAdmin(admin.ModelAdmin):
    list_display=('pseudo_filiere','full_filiere','domaine','type_formation')
    list_display_links=('pseudo_filiere','full_filiere')
    list_filter = ('domaine','pseudo_filiere')
    inlines = (ModuleForFilliereAdminInline,)

#class SpecialiteAdmin(admin.ModelAdmin):
 #   list_display=('pseudo_specialite','full_specialite','type_formation')
  #  list_display_links=('pseudo_specialite','full_specialite')
   # list_filter = ('pseudo_specialite')
    #inlines = (ModuleForSpecialiteAdminInline,)


class SpecialitesAdmin(admin.ModelAdmin):
    list_display=('code_specialite','full_specialite','type_formation')
    list_display_links=('code_specialite','full_specialite')
    inlines = (ModuleForSpecialiteAdminInline,)

class ModuleAdmin(admin.ModelAdmin):
    list_display=('code_module','intitule_module_fr','intitule_module_ar','unite_enseignement')
    list_display_links=('code_module','intitule_module_fr')
   
     

class BacAdmin(admin.ModelAdmin):
    list_display =('pseudo_bac','serie_bac_fr')

class FiliereBacAdmin(admin.ModelAdmin):
    list_display =('bac','filiere','moyenne_min','condition_matiere','autorized','priorite','zone','annee_bac')
    list_filter = ('priorite','filiere','bac','annee_bac')

class UEAdmin(admin.ModelAdmin):
    list_display =('code_ue_fr','intitule_ue_fr','intitule_ue_ar','code_ue_ar')

    
    
admin.site.register(Etablissements,EtablissementAdmin)    
admin.site.register(Facultes,FaculteAdmin)
#admin.site.register(Domaines,DomaineAdmin)
admin.site.register(Filieres,FiliereAdmin)
admin.site.register(Specialites,SpecialitesAdmin)
admin.site.register(Bac,BacAdmin)
admin.site.register(FiliereBac,FiliereBacAdmin)
#admin.site.register(UnitesEnseignements,UEAdmin)
#admin.site.register(Modules,ModuleAdmin)
admin.site.register(Cycles,CycleAdmin)
admin.site.register(TypesFormation,TypesFormationAdmin)

