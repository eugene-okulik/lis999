import pytest
import requests

BASE_URL = "http://167.172.172.115:52353/object"


@pytest.fixture(scope="session")
def start_end():
    print("Start testing")
    yield
    print("Testing Complete")


@pytest.fixture(scope="function")
def before_after():
    print("\nbefore test")
    yield
    print("\nafter test")


@pytest.fixture
def new_object():
    payload = {"name": "Temp object", "data": {"color": "blue", "size": "L"}}
    response = requests.post(BASE_URL, json=payload)
    object_id = response.json().get("id")
    print(object_id)
    yield object_id
    print("deleting the object")
    requests.delete(f"{BASE_URL}/{object_id}")
