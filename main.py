from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

class ProductSChema(BaseModel):
    name:str
    price:int
    stock:int


app = FastAPI()

inventory = [
    {"id": 1, "name": "Laptop", "price": 50000, "stock": 10},
    {"id": 2, "name": "Mouse", "price": 1000, "stock": 50},
    {"id": 3, "name": "Keyboard", "price": 1500, "stock": 20}
]

@app.get("/")
def greeting():
    return ("Hello there!")


@app.get("/product")
def product():
    
    return inventory

@app.get("/search")
def search_product(name: str):
    result=[]
    for item in inventory:
        if name.lower() in item["name"].lower():
            result.append(item)
    return result

@app.delete("/remove_product/{product_id}")
def remove_product(product_id:int):
    for item in inventory:
        if item['id']== product_id:
            inventory.remove(item)


@app.post("/products")
def create_product(new_product: ProductSChema):
    product_dict= new_product.model_dump()
    if inventory:
        new_id=inventory[-1]["id"]+1
    else:
        new_id=1

    product_dict["id"]=new_id
    inventory.append(product_dict)

    return product_dict