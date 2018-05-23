class Tree(object):
    def __init__(self):
        self.child = []
        self.id = None
        self.name = None
        self.effect = []


    def createChildren(self, amount):
        for i in range(0, amount):
            self.child.append(Tree())

    def setName(self,name):
        self.name = name

    def setID(self,numID):
        self.id = numID

    def setEffect(self,effect):
        self.effect.append(effect)

database = open("omim.txt",'r')
terme = "*FIELD* NO"
terme2 = "*FIELD* TI"
terme3 = "*FIELD* CS"
terme4 = "*THEEND*"
terme5 = "*RECORD*"

root = Tree()
i = 0
print("Parsing of OMIM.txt, please wait")
for line in database:
    line.strip().split('/n')

    if line.startswith(terme):
        root.createChildren(1)
        root.child[i].createChildren(3)
        line=database.readline()
        root.child[i].child[0].setID(line)
        i = i+1

    if line.startswith(terme2):
        line = database.readline()
        root.child[i-1].child[1].setName(line)

    elif line.startswith(terme3):
        root.child[i-1].child[2].setName("Effect")

    elif (not line.startswith(terme4)) and (len(line.strip())>0) and (line.startswith(" ")):
        effect = line.strip(' \t\n\r')
        root.child[i-1].child[2].setEffect(effect)

database.close()
print("End of the parsing")


def searchById(id):
    resultID = []
    for j in range(i - 1):
        if (int(root.child[j].child[0].id) == id):
            resultID.append(root.child[j].child[1].name)
    return resultID

def searchByName(name):
    resultName = []
    for j in range(i-1):
        if (name in root.child[j].child[1].name):
            resultName.append(root.child[j].child[2].effect)
    return resultName

def searchBySymptom(effect):
    resultSymptom = []
    for j in range(i-1):
        if effect in root.child[j].child[2].effect :
            resultSymptom.append(root.child[j].child[1].name)
    return resultSymptom

#print(searchById(616211))
#print(searchByName("EPILEPTIC ENCEPHALOPATHY"))
#print(searchBySymptom("Hip dislocation"))
