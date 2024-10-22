import requests


class Yougile:

    def __init__(self, login, password, company_id):
        self.login = login
        self.password = password
        self.company_id = company_id
        self.base_url = "https://ru.yougile.com"
        self.token = self.get_auth_token()

    def get_auth_token(self):
        url = self.base_url + "/api-v2/auth/keys/get"
        headers = {"Content-Type": "application/json"}
        payload = {
            "login": self.login,
            "password": self.password,
            "companyId": self.company_id,
        }
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            if isinstance(response_data, list) and len(response_data) > 0:
                return response_data[0].get('key')
            else:
                raise Exception("Unexpected response format: Expected a list")
        else:
            raise Exception(
                f"Authentication failed: {response.status_code} {response.text}"
            )

    def make_authorized_request(self, endpoint, data=None, method="GET"):
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        print(f"Making {method} request to: {url}")
        print(f"Request headers: {headers}")
        print(f"Request data: {data}")

        if method == "POST":
            response = requests.post(url, json=data, headers=headers)
        elif method == "PUT":
            response = requests.put(url, json=data, headers=headers)
        elif method == "GET":
            response = requests.get(url, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")

        if response.status_code in [200, 201]:
            return response.json()
        else:
            raise Exception(
                f"Request failed: {response.status_code} {response.text}"
            )

    def create_project(self, project_name, users):
        endpoint = "/api-v2/projects"
        data = {"title": project_name, "users": users}
        return self.make_authorized_request(endpoint, data)

    def get_list_of_projects(self):
        endpoint = "/api-v2/projects"
        url = self.base_url + endpoint
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                f"Request failed: {response.status_code} {response.text}"
            )

    def update_project(self, project_id, new_title):
        endpoint = f"/api-v2/projects/{project_id}"
        data = {"title": new_title}
        return self.make_authorized_request(endpoint, data, method="PUT")

    def get_project_by_id(self, project_id):
        endpoint = f"/api-v2/projects/{project_id}"
        return self.make_authorized_request(endpoint, method="GET")
