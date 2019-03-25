import json
imp= raw_input("intorodu ce cauti: ")
json_obj=None
with open ("file.json",'r') as f:
    content = f.read()
    json_obj=json.loads(content)

result = []
for a in json_obj:
    if imp in a:
        result.append(a)

print(result)

with open("output.json","w") as w:
    w.write(json.dumps(result))
