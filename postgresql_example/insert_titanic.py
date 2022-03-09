import psycopg2
import queries as q
import pandas as pd


dbname = "kbeqtfvy"
user = "kbeqtfvy"
password = "XgFkv_aXB47_XtshxZ5g3eIEtlctmrms"
host = "fanny.db.elephantsql.com"

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
conn.commit()
curs = conn.cursor()


def execute_query(curs, query):
    result = curs.execute(query)
    return result


execute_query(curs, q.drop_table)
execute_query(curs, q.create_table)
#execute_query(curs, q.insert_data)

df = pd.read_csv('/Users/chunyanwang/Christine_documents/Data_Science/LambdaSchool/DS-Unit-3-Sprint-2-SQL-and-Databases-master/ds32-3-sprint2-assignments/postgresql_example/titanic.csv')
cols = "survived, pclass, name, sex, age, siblings_or_spouses_aboard, \
    parents_or_children_aboard, fare"

for i, row in df.iterrows():
    sql = "INSERT INTO titanic1 (" + cols + \
        ") VALUES (" + "%s,"*(len(row)-1) + "%s)"
    curs.execute(sql, tuple(row))

#result = curs.fetchall()
#print(result)
conn.commit()
