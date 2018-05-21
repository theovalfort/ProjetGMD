database = open('br08303.keg', 'r')

HashMap = {}

for line in database :
    if line.startswith("F"):
        a = line.strip('F   ')
        tab = a.split()
        num = tab[0]
        name = []
        for i in range(1, len(tab)-1):
            name.append(tab[i])
        fullname = ' '.join(name)
        HashMap[num] = fullname

def searchName(ATCid):
    return HashMap[ATCid];


print(searchName('D01467'))
