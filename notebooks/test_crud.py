import requests

BASE_URL = "http://127.0.0.1:8000"


def test_root():
    print("=== GET / ===")
    resp = requests.get(f"{BASE_URL}/")
    print(f"Status: {resp.status_code}")
    print(f"Body:   {resp.json()}")
    print()


def test_greet(username: str):
    print(f"=== GET /greet/{username} ===")
    resp = requests.get(f"{BASE_URL}/greet/{username}")
    print(f"Status: {resp.status_code}")
    print(f"Body:   {resp.json()}")
    print()


def test_search(query: str):
    print(f"=== GET /search?q={query} ===")
    resp = requests.get(f"{BASE_URL}/search", params={"q": query})
    print(f"Status: {resp.status_code}")
    print(f"Body:   {resp.json()}")
    print()


def test_greet_optional(query: str | None = None):
    label = f"q={query}" if query else "no query"
    print(f"=== GET /greet_optional ({label}) ===")
    params = {"q": query} if query else {}
    resp = requests.get(f"{BASE_URL}/greet_optional", params=params)
    print(f"Status: {resp.status_code}")
    print(f"Body:   {resp.json()}")
    print()


def test_create_user(username: str, email: str):
    print(f"=== POST /create_user ===")
    payload = {"username": username, "email": email}
    print(f"Sending: {payload}")
    resp = requests.post(f"{BASE_URL}/create_user", json=payload)
    print(f"Status:  {resp.status_code}")
    print(f"Body:    {resp.json()}")
    print()


if __name__ == "__main__":
    test_root()

    test_greet("Sungsoon")

    test_search("Joey")
    test_search("Unknown")

    test_greet_optional("Phil")
    test_greet_optional()

    test_create_user("NewUser", "newuser@example.com")

    # verify the new user shows up in search
    test_search("NewUser")
