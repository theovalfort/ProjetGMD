import csv

tsv = open("C:/Users/ypsor/PycharmProjects/GMD/chemical_source.tsv")
tsvreader = csv.reader(tsv, delimiter='	')
for i in range(0, 9):
    next(tsvreader, None)

def querrytsv(ATC_code):
    for row in tsvreader:
        if row[3]==ATC_code:
            return([row[0],row[1]])

def querrytsvCID(CID1,CID2):
    for row in tsvreader:
        if (row[1]==CID2 & row[0]==CID1):
            return(row[3])


