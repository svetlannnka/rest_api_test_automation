import pytest
from requests.models import Response
from test_steps.pet_steps import delete_v2_pet, get_v2_pet, generate_pet, post_v2_pet, put_v2_pet
from support.assertions import assert_valid_schema, assert_status_code, assert_max_response_time, assert_response_key_value
from support.client import Client


@pytest.mark.final_tests
class TestPetV2:
    client = Client()
    pet = generate_pet()
    created_pet_post_response: Response = ''

    def setup_method(self):
        if not self.created_pet_post_response:
            response = post_v2_pet(self.client, **self.pet)
            assert_status_code(response, 200)
            self.created_pet_post_response = response

    def test_post_pet_200(self):
        response = self.created_pet_post_response
        assert_status_code(response, 200)
        assert_max_response_time(response, 1)
        assert_valid_schema(response.json(), 'pet/v2_pet.json')
        assert_response_key_value(response, 'id', self.pet['id'])
        assert_response_key_value(response, 'name', self.pet['name'])

    def test_get_pet_200(self):
        response = get_v2_pet(self.client, self.pet['id'])
        assert_status_code(response, 200)
        assert_max_response_time(response, 1)
        assert_valid_schema(response.json(), 'pet/v2_pet.json')
        assert_response_key_value(response, 'id', self.pet['id'])
        assert_response_key_value(response, 'name', self.pet['name'])

    def test_delete_pet_200(self):
        self.created_pet_post_response = ''
        response = delete_v2_pet(self.client, self.pet['id'])
        assert_status_code(response, 200)
        assert_max_response_time(response, 1)

    def test_get_deleted_pet_404(self):
        delete_v2_pet(self.client, self.pet['id'])
        response = get_v2_pet(self.client, self.pet['id'])
        assert_status_code(response, 404)
        assert_max_response_time(response, 1)

    def test_put_pet_200(self):
        self.pet['name'] = 'NewName'
        response = put_v2_pet(self.client, **self.pet)
        assert_status_code(response, 200)
        assert_max_response_time(response, 1)
        assert_valid_schema(response.json(), 'pet/v2_pet.json')
        assert_response_key_value(response, 'id', self.pet['id'])
        assert_response_key_value(response, 'name', self.pet['name'])

        response = get_v2_pet(self.client, self.pet['id'])
        assert_response_key_value(response, 'name', self.pet['name'])
