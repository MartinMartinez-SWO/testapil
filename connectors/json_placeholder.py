from requests import get
URL_API = 'https://jsonplaceholder.typicode.com'


class JsonPlaceholder:

    def __init__(self) -> None:
        self._url = '%s/' % (URL_API)

    def list_all(self):
        response = get(self._url + "users")
        return response.json() 


    def get_user_by_id(self, user_id):
        response = get(self._url + f"users/{user_id}")
        return response.json()