import requests
import pytest
import allure


BASE_URL = "http://167.172.172.115:52353/object"


@pytest.mark.parametrize(
    "name, data",
    [
        ("Object 1", {"color": "green", "size": "adult S"}),
        ("Object 2", {"color": "blue", "size": "adult M"}),
        ("Object 3", {"color": "yellow", "size": "adult L"}),
    ],
)
@pytest.mark.critical
def test_create_object(name, data):
    payload = {"name": name, "data": data}
    response = requests.post(BASE_URL, json=payload)
    assert response.status_code in (200, 201)
    response_data = response.json()
    assert "id" in response_data
    requests.delete(f"{BASE_URL}/{response_data['id']}")


@allure.feature("Feature 1")
@pytest.mark.medium
def test_update_object(new_object):
    object_id = new_object
    updated = {"name": "Updated name", "data": {"color": "black", "size": "XL"}}
    response = requests.put(f"{BASE_URL}/{object_id}", json=updated)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated name"


@pytest.mark.skip("For some reason")
def test_patch_object(new_object):
    object_id = new_object
    patch_payload = {"name": "Patched name"}
    response = requests.patch(f"{BASE_URL}/{object_id}", json=patch_payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Patched name"


@allure.story("Story X")
@pytest.mark.smoke
def test_delete_object():
    payload = {"name": "To delete", "data": {"color": "gray", "size": "XS"}}
    response = requests.post(BASE_URL, json=payload)
    object_id = response.json().get("id")
    del_response = requests.delete(f"{BASE_URL}/{object_id}")
    assert del_response.status_code == 200


@allure.feature("Feature 2")
@allure.story("Story X")
def test_get_object(new_object):
    object_id = new_object
    response = requests.get(f"{BASE_URL}/{object_id}")
    assert response.status_code == 200
    assert "id" in response.json()
