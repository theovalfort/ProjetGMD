# -*- coding:utf-8 -*-

__nom_fichier__ = "fichier csv"
__author__ = "Capucine"
__date__ = "avril 2018"

import csv


def find_synonyms_and_CUI_Id_from_disease(disease_name):
    file = open("omim_onto.csv", "r")
    f_omim = csv.reader(file)
    for row in f_omim:
        if row[1]==disease_name:
            return (row[2], row[5])
    f_omim.close()

#
# def find_CUI_Id_from_disease(disease_name):
#     file = open("omim_onto.csv", "r")
#     f_omim = csv.reader(file)
#     for row in f_omim:
#         if row[1]==disease_name:
#             return row[5]
#     f_omim.close()

def find_disease_and_CUI_Id_from_synonyms(synonyms):
    file = open("omim_onto.csv", "r")
    f_omim = csv.reader(file)
    for row in f_omim:
        if row[2]==synonyms:
            return (row[1], row[5])
    f_omim.close()

# def find_CUI_Id_from_synonyms(synonyms):
#     file = open("omim_onto.csv", "r")
#     f_omim = csv.reader(file)
#     for row in f_omim:
#         if row[2]==synonyms:
#             return row[5]
#     f_omim.close()

def find_disease_ans_synonyms_from_CUI_Id(id_CUI):
    file = open("omim_onto.csv", "r")
    f_omim = csv.reader(file)
    for row in f_omim:
        if row[5]==id_CUI:
            #return (row[1], row[2])
            return row[1]
    f_omim.close()

# def find_synonyms_from_CUI_Id(id_CUI):
#     file = open("omim_onto.csv", "r")
#     f_omim = csv.reader(file)
#     for row in f_omim:
#         if row[5]==id_CUI:
#             return row[2]
#     f_omim.close()

if __name__ == "__main__":
    print(find_synonyms_and_CUI_Id_from_disease("N-ACYL PHOSPHATIDYLETHANOLAMINE-HYDROLYZING PHOSPHOLIPASE D"))
    print(find_disease_and_CUI_Id_from_synonyms("N-ACYL PHOSPHATIDYLETHANOLAMINE PHOSPHOLIPASE D|NAPEPLD"))
    print(find_disease_ans_synonyms_from_CUI_Id("C2239773"))