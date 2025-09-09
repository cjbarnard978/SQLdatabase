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

query = """
SELECT 
    p.Presbytery, 
    m.Parish
FROM locations l
WHERE m.Parish = unknown
COUNT unknown
ORDER BY p.Presbytery
ARRANGE desc
"""
print ('done')

#Query 2
#Saint Andrews Presbytery has a significant number of trials. 
# I want to limit the records by St. Andrews as a Presbytery and then join to the individuals column.

query = """
SELECT 
    p.Presbytery
FROM locations l
WHERE p.Presbytery = St. Andrews 
JOIN individuals i ON i.IDnumber = l.IDnumber
"""
print('joined')

#Query 3
#After adding a column to the individuals table that discusses the charges each person faced
#I want to join it to the locations column 
#And order by parish to see the prevalence of each accusation by location.  

query = """
SELECT
    ch.Characterizations
FROM crimes c
JOIN locations l ON l.IDnumber = c.IDnumber
ORDER By p.Parish
"""
print('ordered')