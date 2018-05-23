database = open('hp.obo', 'r')

HashMap = {}

def searchBySymptom (symptom):
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

    return HashMap
