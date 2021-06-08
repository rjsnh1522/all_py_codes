import io, json
data = [1,23,2423,4234,4324324,4234,2,23,556,66,677,'sd']
kd = {v: k for v, k in enumerate(data)}
# print(kd)
with io.open('data.json', 'w', encoding='utf-8') as f:
  f.write(json.dumps(kd, ensure_ascii=False))



with io.open('data.json', 'r') as f:
    datastore = json.load(f)
    print(datastore["0"])



print(datastore)