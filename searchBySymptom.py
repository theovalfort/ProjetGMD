import CouchdbDataRead as cdb
import HPOsqlRead as hsql
import OmimcsvRead as ocsv
import OmimTxtRead as otxt
import HpOboRead as hpobo
import MeddraRead as med
import DrugBankRead as dbr

import csv

symptom = ""


def searchDisease(symptom):
    resultfile = open("results.csv", "w", newline='')
    fieldnames = ['Symptom', 'Disease Name', 'Side Effect origin', 'Drug', 'original Files', 'Iterations']
    writer = csv.DictWriter(resultfile, fieldnames=fieldnames)
    writer.writeheader()
    tabResult = []
    dictResult= {}

    omimtxt = otxt.searchBySymptom(symptom)
    couch = cdb.searchByClinicalSign(symptom)
    hpID = hpobo.searchHPOidbySymptom(symptom)
    cui = med.find_stitch_id_and_CUI_id_from_side_effect_name("Abdominal cramps")



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

    for i in range(len(cui)):
        res = ocsv.find_disease_ans_synonyms_from_CUI_Id(cui[0][i]['cui'])
        #res = ocsv.find_disease_ans_synonyms_from_CUI_Id('C2239773')
        if res is not None:
            drug = dbr.searchTreatment(res)
            dictResult["Symptom"] = symptom
            dictResult["Disease Name"] = res
            dictResult['Side Effect origin'] = ''
            dictResult['Drug'] = drug
            dictResult['original Files'] = 'Meddra + Omim.csv + DrugBank'
            dictResult['Iterations'] = 1
            tabResult.append(dictResult)
            writer.writerow(
                {"Symptom": symptom, "Disease Name": res, 'Side Effect origin': '', 'Drug': drug,
                 'original Files': 'Meddra + Omim.csv + DrugBank', 'Iterations': 1})


    return tabResult
    resultfile.close()



"""
def resultClassification(file):
    file = open(file, "r")
    resultFile = csv.DictReader(file)
    size = 0
    analyse = [r for r in resultFile]
    # print(analyse)
    print(len(analyse))
    for i in range(1, len(analyse) - 1):
        test = analyse[i]['Disease Name']

        test.lower()
        # print(test)
        for j in range(1, len(analyse) - 1):
            # print(j)
            # if j!=i :
            compa = analyse[j]['Disease Name'].lower()
            # print(compa)
            if test in compa:
                print("hello", analyse[j]['Disease Name'])

    file.close()
    """



# resultClassification("results.csv")
print(searchDisease('Hip dislocation'))
