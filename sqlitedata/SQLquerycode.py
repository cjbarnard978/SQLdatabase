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
            # Ensure data types match the schema
            id_number = int(row['ID Number']) if row['ID Number'] and row['ID Number'].isdigit() else None
            year = int(row['Year']) if row['Year'] and row['Year'].isdigit() else None

            cursor.execute('''
            INSERT OR IGNORE INTO crimes (IDnumber, Date, Characterizations)
            VALUES (?, ?, ?)
            ''', (id_number, row['Year'], row['Characterizations']))
        except (ValueError, TypeError, KeyError) as e:
            print(f"Skipping row due to error: {e}")

# Commit changes and close the connection
conn.commit()
conn.close()
print('Data imported successfully.')