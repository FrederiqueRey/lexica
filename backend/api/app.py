from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
from api.database import client  # Import the client from database.py

app = FastAPI()
app.include_router(router)

# app.mount('/', StaticFiles(directory='app/frontend', html=True))

# NEW
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost/:1",
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


@app.get("/test-mongo", tags=["Test"])
async def test_mongo():
    try:
        # Check if the MongoDB client is connected
        await client.admin.command("ping")
        return {"message": "MongoDB connection successful"}
    except Exception as e:
        return {"message": f"MongoDB connection failed: {str(e)}"}
