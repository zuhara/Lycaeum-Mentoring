from faker import Faker 
import psycopg2

def main():
    fake = Faker()
    conn = psycopg2.connect('dbname=invoice')
    curr = conn.cursor()
    
    for i in range(1,5001):
        name,date,address,email = fake.name(),fake.date(),fake.address(),fake.email()
        curr.execute("""INSERT INTO
                customer(id,name,jdate,address,email)
                VALUES(%s,%s,%s,%s,%s);""",(i,name,date,address,email))
        conn.commit()
    print("Its done")

if __name__ == "__main__":
    main()
