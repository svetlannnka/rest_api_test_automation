from test_steps.pet_steps import delete_v2_pet, get_v2_pet, generate_pet, post_v2_pet, put_v2_pet
from support.assertions import assert_valid_schema, assert_status_code, assert_max_response_time, assert_response_key_value
from support.client import Client


class TestsPet:

    def test_pet(self):
        client = Client()
        pet = generate_pet()

        # POST a pet
        response = post_v2_pet(client, **pet)
        assert_status_code(response, 200)
        assert_max_response_time(response, 1)
        assert_valid_schema(response.json(), 'pet/v2_pet.json')

        # GET a pet
        response = get_v2_pet(client, pet['id'])
        assert_status_code(response, 200)
        assert_max_response_time(response, 1)
        assert_valid_schema(response.json(), 'pet/v2_pet.json')
        assert_response_key_value(response, 'id', pet['id'])
        assert_response_key_value(response, 'name', pet['name'])

        # PUT a pet
        pet['name'] = 'NewName'
        response = put_v2_pet(client, **pet)
        assert_status_code(response, 200)
        assert_max_response_time(response, 1)
        assert_valid_schema(response.json(), 'pet/v2_pet.json')
        assert_response_key_value(response, 'id', pet['id'])
        assert_response_key_value(response, 'name', pet['name'])

        # DELETE
        response = delete_v2_pet(client, pet['id'])
        assert_status_code(response, 200)
        assert_max_response_time(response, 1)

        # GET a pet
        response = get_v2_pet(client, pet['id'])
        assert_status_code(response, 404)
