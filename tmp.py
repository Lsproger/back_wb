import json
import random
from unicodedata import category


data1 = None
data2 = None
result = list()

with open("database.json", "r") as stream:
    data1 = json.loads(stream.read())
    for e in data1:
        print(e)
        break

with open("data2.csv", "r") as stream:
    data2 = list(map(lambda x: list(map(lambda y: y.strip(), x.strip().split(","))), stream.readlines()))
    for e in data2:
        print(e)
        break


idd = 0


for e in data1:
    el = {
        "category": e.get("category"),
        "name": data2[idd][2].replace(r"%2C", ","),
        "discount": int(e.get("discount")),
        "price": float(data2[idd][3]),
        "count": 0,
        "image": data2[idd][1],
        "id": int(e.get("id"))
    }
    idd += 1
    result.append(el)


# for e in data1:
#     el = {
#         "category": e.get("category"),
#         "name": e.get("name"),
#         "discount": int(e.get("discount")),
#         "price": float(e.get("price")),
#         "count": 0,
#         "image": e.get("image"),
#         "id": int(e.get("id"))
#     }
#     result.append(el)


# id = 101
# for e in data2:
#     el = {
#         "category": e[0],
#         "name": e[2].replace(r"%2C", ","),
#         "discount": int(random.random() * 30),
#         "price": float(e[3]),
#         "count": 0,
#         "image": e[1],
#         "id": id
#     }
#     id += 1
#     result.append(el)

with open("result.json", "w") as stream:
    stream.write(json.dumps(result).encode("utf-8").decode("utf-8"))
# print(result)