import csv

tsv = open("chemical.sources.tsv")
tsvreader = csv.reader(tsv, delimiter='\t')
for i in range(0, 9):
    next(tsvreader, None)

def querytsv(ATC_code):
    for row in tsvreader:
        if row[3]==ATC_code:
            return([row[0],row[1]])

def querytsvCID(CID1,CID2):
    for row in tsvreader:
        if (row[0]==CID1 and row[1]==CID2 and row[2]=="ATC"):
            return(row[3])


print(querytsvCID('CIDm00003954','CIDs00003954' ))