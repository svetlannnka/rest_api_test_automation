import requests

from support.assertions import assert_valid_schema, assert_status_code, assert_max_response_time, assert_response_key_value


class TestPet:

    def test_get_pet(self):

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
        requests.post(url='https://petstore.swagger.io/v2/pet', json=payload)

        # GET a pet
        response = requests.get(url=f'https://petstore.swagger.io/v2/pet/{pet_id}')

        assert_status_code(response, 200)
        assert_max_response_time(response, 1)
        assert_valid_schema(response.json(), 'pet/v2_pet.json')
        assert_response_key_value(response, 'id', pet_id)
        assert_response_key_value(response, 'name', pet_name)


