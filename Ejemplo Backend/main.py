from fastapi import FastAPI
from pydantic import BaseModel

class UserModel(BaseModel):
    email: str
    matricula: int
    puntos_extra: int = 0
    representativo: str | None = None

app = FastAPI()

@app.get("/")
def get_root():
    return {"message": "hello world!"}

# Path parameter
@app.get("/acceso/{id}/subacceso/{subid}")
def get_acceso(id : int, subid : int):
    return {"message": f"Tu id asignado es: {id}"}

# Query parameter
# http://127.0.0.1:8000/query?usuario=Aram&creditos=100
@app.get("/query")
def get_query(usuario : str = "N/A", creditos : int = 0):
    return {
        "Usuario": usuario,
        "Créditos": creditos
    }

@app.post("/user")
def post_user(user : UserModel):
    return {
        "Correo": user.email,
        "Matrícula": user.matricula,
        "Puntos extra": user.puntos_extra,
        "Representativo": user.representativo
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)