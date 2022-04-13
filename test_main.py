from main import translate, app

def test_main_menu():
    response = app.test_client().get("/")
    assert response.status_code == 200

    
def test_predict():
    response = app.test_client().get("/predict")
    assert response.status_code == 200
    
