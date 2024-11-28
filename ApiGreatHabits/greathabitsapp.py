from fastapi import FastAPI


# Construir la aplicacion de FastApi
app = FastAPI()


# Endpoint root de la API
@app.get("/")
def root():
    return {"message": "Bienvenido a la API de mongoDB de TechBridge"}