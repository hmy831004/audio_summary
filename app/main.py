from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    tax: float = None
    
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, Onuii World!"}

@app.get("/onuii")
async def read_root():
    with open('result.txt','r') as f :
        file = f.read()
    
    return {"message": file}
