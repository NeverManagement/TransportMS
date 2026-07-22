from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "TransportMS funcionando correctamente UwU"}