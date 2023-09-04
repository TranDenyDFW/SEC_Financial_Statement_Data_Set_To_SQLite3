import pandas as pd
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('secdb.db')

tables = ['sub', 'tag', 'num', 'pre']

# Load your datasets
for t in tables:
    pd = pd.read_csv(f'{t}.txt', delimiter='\t')
    df.to_sql(t, conn, if_exists='replace', index=False)

# Commit the transaction and close the connection
conn.commit()
conn.close()
