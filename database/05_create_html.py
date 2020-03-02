''' Taking values from the database and creating a html file with the datas  '''

import psycopg2
import jinja2
import os

def main(fname):
    conn = psycopg2.connect('dbname=invoice')
    curr = conn.cursor()
    curr.execute('SELECT * FROM customer')
    rows = curr.fetchall()
    headers = [i[0] for i in curr.description]
    
    search_path = os.getcwd()
    templateLoader = jinja2.FileSystemLoader(searchpath=search_path)
    templateEnv = jinja2.Environment(loader=templateLoader)
    template = templateEnv.get_template("template.html")
    str = template.render(datas = rows,headers = headers)  

    with open(fname,'wt') as f:
        f.write(str)

    print("DONE !!!!!!")
    print('Check the file ',fname)

if __name__ == "__main__":
    main("data.html")

    
