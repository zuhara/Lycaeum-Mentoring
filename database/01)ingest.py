import csv
import psycopg2

def main(fname):
    conn = psycopg2.connect('dbname=invoice')
    curr = conn.cursor()
    with open(fname) as f:
        reader = csv.reader(f)
        for row in reader:
            print(row,len(row))
            id_,name,date,address,email = row
            curr.execute("""INSERT INTO
                customer(id,name,jdate,address,email)
                VALUES(%s,%s,%s,%s,%s);""",
                (id_,name,date,address,email))
            conn.commit()

if __name__ == "__main__":
    main("data.csv")
