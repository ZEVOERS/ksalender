from fastapi import FastAPI
from routes import dbs, auth, users
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
    "https://mkdb.zevoers.dev",
    "https://mkdb.dev",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def srfunc():
    return "Developed by _baek.jw"


app.include_router(auth.router)
app.include_router(users.router)
app.include_router(dbs.router)
