# -*- coding:utf-8 -*-

__nom_fichier__ = "base sql"
__author__ = "Capucine"
__date__ = "mars 2018"

import sqlite3


def find_disease_db_id_and_sign_id_from_disease(disease_label):
    conn = sqlite3.connect('hpo_annotations.sqlite')
    cursor = conn.cursor()
    result=[]
    requete ="SELECT disease_db_and_id, sign_id FROM phenotype_annotation WHERE disease_label = '" + disease_label + "'"
    cursor.execute(requete)
    for row in cursor.fetchall():
        result.append(row)
    conn.close()
    return result

def find_disease_and_sign_id_from_disease_db_id(disease_db_id):
    conn = sqlite3.connect('hpo_annotations.sqlite')
    cursor = conn.cursor()
    result=[]
    requete ="SELECT disease_label, sign_id FROM phenotype_annotation WHERE disease_db_and_id = '" + disease_db_id + "'"
    cursor.execute(requete)
    for row in cursor.fetchall():
        result.append(row)
    conn.close()
    return result

def find_disease_db_id_and_disease_from_sign_id(sign_id):
    conn = sqlite3.connect('hpo_annotations.sqlite')
    cursor = conn.cursor()
    result=[]
    requete ="SELECT disease_db_and_id, disease_label FROM phenotype_annotation WHERE sign_id = '" + sign_id + "'"
    cursor.execute(requete)
    for row in cursor.fetchall():
        result.append(row)
    conn.close()
    return result

if __name__ == "__main__":
    #print(find_disease_db_id_and_sign_id_from_disease("100050 AARSKOG SYNDROME, AUTOSOMAL DOMINANT"))
   # print(find_disease_and_sign_id_from_disease_db_id("DECIPHER:17"))
    print(find_disease_db_id_and_disease_from_sign_id("HP:0000098"))

#user1 = cursor.fetchone()
#print(user1)