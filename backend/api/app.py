from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
from api.database import client, entries_collection, get_dics  # Import the client from database.py

app = FastAPI()
app.include_router(router)

origins = [
    "http://localhost:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await entries_collection.create_index("dic")
    await entries_collection.create_index("sort_key")
    await entries_collection.create_index("l")
    await entries_collection.create_index("b")
    await entries_collection.create_index("m")

@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the Dictionaries api"}

@app.get("/dics", tags=["dics"])
async def list_dics():
    return await get_dics()

@app.get("/test-mongo", tags=["Test"])
async def test_mongo():
    try:
        # Check if the MongoDB client is connected
        await client.admin.command("ping")
        return {"message": "MongoDB connection successful"}
    except Exception as e:
        return {"message": f"MongoDB connection failed: {str(e)}"}
