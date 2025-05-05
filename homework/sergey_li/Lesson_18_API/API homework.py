import requests

BASE_URL = "http://167.172.172.115:52353/object"


def create_object():
    payload = {"name": "New object", "data": {"color": "green", "size": "adult M"}}
    response = requests.post(BASE_URL, json=payload)
    object_id = response.json().get("id")
    print(response.json(), response.status_code)
    return object_id


def update_object(object_id):
    new_payload = {
        "name": "Updated object",
        "data": {"color": "light green", "size": "adult S"},
    }
    response = requests.put(f"{BASE_URL}/{object_id}", json=new_payload)
    print(response.json(), response.status_code)


def patch_update_object(object_id):
    patch_payload = {"name": "Object updated with patch"}
    response = requests.patch(f"{BASE_URL}/{object_id}", json=patch_payload)
    print(response.json(), response.status_code)


def delete_object(object_id):
    response = requests.delete(f"{BASE_URL}/{object_id}")
    print(response.status_code)


def view_object(object_id):
    response = requests.get(f"{BASE_URL}/{object_id}")
    print(response.status_code)


obj_id = create_object()
update_object(obj_id)
patch_update_object(obj_id)
delete_object(obj_id)
