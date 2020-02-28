import psycopg2
import csv

def main(fname):
    conn = psycopg2.connect('dbname=invoice')
    curr = conn.cursor()
    curr.execute('SELECT * FROM customer')
    rows = curr.fetchall()
    with open(fname,'wt') as f:
        writer = csv.writer(f)
        writer.writerow(('id', 'name', 'date', 'address','email'))
        for i in rows:        
            id_,name,date,address,email = i[0],i[1],i[2],i[3],i[4]
            csv_row = (id_,name,date,address,email)
            writer.writerow(csv_row)
            
    print("Done!!!!!!!!!!!!")
    
if __name__ == "__main__":
    main("data2.csv")
