import requests

class TestPet:

    def test_pet_creation(self):

        pet_id, pet_name = 21435431254521, 'Garfield'
        payload = {
            "id": pet_id,
            "name": "Garfield",
            "category": {
                "name": "cats"
            },
            "status": "available"
        }

        # POST a pet
        response = requests.post(url='https://petstore.swagger.io/v2/pet', json=payload)

        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 1
        # Let's verify ALL required data is returned
        assert response.json()['id'] == pet_id
        assert response.json()['name'] == pet_name
        assert 'status' in response.json()
        assert 'category' in response.json()
        assert 'name' in response.json()['category']
        assert 'photoUrls' in response.json()
        assert 'tags' in response.json()
