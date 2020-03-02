''' Fetch values from the database and print in the terminal  '''

import psycopg2

def main():
    conn = psycopg2.connect('dbname=invoice')
    curr = conn.cursor()
    curr.execute('SELECT * FROM customer')
    rows = curr.fetchall()
    for i in rows:
        print(i)

if __name__ == "__main__":
    main()
