# Ancient Languages Dictionary API

A REST API serving classical lexicons, starting with the **Liddell-Scott-Jones Greek Lexicon (LSJ)** and the ** Brown, Driver, Briggs, A Hebrew and English Lexicon of the Old Testament** Built as an open platform intended to host multiple dictionaries (LSJ Greek, BDB Hebrew, Aramaic, Bailly, Gaffiot, and more).

## Stack

| Layer | Technology |
|---|---|
| API | FastAPI (Python) |
| Database | MongoDB + Motor (async driver) |
| Frontend | Vue 3 + Tailwind CSS |
| Runtime | Docker Compose |

## Project structure

```
.
├── backend/
│   ├── api/
│   │   ├── app.py        # FastAPI app, CORS, startup
│   │   ├── routes.py     # API routes
│   │   ├── database.py   # MongoDB queries
│   │   └── models.py     # Pydantic models
│   ├── tests/
│   │   └── test_routes.py
│   └── requirements.txt
├── frontend/
│   └── src/
│       └── App.vue       # Vue 3 single-page app
├── data/
│   └── lsj.json    # dictionnary lsj
│   └── bdb.json    # dictionnary bdb
└── docker-compose.yml
```

## API endpoints

| Method | Route | Description |
|---|---|---|
| GET | `/dics` | List all available dictionaries. |
| GET | `/{dic}/search/{term}` | Search entries by headword, transliteration, or base form. Returns up to 10 results. |
| GET | `/{dic}/{id}` | Get an entry by its MongoDB `_id`. |
| GET | `/{dic}/{id}/neighbors` | Get the `n` entries before and after a given entry (default `n=3`). |

`{dic}` is the dictionary identifier as stored in MongoDB (e.g. `LSJ`, `BDB`).

Interactive documentation available at `http://localhost:8000/docs`.

## Adding a dictionary

Each dictionary is a JSON array of entries imported into the `DICS.entries` MongoDB collection. The `dic` field is the discriminator — the API picks up any new dictionary automatically.

### Entry structure

```json
{
  "sort_key": 1,
  "dic": "LSJ",
  "lang": "Greek",
  "m": ["ἀγαθός"],
  "b": ["αγαθος"],
  "l": ["agathos"],
  "d": "<p><b>ἀγαθός</b> HTML definition...</p>"
}
```

| Field | Type | Description |
|---|---|---|
| `sort_key` | int | Sequential integer used for neighbor queries. Must be unique within a dictionary. |
| `dic` | str | Dictionary identifier (`LSJ`, `BDB`, `Bailly`…). Used in all API routes. |
| `lang` | str | Language of the entry (`Greek`, `Hebrew`, `Aramaic`…). |
| `m` | list[str] | Headword(s) in the original script. Used for search. |
| `b` | list[str] | Base form(s) without diacritics. Used for search. |
| `l` | list[str] | Latin transliteration(s). Used for search. |
| `d` | str | Full definition, may contain HTML. |

### Import steps

1. Prepare your `mydict.json` file following the structure above.
2. Add it to `data/` and mount it in `docker-compose.yml`:
```yaml
volumes:
  - ./data/mydict.json:/docker-entrypoint-initdb.d/mydict.json
```
3. Add a `mongoimport` line in the `command` block:
```bash
mongoimport --db DICS --collection entries --file /docker-entrypoint-initdb.d/mydict.json --jsonArray
```
4. Restart from scratch:
```bash
docker compose down && docker compose up
```

The new dictionary appears automatically in `/dics` and is searchable via `/{dic}/search/{term}`.

## Run locally

```bash
docker compose up
```

- API: `http://localhost:8000`
- Frontend: `http://localhost:5174`

## Data import

The Dictionaries source must be placed at `data/lsj.json`. The `docker-compose.yml` imports it automatically on first run via `mongoimport`.

To reimport from scratch (drops the existing collection):

```bash
docker compose down -v
docker compose up
```

## Run tests

```bash
cd backend
pip install pytest pytest-asyncio "anyio[trio]" httpx
pytest tests/ -v
```

Tests use mocked database functions — no running MongoDB instance required.

## License

The Liddell-Scott-Jones lexicon is in the public domain. Source data from the [Perseus Digital Library](http://www.perseus.tufts.edu/).
