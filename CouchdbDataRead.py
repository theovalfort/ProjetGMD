import couchdb

couch = couchdb.Server("http://couchdb.telecomnancy.univ-lorraine.fr")
db = couch['orphadatabase']
#for id in db :
 #   print(id)
doc = db['CStoDiseaseClassificationMinified.json']

def searchByClinicalSign(sign):
    result = []
    for item in db.view('clinicalsigns/GetClinicalSignDiseases'):
        if sign in item.value['clinicalSign']['Name']['text']:
            result.append(item.value['disease']['Name']['text'])
    return result

#for item in db.view('clinicalsigns/GetClinicalSignDiseases'):
   # print(item)
 #   if 'dysplasia/coxa valga/coxa vara' in item.value['clinicalSign']['Name']['text']:
  #       a= item.value['disease']['Name']['text']



#for item in db.view('diseases/GetDiseasesNumber'):
 #   if(item.value['OrphaNumber']==325529):
  #     print(item)

#for item in db.view('diseases/GetDiseasesBySynonym'):
#      print(item.value['SynonymList']['Synonym'][0]["text"])

#for item in db.view('diseases/GetDiseasesByName'):

