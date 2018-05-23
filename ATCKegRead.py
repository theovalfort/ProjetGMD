database = open('br08303.keg', 'r')

HashMap = {}

for line in database :
    name = []
    if line.startswith("F") or line.startswith("E"):
        if line.startswith("F"):
            a = line.strip('F   ')
        elif line.startswith("E"):
            a = line.strip('E   ')
        tab = a.split()
        num = tab[0]
        for i in range(1, len(tab)):
            name.append(tab[i])
        fullname = ' '.join(name)
        HashMap[num] = fullname



def searchName(ATCid):
    return HashMap[ATCid];


print(searchName('A16AX02'))
