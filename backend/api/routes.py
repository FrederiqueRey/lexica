from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from api.database import*
from api.models import*
"""
from api.database import (
    add_word,
    delete_word,
    retrieve_word,
    retrieve_words,
    update_word,
)
from api.models import (
    ErrorResponseModel,
    ResponseModel,
    word,
    #UpdatewordModel,
)
"""
router = APIRouter(
    prefix="/word",
    tags=["words"],
    responses={404: {"description": "I could not find this word !"}}
)

#Affiche la liste de toutes les entrées du dictionnaire
@router.get("/", response_model=List[word],
            summary="Affiche la liste de toutes les entrées",
            status_code=300,
            response_description="words retrieved")
async def get_words():
    """
    Affiche l'ensemble des entrées du dictionnaire. Cependant... comme il y a beaucoup d'entrée
    j'ai l'impression que ça fait tout planter dans le swag parce que ça sort en print.
    """
    words = await retrieve_words()
    return words


#Affiche l'entrée trouvée en saisissant le mot grec en caractère latin
@router.get("/{l}", summary= "Retrieve word by its latin transcription",
            status_code=300,
            response_description="word retrieved")
async def get_l(l):
    word = await retrieve_l(l)
    return word
    """
    if word:
        return ResponseModel(word, "word data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "word doesn't exist.")
    """

#Affiche une liste de mot trouvée en saisissant le mot grec en caractère latin ou grec
@router.get("/{m_g_l}", summary= "Retrieve word by its latin transcription",
            status_code=300,
            response_description="word retrieved")
async def get_m_g_l(m_g_l):
    word = await find_word(m_g_l)
    return word

#Cherche une entrée par _id
@router.get("/{id}",
            summary="Get word by its _id",
            response_description="word data retrieved")
async def get_word_data(id):
    word = await retrieve_word(id)
    return word
    """
    if word:
        return ResponseModel(word, "word data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "word doesn't exist.")
    """


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


