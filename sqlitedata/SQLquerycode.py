import sqlite3
import pandas as pd
print("=== Relational Database Witches in Fife 1563-1662 ===")
print("connection to csv")
conn = sqlite3.connect ('WitchesinFife.db') 
cursor = conn.cursor() 
print('connected to WitchesinFife.db')


#Query 1: I want to count the number of unknown values in the 
# locations table and arrange them by Presbytery in descending order
# Ideally this will help me figure out which Presbytery's archives have been least examined.

import sqlite3
conn = sqlite3.connect ('WitchesinFife.db') 
cursor = conn.cursor() 
print ('connected')


query1 = """
SELECT 
    Presbytery, COUNT(*) as unknown_count 
FROM locations 
GROUP BY Presbytery
ORDER BY unknown_count DESC
"""

cursor.execute(query1)
results1 = cursor.fetchall()
print('unknown parishes')
for row in results1:
    print(row)
#Query 2
#Saint Andrews Presbytery has a significant number of trials. 
# I want to limit the records by St. Andrews as a Presbytery and then join to the individuals column.

query2 = """
SELECT 
    Presbytery
FROM locations
WHERE Presbytery = St. Andrews 
JOIN individuals i ON i.IDnumber = l.IDnumber
"""

cursor.execute(query2)
results2 = cursor.fetchall()
print('unknown parishes')
for row in results2:
    print(row)

#Query 3
#After adding a column to the individuals table that discusses the charges each person faced
#I want to join it to the locations column 
#And order by parish to see the prevalence of each accusation by location.  

query3 = """
SELECT
    Characterizations
FROM crimes 
JOIN locations ON l.IDnumber = c.IDnumber
ORDER By Parish
"""

cursor.execute(query3)
results3 = cursor.fetchall()
print('unknown parishes')
for row in results3:
    print(row)
conn.close()