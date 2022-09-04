# Fastapi-Test-02-2022
Very preliminary test of connection between Fastapi and mongodb, based on the tutorial : https://testdriven.io/blog/fastapi-mongo/ and Sophie Robert slides Fastapi_handson. 




For the following error : `from app.server.routes.student import router as StudentRouter ModuleNotFoundError: No module named 'app'`  
    -> Don't forget to create the virtual environment.   
      `python3 -m venv venv`   
      `source venv/bin/activate`
    
    -> For a first instalation
      `pip install -e .`
      `pip install -r requirements.txt`

    -> lancer l'api
      `launchapi`     





###Github###



###Docker###



Pour installer

**Lancer le backend**
1. Lancer l'environnement virtuel
      `$ python3.9 -m venv venv`   
      `$ source venv/bin/activate`   
      `$ export PYTHONPATH=$PWD`
2. Lancer le backend
  python3.9 app/main.py

3. Tester l'api
  http://0.0.0.0:8000/docs

**Lancer le Frontend**
1. Ouvrir un terminal dans app/frontend
  npm run dev
2. Tester le frontend
  http://localhost:3000/ 


**A Installer comme éditeur de texte collaboratif**
https://etherpad.org
https://github.com/ether/etherpad-lite-jquery-plugin/blob/master/index.html
https://github.com/ether/etherpad-lite


**Oline Tools**
Convertisseur XML to JSON
https://codebeautify.org/xmltojson

**Gestion des buggs**
On Mac OS, for the SSL certificate error -> run the following commands (if you connect to the mongodb+srv://<username>:<password>@test1.d66q5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority)
    `CERT_PATH=$(python3.9 -m certifi)`
    `export SSL_CERT_FILE=${CERT_PATH}`
    `export REQUESTS_CA_BUNDLE=${CERT_PATH}`

In the tutorial the following lines are missing in the app.server.routes.student file:
  from app.server.database import*
  from app.server.models.student import*

For the ObjectId syntax error message -> mais ça ne marche toujours pas :-(

from bson.objectid import ObjectId

class PyObjectId(ObjectId):
    """ Custom Type for reading MongoDB IDs """
    @classmethod
    def __get_validators__(cls):
        yield cls.validate
    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)
    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class word(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        json_encoders = {ObjectId: str}


