import motor.motor_asyncio
import logging
logging.basicConfig(level=logging.DEBUG)
from bson.objectid import ObjectId


# MONGO_DETAILS = "mongodb://localhost:27017"
MONGO_DETAILS = "mongodb://mongodb:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.LSJ
word_collection = database.get_collection("Words")


# helpers
def word_helper(word) -> dict:
    return {
        "id": str(word["_id"]),
        "d": word["d"],
        "m": word["m"],
        "g": word["g"],
        "l": word["l"],
    }


# Retrieve a word by its latin name
async def find_word(m_g_l: str) -> dict:
    logging.info(f"Searching words: {m_g_l}.")
    words = []
    async for word in word_collection.find(
        {"$or": [
            {"g": {"$regex": f"^{m_g_l}"}},
            {"l": {"$regex": f"^{m_g_l}"}},
            {"m": {"$regex": f"^{m_g_l}"}}
        ]}
    ).limit(10):
        words.append(word_helper(word))
    logging.debug(f"Result: {words}.")
    return words

"""
# Retrieve a word by its latin name
async def retrieve_l(l: str) -> dict:
    logging.info(f"Searching word: {l}.")
    word = await word_collection.find_one({"l": l})
    logging.debug(f"Result: {word}.")
    if word:
        return [word_helper(word)]
    else:
        return []

# Retrieve a word by its Greek name
async def retrieve_g(g: str) -> dict:
    logging.info(f"Searching word: {g}.")
    word = await word_collection.find_one({"g": g})
    logging.debug(f"Result: {word}.")
    if word:
        return [word_helper(word)]
    else:
        return []

# Retrieve all words present in the database
async def retrieve_words():
    words = []
    async for word in word_collection.find():
        words.append(word_helper(word))
    logging.debug(f"Liste of words: {words}.")
    return words

# Add a new word into to the database
async def add_word(word_data: dict) -> dict:
    word = await word_collection.insert_one(word_data)
    new_word = await word_collection.find_one({"_id": word.inserted_id})
    logging.debug(f"The word {new_word} has been added.")
    return word_helper(new_word)


# Retrieve a word with a matching ID
async def retrieve_word(id: str) -> dict:
    logging.info(f"Searching id: {id}.")
    word = await word_collection.find_one({"_id": ObjectId(id)})
    logging.debug(f"Result: {word}.")
    if word:
        return word_helper(word)

# Update a word with a matching ID
async def update_word(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    logging.info(f"l'id {id} will be updated.")
    word = await word_collection.find_one({"_id": ObjectId(id)})
    if word:
        updated_word = await word_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_word:
            logging.debug(f"The word {updated_word} has been updated.")
            return True
        return False


# Delete a word from the database
async def delete_word(id: str):
    word = await word_collection.find_one({"_id": ObjectId(id)})
    if word:
        await word_collection.delete_one({"_id": ObjectId(id)})
        logging.debug(f"The word {word} has been deleted.")
        return True
"""