from fastapi import FastAPI, Path, Query, HTTPException, status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None


class UpdateItem(BaseModel):
    name: Optional[str] =None
    price: Optional[float] = None
    brand: Optional[str] = None

inventory = {}

@app.get('/')
def home():
    return {"Data" : "Test data"}

@app.get('/about')
def about():
    return {"Data" : "About Test data"}

@app.get('/items/{id}')
def get_item_by_id(id: int):
    for id in inventory:
        if inventory[id].id == id:
            return inventory[id]
    return {"data": f"Item with id {id} is in not in our inventory"}


@app.get('/items')
def get_item_by_name(name: str = Query(title="Name", description="Name of the item")):
    for id in inventory:
        if inventory[id].name == name:
            return inventory[id]
    return {"data": f"{name} is in not in our inventory"}


@app.post('/items/{id}')
def create_item(id: int, item: Item):
    if id in inventory:
        return {"Error": f"Item  with id {id}, already exists."}
    inventory[id] = item
    return inventory[id]

@app.put('/items/{id}')
def update_item(id: int, item: UpdateItem):
    if id not in inventory:
        return {"Error": f"Item of id {id},  doesn't  exists."}

    if item.name != None:
        inventory[id].name = item.name
    if item.price != None:
        inventory[id].price = item.price
    if item.brand != None:
        inventory[id].brand = item.brand
    return inventory[id]

@app.delete('/items/{id}')
def delete_item(id: int):
    if id  not in inventory:
        return {"Error": f"Item  with id {id}, Does't exists."}
    del inventory[id]
    return {f"Item of id {id} has been deleted"}