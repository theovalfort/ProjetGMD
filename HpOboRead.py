database = open('hp.obo', 'r')

HashMap = {}


for line in database :
        if line.startswith("id"):
            a=line.split()
            id = a[1]
            line=database.readline()
            if line.startswith("name:"):
                b=line.split()
                name=[]
                for i in range(1,len(b)-1):
                    name.append(b[i])
                fullname = ' '.join(name)
                HashMap[fullname]=id




def searchHPOidbySymptom(symptom):
    if symptom in HashMap:
        return HashMap[symptom]
