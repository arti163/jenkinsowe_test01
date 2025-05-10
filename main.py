from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

@app.get("/")
async def read_item(param: str):
	return {"otrzymany_parametr": param}

client = TestClient(app)

def test_read_item_with_param():
    response = client.get("/?param=testowa_wartosc")
    assert response.status_code == 200
    assert response.json() == {"otrzymany_parametr": "testowa_wartosc"}

def test_read_item_without_param():
    response = client.get("/")
    assert response.status_code == 422 # FastAPI automatycznie waliduje brak wymaganego parametru
