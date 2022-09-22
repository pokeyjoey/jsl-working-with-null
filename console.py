import sqlite3
import pandas as pd

# get db connections
conn = sqlite3.connect('crm.db')
cursor = conn.cursor()

# get the data
url = "https://raw.githubusercontent.com/data-eng-10-21/case-when/main/coerced_persons.csv"
df = pd.read_csv(url)
print('print the dataframe first 2 records from the csv')
print(df[:2])
print('')
print('')

# load the persons table
#df.to_sql('persons', conn, index = False)

# read the table
print('SELECT * FROM persons WHERE first_name IS NULL LIMIT 3')
print(pd.read_sql("SELECT * FROM persons WHERE first_name IS NULL LIMIT 3;", conn))
print('')
print('')


print('Replace any null values in first name with the string unknown')
query = """
    SELECT COALESCE(first_name, 'Unknown') as first_name, last_name
    FROM persons
    LIMIT 6;"""
print(query)
print(pd.read_sql(query, conn))
print('')
print('')

print('Use a persons last name when the first name is not present')
query = """
    SELECT COALESCE(first_name, last_name) as first_name, last_name
    FROM persons
    LIMIT 6"""
print(query)
print(pd.read_sql(query, conn))
print('')
print('')

print('Convert empty strings to null values')
query = """
    SELECT id, NULLIF(first_name, '') as first_name, last_name
    FROM persons
    LIMIT 3"""
print(query)
print(pd.read_sql(query, conn))

print('Convert empty strings to null values')
query = """
    SELECT id, NULLIF(first_name, '') as name, last_name
    FROM persons
    WHERE name IS NULL LIMIT 3"""
print(query)
print(pd.read_sql(query, conn))
print(' ')
print(' ')

print('convert empty strings to null with NULLIF, then use COALESCE to convert nulls  to unknown')
query = """
    SELECT COALESCE(NULLIF(first_name, ' '), 'Unknown')  as first_name, last_name
    FROM persons
    LIMIT 6;"""
print(query)
print(pd.read_sql(query, conn))

