import os
from .models import Pathology, User, Patient,TraitementMolecule,TraitementClasse,TraitementCIS

### Renvoie la liste de toutes les maladies
def pathologyChoices():

    temp = Pathology.query.with_entities(Pathology.id, Pathology.name, Pathology.other_name).all()
    other_name_temp = []

    for x in temp:
        if x[2]:
            array = x[2].split(",")

            for i in range(len(array)):
                if array[i] is not None:
                    other_name_temp.append((x[0], array[i].strip()))

    choices = [(x[0], x[1]) for x in temp] + other_name_temp

    i = 0
    l = len(choices)
    while (i < l and choices[i]):
        if choices[i][1] == '':
            del choices[i]
            l -= 1
        else:
            i += 1

    return choices

#renvoie la liste de tous les users
def userChoices():

    temp = User.query.with_entities(User.id, User.forename).all()
    choices = [(x[0], x[1]) for x in temp]
    return choices

def patientAll():
    temp = Patient.query.with_entities(Patient.id).all()
    patient = [(x[0])for x in temp]
    return patient
def getPathologyIcd10(pathology):#icd10
    icd10 = Pathology.query.filter_by(id=pathology).with_entities(Pathology.icd_10).first()
    icd10 = cleanChar(icd10)
    return icd10

def getTraitementMol(icd10):
    traitementM = TraitementMolecule.query.filter_by(icd10=icd10).with_entities(Pathology.icd_10)
    traitementM = cleanChar(traitementM)
    return traitementM
def getTraitementClasse(icd10):
    traitementC = TraitementClasse.query.filter_by(icd10=icd10).with_entities(Pathology.icd_10)
    traitementC = cleanChar(traitementM)
    return traitementC
def getTraitementCIS(icd10):
    traitementCIS = TraitementCIS.query.filter_by(icd10=icd10).with_entities(Pathology.icd_10)
    traitementCIS = cleanChar(traitementM)
    return traitementCIS
