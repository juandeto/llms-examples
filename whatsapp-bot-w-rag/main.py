from fastapi import FastAPI
from dotenv import load_dotenv
from router import webhook
load_dotenv()


app = FastAPI()
app.include_router(webhook.router)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

