import psycopg2
from utilities.configurations import db_connect

print("Connecting to the postgreSQL database...")
conn = db_connect()

# create a cursor
cur = conn.cursor()

# execute a statement
cur.execute('SELECT * FROM restaurants')

# fetch one row
# row = cur.fetchone()
# print(row)

# fetch all the rows
# rows = cur.fetchall()
# print(rows)

# fetch some rows
# rows = cur.fetchmany(2)
# print(rows)
# rows = cur.fetchmany(2)
# print(rows)

# iterate over the rows
rows = cur.fetchall()
for row in rows:
    print(f'{row[1]} - {row[2]} - {row[3]}')


cur.close()