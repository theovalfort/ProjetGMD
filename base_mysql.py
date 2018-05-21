# -*- coding:utf-8 -*-

__nom_fichier__ = "base_mysql"
__author__ = "Capucine"
__date__ = "mai 2018"


# on importe le module MySQLdb
import MySQLdb

# On créé un dictionnaire contenant les paramètres de connexion MySQL
paramMysql = {
    'host'   : 'neptune.telecomnancy.univ-lorraine.fr',
    'user'   : 'gmd-read',
    'passwd' : 'esial',
    'db'     : 'gmd'
}
# Bien respecter les noms des paramètres (host, user, passwd, db)


def find_stitch_id_and_CUI_id_from_side_effect_name(side_effect_name):
    conn = MySQLdb.connect(**paramMysql)
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    result_meddra_freq=[]
    requete ="SELECT stitch_compound_id1, stitch_compound_id2, cui FROM meddra_freq WHERE side_effect_name = '" + side_effect_name + "'"
    cursor.execute(requete)
    for row in cursor.fetchall():
        result_meddra_freq.append(row)

    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    result_meddra_all_indications=[]
    requete ="SELECT stitch_compound_id, cui FROM meddra_all_indications WHERE concept_name = '" + side_effect_name + "'"
    cursor.execute(requete)
    for row in cursor.fetchall():
        result_meddra_all_indications.append(row)

    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    requete ="SELECT stitch_compound_id, cui FROM meddra_all_indications WHERE meddra_concept_name = '" + side_effect_name + "'"
    cursor.execute(requete)
    for row in cursor.fetchall():
        result_meddra_all_indications.append(row)

    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    result_meddra=[]
    requete ="SELECT cui FROM meddra WHERE label = '" + side_effect_name + "'"
    cursor.execute(requete)
    for row in cursor.fetchall():
        result_meddra.append(row)

    conn.close()
    return result_meddra_freq, result_meddra_all_indications, result_meddra

def find_side_effect_name_and_CUI_id_from_stitch_id(stitch_id):
    conn = MySQLdb.connect(**paramMysql)
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    result_meddra_freq=[]
    requete ="SELECT side_effect_name, cui FROM meddra_freq WHERE stitch_compound_id1 = '" + stitch_id + "'"
    cursor.execute(requete)
    for row in cursor.fetchall():
        result_meddra_freq.append(row)


    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    requete ="SELECT side_effect_name, cui FROM meddra_freq WHERE stitch_compound_id2 = '" + stitch_id + "'"
    cursor.execute(requete)
    for row in cursor.fetchall():
        result_meddra_freq.append(row)


    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    result_meddra_all_indications=[]
    requete ="SELECT concept_name, meddra_concept_name, cui FROM meddra_all_indications WHERE stitch_compound_id = '" + stitch_id + "'"
    cursor.execute(requete)
    for row in cursor.fetchall():
        result_meddra_all_indications.append(row)


    return result_meddra_freq, result_meddra_all_indications

def find_stitch_id_and_side_effect_name_from_CUI_id(CUI_id):
    conn = MySQLdb.connect(**paramMysql)
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    result_meddra_freq=[]
    requete ="SELECT stitch_compound_id1, stitch_compound_id2, side_effect_name FROM meddra_freq WHERE cui = '" + CUI_id + "'"
    cursor.execute(requete)
    for row in cursor.fetchall():
        result_meddra_freq.append(row)

    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    result_meddra_all_indications=[]
    requete ="SELECT stitch_compound_id, concept_name, meddra_concept_name FROM meddra_all_indications WHERE cui = '" + CUI_id + "'"
    cursor.execute(requete)
    for row in cursor.fetchall():
        result_meddra_all_indications.append(row)

    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    result_meddra=[]
    requete ="SELECT label FROM meddra WHERE cui = '" + CUI_id + "'"
    cursor.execute(requete)
    for row in cursor.fetchall():
        result_meddra.append(row)

    conn.close()
    return result_meddra_freq, result_meddra_all_indications, result_meddra