
import requests

class TestPet1:

    def test_pet_creation1(self):
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
        response = requests.post(
            url='https://petstore.swagger.io/v2/pet',
            json=payload
        )
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 1
        assert response.json()['id'] == pet_id

        # GET a pet
        response = requests.get(
            url=f'https://petstore.swagger.io/v2/pet/{pet_id}'
        )
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 1
        assert response.json()['id'] == pet_id

