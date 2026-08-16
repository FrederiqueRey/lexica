import motor.motor_asyncio
import logging
logging.basicConfig(level=logging.DEBUG)
from bson.objectid import ObjectId


MONGO_DETAILS = "mongodb://mongodb:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.DICS
entries_collection = database.get_collection("entries")


# helpers
def word_helper(word) -> dict:
    return {
        "id": str(word["_id"]),
        "dic": word["dic"],
        "sort_key": word["sort_key"],
        "lang": word["lang"],
        "d": word["d"],
        "m": word["m"],
        "b": word["b"],
        "l": word["l"],
    }


# Retrieve a word by its latin name
async def find_word(dic: str, m_b_l: str) -> dict:
    logging.info(f"Searching words: {m_b_l}.")
    words = []
    async for word in entries_collection.find(
        {"$or": [
            {"b": {"$regex": f"^{m_b_l}"}},
            {"l": {"$regex": f"^{m_b_l}"}},
            {"m": {"$regex": f"^{m_b_l}"}}
        ],
        "dic": dic,
        }
    ).limit(10):
        words.append(word_helper(word))
    logging.debug(f"Result: {words}.")
    return words

async def get_neighbors(dic: str, m: str, n: int = 3) -> dict:
    logging.info(f"Getting the {n} neighbors for: {m}")

    before = []
    async for word in entries_collection.find(
        {"sort_key": {"$lt": m},
        "dic": dic,}
    ).sort("sort_key", -1).limit(n):
        before.append(word_helper(word))
    before.reverse()

    after=[]
    async for word in entries_collection.find(
        {"sort_key": {"$gt": m},
        "dic": dic}
    ).sort("sort_key", 1).limit(n):    
        after.append(word_helper(word))
    
    return {"before": before, "after": after}

# Retrieve a word with a matching ID
async def retrieve_word(id: str) -> dict:
    logging.info(f"Searching id: {id}.")
    word = await entries_collection.find_one({"_id": ObjectId(id)})
    logging.debug(f"Result: {word}.")
    if word:
        return word_helper(word)

async def get_dics() -> list:
    return await entries_collection.distinct("dic")
    