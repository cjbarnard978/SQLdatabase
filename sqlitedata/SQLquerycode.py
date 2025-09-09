import sqlite3

print("=== Relational Database Witches in Fife 1563-1662 ===")
print("connection to csv")
conn = sqlite3.connect ('WitchesinFife.db') 
cursor = conn.cursor() 
print('connected to WitchesinFife.db')

cursor.execute('''
CREATE TABLE IF NOT EXISTS crimes (
    IDnumber INTEGER,
    Date INTEGER,
    Characterizations TEXT,
    FOREIGN KEY (IDnumber) REFERENCES individuals (IDnumber)
)   
''')
print('created')
print('structure committed')
conn.commit()

import csv
with open('/Users/ceciliabarnard/8510/sqlitedata/witchcraftrialsfife.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
           
            id_number = int(row['ID Number']) if row['ID Number'] and row['ID Number'].isdigit() else None
            year = int(row['Year']) if row['Year'] and row['Year'].isdigit() else None

            cursor.execute('''
            INSERT OR IGNORE INTO crimes (IDnumber, Date, Characterizations)
            VALUES (?, ?, ?)
            ''', (id_number, row['Year'], row['Characterizations']))
        except (ValueError, TypeError, KeyError) as e:
            print(f"Skipping row due to error: {e}")


conn.commit()
conn.close()
print('Data imported successfully.')

#Query 1: I want to count the number of unknown values in the 
# locations table and arrange them in descending order based on Presbytery
# Ideally this will help me figure out which Presbytery's archives have been least examined.

import sqlite3
conn = sqlite3.connect ('WitchesinFife.db') 
cursor = conn.cursor() 
print ('connected')

query = """
SELECT 
    Presbytery, 
    Parish
FROM locations 
WHERE Parish = unknown
ORDER BY Presbytery
"""
print ('done')

#Query 2


#Query 3