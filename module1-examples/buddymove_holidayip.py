import sqlite3
import pandas as pd

# write buddymove_holidayiq.csv data into new database buddymove_holidayiq
df = pd.read_csv('buddymove_holidayiq.csv')
conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
df.to_sql('buddymove_holidayiq', conn, if_exists='replace')

# queries of database buddymove_holidayiq
curs = conn.cursor()
print(curs.execute(
    'SELECT COUNT(*) FROM buddymove_holidayiq').fetchall()[0][0])
print(curs.execute('''
    SELECT COUNT(*) FROM buddymove_holidayiq b
    WHERE b.Nature >= 100 AND b.Shopping >= 100
''').fetchall()[0][0])

conn.commit()
curs.close()
