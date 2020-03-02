''' creating a html file using the datas from the databse without jinja2 '''

import psycopg2
import os

def main(fname):
    conn = psycopg2.connect('dbname=invoice')
    curr = conn.cursor()
    curr.execute('SELECT * FROM customer')
    rows = curr.fetchall()
    headers = [i[0] for i in curr.description]
    
    l = []
    for i in headers:
        s = '<th scope="col" >'+i+'</th>'
        l.append(s)
        
    m = []
    for i in rows:
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
    print('Check the file ',fname)

if __name__ == "__main__":
    main("data2.html")
