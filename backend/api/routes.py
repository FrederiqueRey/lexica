from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

from api.database import*
from api.models import*

router = APIRouter(
    prefix="/word",
    tags=["word"],
    responses={404: {"description": "I could not find this word !"}}
)

#Affiche une liste de mot trouvée en saisissant le mot grec en caractère latin ou grec
@router.get("/mgl/{m_g_l}", summary= "Retrieve all words in the disctionnary by their Latin or Greek transcriptions (with or without accentuation)",
            #status_code=200,
            response_description="word retrieved!")
async def get_m_g_l(m_g_l):
    word = await find_word(m_g_l)
    return word

"""
#Affiche la liste de toutes les entrées du dictionnaire
@router.get("/", response_model=List[word],
            summary="Affiche la liste de toutes les entrées",
            #status_code=300,
            response_description="words retrieved")

#Cherche une entrée par _id
@router.get("/{id}",
            summary="Get word by its _id",
            response_description="word data retrieved")
async def get_word_data(id):
    word = await retrieve_word(id)
    if word is None:
        raise HTTPException(status_code=404, detail="Word not found")
    return word

#Affiche la première entrée trouvée d'un mot grec saisi en caractère latin
@router.get("/l/{l}", summary= "Retrieve the first word in the dictionary by its latin transcription",
            #status_code=300,
            response_description="word retrieved")
async def get_l(l):
    word = await retrieve_l(l)
    return word

#Affiche l'entrée trouvée en saisissant le mot grec en caractère latin
@router.get("/g/{g}", summary= "Retrieve the first word in the dictionary by its Greek transcription (without accentuation)",
            #status_code=300,
            response_description="word retrieved")
async def get_g(g):
    word = await retrieve_g(g)
    return word

#Ajoute une entrée au dictionnaire
@router.post("/", response_description="word data added into the database")
async def add_word_data(word: word = Body(...)):
    word = jsonable_encoder(word)
    new_word = await add_word(word)
    return ResponseModel(new_word, "word added successfully.")


#Mets à jour une entrée du dictionnaire
@router.put("/{id}")
async def update_word_data(id: str, req: word = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_word = await update_word(id, req)
    if updated_word:
        return ResponseModel(
            "word with ID: {} name update is successful".format(id),
            "word name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the word data.",
    )

#Supprime une entrée du dictionnaire
@router.delete("/{id}", response_description="word data deleted from the database")
async def delete_word_data(id: str):
    deleted_word = await delete_word(id)
    if deleted_word:
        return ResponseModel(
            "word with ID: {} removed".format(id), "word deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "word with id {0} doesn't exist".format(id)
    )
"""

