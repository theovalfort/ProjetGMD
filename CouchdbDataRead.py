import couchdb

couch = couchdb.Server("http://couchdb.telecomnancy.univ-lorraine.fr")
db = couch['orphadatabase']
#for id in db :
 #   print(id)
doc = db['CStoDiseaseClassificationMinified.json']


for item in db.view('clinicalsigns/GetClinicalSignDiseases'):
    #print(item)
    if (item.value['disease']['Name']['text'] == 'Jacobsen syndrome'):
         print(item)


#for item in db.view('diseases/GetDiseasesNumber'):
    #if(item.value['OrphaNumber']==325529):
       #print(item)

#for item in db.view('diseases/GetDiseasesBySynonym'):
      #print(item.value['SynonymList']['Synonym'][0]["text"])
