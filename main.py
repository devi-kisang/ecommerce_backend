from fastapi import FastAPI,HTTPException

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