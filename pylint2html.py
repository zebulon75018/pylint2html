import json
import os
import sys
from jinja2 import Environment, FileSystemLoader

THIS_DIR = os.path.dirname(os.path.abspath(__file__))

inputjson = sys.stdin.readlines()
data = json.loads(''.join([str(x) for x in inputjson]))

pdata = {}
for d in data:
    if d["type"] not in pdata:
        pdata[d["type"]] = []
    pdata[d["type"]].append(d)

j2_env = Environment(loader=FileSystemLoader(THIS_DIR),trim_blocks=True)
print j2_env.get_template('pylint2html.html').render(pdata=pdata)