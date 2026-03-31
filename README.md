# FastAPI Beyond CRUD

Learning the FastAPI framework step by step.

## Branches

### `2-end` — Simple Server

Built a basic FastAPI application covering core request/response concepts:

- **Path parameters** — `GET /greet/{username}` returns a personalized greeting
- **Query parameters** — `GET /search?q=` searches an in-memory user list
- **Optional query parameters** — `GET /greet_optional?q=` with a default fallback
- **Request body (POST)** — `POST /create_user` accepts a JSON body validated by a Pydantic `User` model (`username`, `email`)
- **Request headers** — `GET /get_headers` extracts common HTTP headers (`User-Agent`, `Accept-Encoding`, etc.)

Includes a Jupyter notebook (`notebooks/2_simple_server.ipynb`) and a standalone test script (`notebooks/test_crud.py`) for testing endpoints with the `requests` library.

### `3-end` — Building a CRUD API

Built a full CRUD REST API for a **Books** resource using an in-memory list:

- **Pydantic models** — `Book` model for full book data; `BookUpdateModel` for partial updates (no `id` or `published_date`)
- **`GET /books`** — returns all books, response validated against `List[Book]`
- **`POST /books`** — creates a new book from a JSON body; uses `model_dump()` to convert Pydantic object to dict; returns `201 Created`
- **`GET /book/{book_id}`** — retrieves a single book by ID; raises `404 Not Found` if missing
- **`PATCH /book/{book_id}`** — partially updates a book's fields (title, publisher, page count, language); raises `404 Not Found` if missing
- **`DELETE /book/{book_id}`** — removes a book by ID; returns `204 No Content`
- **HTTP status codes** — uses `fastapi.status` constants and `HTTPException` for proper error responses

Includes a Jupyter notebook (`notebooks/3_building_crud_api.ipynb`) for testing all CRUD endpoints interactively.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
fastapi dev main.py
```
