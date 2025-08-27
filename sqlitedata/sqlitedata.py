#Since I am in the process of creating a database from scratch for my current research
#I am using older data already in a CSV to practice the code. I am going to take the data I used for Dr. Burd's mapping project, and create a relational database
#that will address data concerns I anticipate seeing in my current project as it progresses. First, I am going to ask Copilot to break this data
#up into three tables: one that assigns a primary key to each individual person in the database, one that arranges the data based on the presbytery the individual belongs to, 
#and one that pulls out any row with a NULL value present. What I want to interrogate is the way in which NULL values affect the individual tables, and 
#how the NULL values affect the ways in which things "relate" for lack of a better work. I will likely have NULL values pretty consistently moving forward.
#I want to make sure I understand the way that these affect data in part and as a whole. 
#Because this was an ArcGIS table, every entry has an ID number assigned, which I will turn into the INTEGER PRIMARY KEY. I will likely prioritize asking Copilot to standardize the value "unknown"
#across the data and change it to NULL to improve the controlled vocabulary. Then I will ask Copilot to group the data by presbytery using the ID numbers as a foreign key, 
#and ask Copilot to create a third table grouping the data by presbytery using the ID numbers as a foreign key. Ideally, this will create a relational database that can identify gaps in the research.
#This table was created using a digital project that is essentially a tertiary source, and by arranging the data in these ways, I can identify presbyteries or individuals who 
#have been neglected by scholarship.
#I want to try and create the database by hand, because I'm still unsure as to what I want in each table. I think this will help me decide on the logic for that element. 

import sqlite3

print("=== Relational Database Witches in Fife 1563-1662 ===")
print("connection to csv")
conn = sqlite3.connect ('WitchesinFife.db') 
cursor = conn.cursor() 
print('connected to WitchesinFife.db')

print('individuals')
cursor.execute('''
CREATE TABLE IF NOT EXISTS individuals (
    IDnumber INTEGER PRIMARY KEY AUTOINCREMENT,
    First TEXT,
    Last TEXT,
    Date INTEGER
)                     
''')
print('created')

print('locations')
cursor.execute('''
CREATE TABLE IF NOT EXISTS locations (
    IDnumber INTEGER,
    Presbytery TEXT,
    Parish TEXT,
    Settlement TEXT,
    FOREIGN KEY (IDnumber) REFERENCES individuals (IDnumber)
)   
''')
print('created')

print('structure committed')
conn.commit()

# Display the schema of all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print(table[0])
    cursor.execute(f"PRAGMA table_info({table[0]})")
    schema = cursor.fetchall()
    print("Schema:")
    for column in schema:
        print(column)

# Close the connection
conn.close()
print('Connection closed.')

# Reopen the connection to import data
conn = sqlite3.connect('WitchesinFife.db')
cursor = conn.cursor()

# Import data from the CSV file
import csv
with open('/Users/ceciliabarnard/8510/sqlitedata/witchcraftrialsfife.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            # Ensure data types match the schema
            id_number = int(row['ID Number']) if row['ID Number'] and row['ID Number'].isdigit() else None
            year = int(row['Year']) if row['Year'] and row['Year'].isdigit() else None

            # Insert data into the 'individuals' table
            cursor.execute('''
            INSERT INTO individuals (IDnumber, First, Last, Date)
            VALUES (?, ?, ?, ?)
            ''', (id_number, row['First Name'], row['Last Name'], year))

            # Insert data into the 'locations' table
            cursor.execute('''
            INSERT OR IGNORE INTO locations (IDnumber, Presbytery, Parish, Settlement)
            VALUES (?, ?, ?, ?)
            ''', (id_number, row['Presbytery'], row['Parish'], row['Settlement']))
        except (ValueError, TypeError, KeyError) as e:
            print(f"Skipping row due to error: {e}")

# Commit changes and close the connection
conn.commit()
conn.close()
print('Data imported successfully.')





