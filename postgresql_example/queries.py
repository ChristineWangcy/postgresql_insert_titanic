import pandas as pd
#df = pd.read_csv('titanic.csv')
drop_table = '''DROP TABLE IF EXISTS titanic1'''
create_table = '''
CREATE TABLE IF NOT EXISTS titanic1 (
id SERIAL PRIMARY KEY,
survived INT,
pclass INT,
name VARCHAR(500) NOT NULL,
sex VARCHAR(500),
age INT,
siblings_or_spouses_aboard INT,
parents_or_children_aboard INT,
fare FLOAT
)
'''

insert_data = '''
INSERT INTO titanic (survived, pclass, \
    name, sex, age, siblings_or_spouses_aboard, \
        parents_or_children_aboard, fare)
VALUES (1, 1, 'Alex', 'F', 49, 2, 0, 765.9)
'''
