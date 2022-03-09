import sqlite3
import queries as q
import pandas as pd

# DB Connect function
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

# Make cursor, execute query, and pull results
def execute_q(connection, query):
    curs = connection.cursor()
    curs.execute(query)
    q_results = curs.fetchall()
    connection.commit()
    curs.close()
    return q_results

# run the code below if this file is run as a script from \
# the Command line
if __name__ == '__main__':
    conn = connect_to_db()
    TOTAL_CHARACTERS = execute_q(conn, q.total_characters)[0][0]
    TOTAL_SUBCLASS = execute_q(conn, q.total_subclass)[0][0]
    TOTAL_ITEMS = execute_q(conn, q.total_items)[0][0]
    WEAPONS = execute_q(conn, q.weapons)[0][0]
    NON_WEAPONS = TOTAL_ITEMS - WEAPONS

    # CHARACTER_ITEMS
    CHARACTER_ITEMS = execute_q(conn, q.character_items)
    # CHARACTER_WEAPONS
    CHARACTER_WEAPONS = execute_q(conn, q.character_items)
    # AVG_CHARACTER_ITEMS
    AVG_CHARACTER_ITEMS = pd.DataFrame(data=CHARACTER_ITEMS)[1].mean()
    # AVG_CHARACTER_WEAPONS
    AVG_CHARACTER_WEAPONS = pd.DataFrame(data=CHARACTER_WEAPONS)[1].mean()

    # print all results
    results = [TOTAL_CHARACTERS, TOTAL_SUBCLASS, TOTAL_ITEMS,
               NON_WEAPONS, CHARACTER_ITEMS[:20], CHARACTER_WEAPONS[:20],
               AVG_CHARACTER_ITEMS, AVG_CHARACTER_WEAPONS]
    print(results)