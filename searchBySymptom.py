import CouchdbDataRead as cdb
import HPOsqlRead as hsql
import OmimcsvRead as ocsv
import OmimTxtRead as otxt
import HPOsqlRead as hpsql
import HpOboRead as hpobo
import csv

symptom = ""

def getDiseasesName(symptom) :
        resultfile = open("results.csv", "w", newline='')
        fieldnames = ['Symptom', 'Disease Name', 'Side Effect origin', 'Drug', 'original Files', 'Iterations']
        writer = csv.DictWriter(resultfile, fieldnames=fieldnames)
        writer.writeheader()

        omimtxt = otxt.searchBySymptom(symptom)
        couch = cdb.searchByClinicalSign(symptom)
        hpID = hpobo.searchBySymptom(symptom)
        print(hpID)
        #hp = hsql.find_disease_db_id_and_disease_from_sign_id()
        #print(hp)
        for i in range(len(couch)-1):
            writer.writerow({"Symptom": symptom, "Disease Name": couch[i].rstrip(), 'Side Effect origin' : '', 'Drug': '', 'original Files': 'Orphadata', 'Iterations' : 0})


        for i in range(len(omimtxt)-1):
            writer.writerow({"Symptom": symptom, "Disease Name": omimtxt[i].rstrip(), 'Side Effect origin' : '', 'Drug': '', 'original Files': 'Omim.txt', 'Iterations' : 0})

        resultfile.close()

def resultClassification(file):
    file = open(file, "r")
    resultFile = csv.DictReader(file)
    size = 0
    analyse = [r for r in resultFile]
    #print(analyse)
    print(len(analyse))
    for i in range(1,len(analyse)-1):
        test = analyse[i]['Disease Name']

        test.lower()
        #print(test)
        for j in range(1,len(analyse)-1):
            #print(j)
            #if j!=i :
            compa = analyse[j]['Disease Name'].lower()
            #print(compa)
            if test in compa :
                print("hello",analyse[j]['Disease Name'])

    file.close()




#resultClassification("results.csv")
getDiseasesName("Hip dislocation")


