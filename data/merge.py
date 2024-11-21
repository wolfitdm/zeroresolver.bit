import json 

files=['./0/names.json','./1/names.json']

data_end={}

for file in files:
    with open(file) as f:
         data = json.load(f)
         data_end.update(data)

with open('namesx.json', 'w') as f:
    f.write(json.dumps(data_end, indent=2, sort_keys=True))