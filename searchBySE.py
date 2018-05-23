import csv

import MeddraRead as med
import ATCKegRead as atc
import stichtsv as sti
#import DrugBankRead as dbr
#import searchBySymptom as sbs


def searchSE(sideEffect):
    resultfile = open("results.csv", "w", newline='')
    fieldnames = ['Symptom', 'Disease Name', 'Side Effect origin', 'Drug', 'original Files', 'Iterations']
    writer = csv.DictWriter(resultfile, fieldnames=fieldnames)
    writer.writeheader()
    tabResult = []
    dictResult= {}

    cid = med.find_stitch_id_and_CUI_id_from_side_effect_name(sideEffect)
    atcresult=[]
    for i in range(len(cid)):
        cid1=cid[0][i]['stitch_compound_id1'][:3]+"m"+cid[0][i]['stitch_compound_id1'][4:12]
        print(cid1)
        cid2=cid[0][i]['stitch_compound_id2'][:3]+"s"+cid[0][i]['stitch_compound_id2'][4:12]
        print(cid2)
        atcid = sti.querytsvCID(cid1,cid2)
        print("stitch", atcid)
        atcresult.append(atc.searchName(atcid))
        print(atcresult)
    print(atcresult)
    resultfile.close()
searchSE("Abdominal cramps")
"""
    for i in range(len(couch) - 1):
        drug = dbr.searchTreatment(couch[i].rstrip())
        dictResult["Symptom"]=symptom
        dictResult["Disease Name"]=couch[i].rstrip()
        dictResult['Side Effect origin']=''
        dictResult['Drug']=drug
        dictResult['original Files']='Orphadata + DrugBank'
        dictResult['Iterations']=1
        tabResult.append(dictResult)
        #print(tabResult)
        writer.writerow({"Symptom": symptom, "Disease Name": couch[i].rstrip(), 'Side Effect origin': '', 'Drug': drug,
                         'original Files': 'Orphadata + DrugBank', 'Iterations': 1})

    for i in range(len(omimtxt) - 1):
        drug = dbr.searchTreatment(omimtxt[i].rstrip())
        dictResult["Symptom"] = symptom
        dictResult["Disease Name"] = omimtxt[i].rstrip()
        dictResult['Side Effect origin'] = ''
        dictResult['Drug'] = drug
        dictResult['original Files'] = 'Omim.txt + DrugBank'
        dictResult['Iterations'] = 1
        tabResult.append(dictResult)
        writer.writerow({"Symptom": symptom, "Disease Name": omimtxt[i].rstrip(), 'Side Effect origin': '', 'Drug': drug,
                         'original Files': 'Omim.txt + DrugBank', 'Iterations': 1})
    if hpID is not None:
        hp = hsql.find_disease_db_id_and_disease_from_sign_id(hpID)
        hpresult= [x for x in hp[1][1].split(";") if x != '']
        #['%102100 ACROMEGALOID CHANGES, CUTIS VERTICIS GYRATA, AND CORNEAL LEUKOMA', 'ROSENTHAL-KLOEPFER SYNDROME']
        for i in range(len(hpresult) - 1):
            drug = dbr.searchTreatment(hpresult[i].rstrip())
            dictResult["Symptom"] = symptom
            dictResult["Disease Name"] = hpresult[i].rstrip()
            dictResult['Side Effect origin'] = ''
            dictResult['Drug'] = drug
            dictResult['original Files'] = 'HPO.obo + HPO.sqlite + DrugBank'
            dictResult['Iterations'] = 1
            tabResult.append(dictResult)
            writer.writerow(
                {"Symptom": symptom, "Disease Name": hpresult[i].rstrip(), 'Side Effect origin' : '', 'Drug':drug,
                 'original Files': 'HPO.obo + HPO.sqlite + DrugBank', 'Iterations': 1})

    return tabResult"""


