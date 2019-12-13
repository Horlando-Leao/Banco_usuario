import sqlite3
#CRIAÇÃO DAS TABELAS
#Inicio do DDL: manipulação da tabela
path = r"/home/horlando/Documentos/src/database/"
con = sqlite3.connect(path + r'base.db')
cur = con.cursor()
sql = """ CREATE TABLE users(
id INTEGER PRIMARY KEY,
nome TEXT ,
telefone TEXT,
email TEXT"""
cur.execute(sql)
con.commit()
con.close


#Fim do DDL

