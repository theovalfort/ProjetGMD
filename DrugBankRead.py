import xml.sax
source = open("full database.xml",encoding="utf8")
class DrugContentHandler(xml.sax.ContentHandler):


    def __init__(self):
        self.DiseasesTab = []
        self.SideEffectTab = []
        self.DrugName = []
        self.i = -1
        self.tab = 0
        self.inside = 0
        xml.sax.ContentHandler.__init__(self)

    def startElement(self, name, attrs):
        #print("element ", name, " level ", self.inside)
        if name == "drug" and self.inside == 1:
            self.i +=1
            #print("druglvl", self.inside)
            #print("parsing drug nb: ", self.i)
        elif name == "name" and self.inside == 2:
            self.tab = 3
            #print("drug nme: ", name, "self inside", self.inside)
        elif name == "toxicity" and self.inside == 2:
            self.tab = 1
        elif name == "indication" and self.inside == 2:
            self.tab = 2
        self.inside+=1

    def endElement(self, name):
        self.tab = 0
        self.inside-=1

    def characters(self, content):
        if(self.tab==3):
            self.DrugName.append(content)
        elif(self.tab==1):
            self.SideEffectTab.append(content)
        elif(self.tab==2):
            self.DiseasesTab.append(content)



print("Parsing, please wait")
d = DrugContentHandler()
xml.sax.parse(source, d)
print("End of the parsing")

    #print(d.DrugName)
    #print(d.SideEffectTab)
    #print(d.DiseasesTab)
def searchTreatment(symptom):
    result=[]
    for i in range(len(d.DiseasesTab)):
        if symptom.lower() in (d.DiseasesTab[i]).lower():
            result.append(d.DrugName[i])

    return result

def searchOrigin(sideEffect):
    result = []
    for i in range(len(d.SideEffectTab)):
        if sideEffect.lower() in (d.SideEffectTab[i]).lower():
            result.append(d.DrugName[i])
    return result

if __name__ == "__main__":
    print(searchTreatment("muscular"))
    print(searchOrigin("dyspnea"))


