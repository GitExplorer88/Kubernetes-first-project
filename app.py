from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is running successfully!"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"greeting": f"Hello, {name}!"}
