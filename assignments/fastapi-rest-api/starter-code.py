from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str
    price: float

items = {}
next_id = 1

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI item service"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]

@app.post("/items")
def create_item(item: Item):
    global next_id
    item_data = item.dict()
    item_data["id"] = next_id
    items[next_id] = item_data
    next_id += 1
    return item_data
