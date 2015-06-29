def test_200(client):
    response = client.get("/overview")
    assert response.status_code == 200
    assert response.mimetype == 'text/html'
    assert '<img src="' in response.get_data(as_text=True)
