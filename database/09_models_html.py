import random
 
import faker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine, ForeignKey, BLOB, Date, Boolean, Table
from sqlalchemy.orm import sessionmaker, relationship

import csv
 
Base = declarative_base()
 
class Customer(Base):
    __tablename__ = "invoice_customer"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    jdate = Column(Date)
    address = Column(String)
    email = Column(String)
    invoices = relationship('Invoice', backref="customer")
 
class Invoice(Base):
    __tablename__ = "invoice_invoice"
    id = Column(Integer, primary_key = True)
    particulars = Column(String)
    date = Column(Date)
    amount = Column(Integer)
    customer_id = Column(Integer, ForeignKey('invoice_customer.id'))
 
def create_db():
    url = "postgres:///invoice"
    #url = "sqlite:///invoice_db.sqlite"
    engine = create_engine(url)
    Base.metadata.create_all(engine)
 
def get_session():
    url = "postgres:///invoice"
    #url = "sqlite:///invoice_db.sqlite"
    engine = create_engine(url)
    Session = sessionmaker(bind = engine)
    session = Session()
    return session

def main(fname):
    create_db()
    
    f = faker.Faker()
    session = get_session()
    for i in range(10):
        c = Customer(name = f.name(),
                     jdate = f.date(),
                     address = f.address(),
                     email = f.email())
        session.add(c)
        for j in range(2):
            invoice = Invoice(particulars = f.sentence(),
                              date = f.date(),
                              amount = random.randint(10, 99),
                              customer = c)
            session.add(invoice)
    session.commit()
    print('Datas added ......')
    
    results = session.query(Customer).all()
    print(results)
    
    
    headers = ['id', 'name', 'date', 'address','email']
    
    l = []
    for i in headers:
        s = '<th scope="col" >'+i+'</th>'
        l.append(s)
        
    res = []
    for i in results:
        res.append([i.id,i.name,i.jdate,i.address,i.email])
    
    m = []
    for i in res:
        m.append('<tr>')
        for j in i:
            s = '<td>'+str(j)+'</td>'
            m.append(s)
        m.append('</tr>')
        
    strr = '''<table class=\"table\">
      <thead><tr>'''+'\n'.join(l)+'''</tr></thead>
      <tbody>'''+'\n'.join(m)+'''</tbody></table>'''
       
    with open(fname,'wt') as f:
        f.write(strr)

    print("DONE !!!!!!")

if __name__ == "__main__":
    main("data2.html")
