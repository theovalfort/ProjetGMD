import csv

tsv = open("chemical_sources_filtered.tsv")
tsvreader = csv.reader(tsv, delimiter='\t')

#for i in range(0, 9):
#next(tsvreader, None)

def querytsvCID(CID1,CID2):
    i = 0
    for row in tsvreader:
        if (row[0]==CID1 and row[1]==CID2):
            return(row[3])


#print(querytsvCID('CIDm00003954','CIDs00003954' ))