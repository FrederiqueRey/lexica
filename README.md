# Ancient Languages Dictionary API

A REST API serving classical lexicons, starting with the **Liddell-Scott-Jones Greek Lexicon (LSJ)**. Built as an open platform intended to host multiple dictionaries (LSJ Greek, BDB Hebrew, CAL Aramaic, and more).

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
│   └── lsj-mongodb.py    # Import script
└── docker-compose.yml
```

## API endpoints

All routes are prefixed with `/word`.

| Method | Route | Description |
|---|---|---|
| GET | `/word/mgl/{term}` | Search by Latin transcription, Greek (unaccented), or Greek (accented). Returns up to 10 results. |
| GET | `/word/{id}` | Get a word entry by its MongoDB `_id`. |
| GET | `/word/{id}/neighbors` | Get the `n` words before and after a given entry (default `n=3`). |

Interactive documentation available at `http://localhost:8000/docs`.

## Run locally

```bash
docker compose up
```

- API: `http://localhost:8000`
- Frontend: `http://localhost:5174`

## Data import

The LSJ JSON source must be placed at `data/LSJ.Words.json`. The `docker-compose.yml` imports it automatically on first run via `mongoimport`.

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
