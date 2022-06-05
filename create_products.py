import json
from back_wb.wb_api.models import Product

data = list()

with open("result.json", "r") as stream:
    data = json.loads(stream.read())

for e in data:
    product = Product(
        id=e["id"], 
        category=e["category"], 
        title=e["name"])
    product.price=e["price"]
    product.discount=e["discount"]
    product.count=0
    product.image_url=e["image"]
    product.save()
