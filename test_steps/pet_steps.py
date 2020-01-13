import allure
from support.environment import ENV


@allure.step('GET /v2/pet/{pet_id}')
def get_v2_pet(client, pet_id, **data):
    """
    GETs /v2/pet
    :param client: Rest Client with auth credentials
    :param pet_id: Store Pet ID
    """
    return client.get(f'{ENV.base_url()}/v2/pet/{pet_id}', **data)


@allure.step('POST /v2/pet')
def post_v2_pet(client, **data):
    """
    POSTs /v2/pet
    :param client: Rest Client with auth credentials
    """
    return client.post(f'{ENV.base_url()}/v2/pet', **data)


@allure.step('PUT /v2/pet')
def put_v2_pet(client, **data):
    """
    PUTs /v2/pet
    :param client: Rest Client with auth credentials
    """
    return client.put(f'{ENV.base_url()}/v2/pet', **data)


@allure.step('DELETE /v2/pet/{pet_id}')
def delete_v2_pet(client, pet_id, **data):
    """
    DELETEs /v2/pet
    :param client: Rest Client with auth credentials
    :param pet_id: Store Pet ID to delete
    """
    return client.delete(f'{ENV.base_url()}/v2/pet/{pet_id}', **data)


def generate_pet() -> dict:
    pet = {
            "id": 21435431254521,
            "name": "Garfield",
            "category": {
                "name": "cats"
            },
            "status": "available"
        }
    return pet

