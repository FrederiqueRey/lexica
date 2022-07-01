from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router

app = FastAPI()
app.include_router(router)

#app.mount('/', StaticFiles(directory='app/frontend', html=True))

# NEW

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost/:1"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the Lidell Scott Dictionary api"}

"""
Test d'application d'une entrée get
@app.get("/word_test")
async def indicate_word():
    return {"message": "This is the first word of the dictionary"}
"""

