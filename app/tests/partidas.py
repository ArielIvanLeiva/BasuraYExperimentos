from fastapi.testclient import TestClient
from main import app
from schemas.partidas import PartidaCreada

client = TestClient(app)

fake_db = {
    
}

def test_read_main():
    client.post("/partidas/", json=PartidaCreada('Juan', False, ))
    response = client.get("/partidas/")
    assert response.status_code == 200
    print(response.json())
    print("Success")
    
test_read_main()