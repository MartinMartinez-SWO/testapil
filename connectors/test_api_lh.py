from requests import get, delete

URL_API = "http://127.0.0.1:5000/api/admin"

class TestApil:
    def __init__(self) -> None:
        self._url = f"{URL_API}/"

    def list_all_users(self):
        response = get(self._url + "user")
        return response.json()

    def get_user_by_id(self, user_id):
        response = get(self._url + f"user/{user_id}")
        return response.json()

    # def save_user(self, body):
    #     return post(self._url + "user")

    # def update_user_by_id(self, user_id, body):
    #     return put(self._url + "user", body)

    def delete_user_by_id(self, user_id):
        response = delete(self._url + f"user/{user_id}")
        return response.json()
