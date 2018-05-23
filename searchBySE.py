import csv

import MeddraRead as med
import ATCKegRead as atc
import stichtsv as sti
import DrugBankRead as dbr
#import searchBySymptom as sbs


def searchSE(sideEffect):
    resultfile = open("resultsSE.csv", "w", newline='')
    fieldnames = ['Side Effect', 'Origin', 'original Files', 'Iterations']
    writer = csv.DictWriter(resultfile, fieldnames=fieldnames)
    writer.writeheader()
    tabResult = []
    dictResult= {}
    cid = med.find_stitch_id_and_CUI_id_from_side_effect_name(sideEffect)
    atcresult=[]

    drugo=dbr.searchOrigin(sideEffect)

    for i in range(len(drugo)):
           dictResult["Side Effect"] = sideEffect
           dictResult["Origin"] = drugo[i].rstrip()
           dictResult['original Files'] = 'DrugBank'
           dictResult['Iterations'] = 1
           tabResult.append(dictResult)
           # print(tabResult)
           writer.writerow({"Side Effect": sideEffect, "Origin": drugo[i].rstrip(),
                             'original Files': 'DrugBank', 'Iterations': 1})



    for i in range(len(cid)):
        cid1=cid[0][i]['stitch_compound_id1'][:3]+"m"+cid[0][i]['stitch_compound_id1'][4:12]
        #print(cid1)
        cid2=cid[0][i]['stitch_compound_id2'][:3]+"s"+cid[0][i]['stitch_compound_id2'][4:12]
        #print(cid2)
        atcid = sti.querytsvCID(cid1,cid2)
        #print("stitch", atcid)
        atcresult.append(atc.searchName(atcid))
        #print(atcresult)
    #print(atcresult)

    return tabResult
    resultfile.close()
searchSE("Abdominal cramps")



