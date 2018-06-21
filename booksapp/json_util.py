import json

with open('booksapp/fixtures/books.json') as json_data:
    b = json.load(json_data)
    cnt = 0
    lset={}
    a=[]
    for i in range(len(b)):
        if b[i]['fields']['language'] in lset:
            continue
        else:
            lset[b[i]['fields']['language']] = 1
    arr = lset.keys()
    for j in range(len(arr)):
        a.append({"pk":j, "model": "booksapp.Language", "fields":{"name": arr[j]}})
    print a
    json_data.close()
with open('booksapp/fixtures/lang.json', 'w') as f:
    json.dump(a, f)
#     for j in range(len(arr)):
#         b.append({"pk":j, "model": "booksapp.Language", "fields":{"name": arr[j]}})
#     json.dump(b, json_data)
#     if len(b) > 0:
#         for i in range(len(b)):
#             temp = b[i]
#             b[i]={"model":"booksapp.Books", "pk":i, "fields":temp}
            # lo.append({"model":"booksapp.Language", "pk":i, "fields":{"language":b[i]['language']}})
            # lo["fields"] = {"name":b[i]['language']}
            # lo["model"] = "booksapp.Language"
            # lo["pk"] = i
    # pprint(b)
    # json_data.seek(0)
    # json.dump(b,json_data,indent=4)
    # json_data.truncate()
    # json_data.close()
    # pprint(o)
    # pprint(lo)

