import json
import os
import sys
from jinja2 import Environment, FileSystemLoader
import sqlite3
import datetime

inputjson = sys.stdin.readlines()
data = json.loads(''.join([str(x) for x in inputjson]))


################################################################3
conn = sqlite3.connect('pylint.db')  # You can create a new database by changing the name within the quotations
c = conn.cursor() # The database will be saved in the location where your 'py' file is saved

# Create table - CLIENTS
c.execute('''CREATE TABLE IF NOT EXISTS pylint
             (message text,
              obj text, 
              column integer,
              path text,
              line integer,
              type text,
              symbol text,
              module text,
              session  integer,
              t timestamp DEFAULT CURRENT_TIMESTAMP)''')
conn.commit()
cur = conn.cursor()
# get the session number.
cur.execute("SELECT MAX(session) FROM pylint")
row = cur.fetchone()
session = 0
if row[0] is not None:
    session = row[0] + 1

# insert data in sql...
sql = ''' INSERT INTO pylint(message,obj,column,path,line,type,symbol,module,session)
              VALUES(?,?,?,?,?,?,?,?,?) '''
cur = conn.cursor()
for d in data:
    cur.execute(sql, [d["message"],d["obj"],d["column"],d["path"],d['line'],d["type"],d["symbol"],d["module"],session])
    conn.commit()

conn.close()
############################################################3
THIS_DIR = os.path.dirname(os.path.abspath(__file__))

pdata = {}
for d in data:
    if d["type"] not in pdata:
        pdata[d["type"]] = []
    pdata[d["type"]].append(d)

j2_env = Environment(loader=FileSystemLoader(THIS_DIR),trim_blocks=True)
print j2_env.get_template('pylint2html.html').render(pdata=pdata)