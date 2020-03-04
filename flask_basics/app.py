from flask import Flask, render_template, request
 
import models
 
app = Flask("lycaeum")
 
@app.route("/")
def hello():
    session = models.get_session()
    customers = session.query(models.Customer).all()
    return render_template("index.html", customers = customers)
 
@app.route("/invoices", methods = ['POST','GET'])
def invoices():
    cid = request.args.get('cid')
    session = models.get_session()
    if request.method == 'POST': 
        date = request.form['date']
        particulars = request.form['particulars']
        amount = request.form['amount']
        invoice = models.Invoice(particulars = particulars,
                              date = date,
                              amount = amount,
                              customer_id = cid)
        session.add(invoice)
        session.commit()

    customer = session.query(models.Customer).filter(models.Customer.id == cid).first()
    invoices = session.query(models.Invoice).filter(models.Invoice.customer_id == cid).all()
    
    return render_template("invoices.html", customer = customer, invoices = invoices)


if __name__ == '__main__':
    app.run(debug = True)
