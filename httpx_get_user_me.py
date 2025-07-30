import httpx

data = {
    "email": "johndoe@example.com",
    "password": "123abc"}

response1 = httpx.post(
    url="http://localhost:8000/api/v1/authentication/login",
    json=data)

json_data = response1.json()["token"]

header = {"Authorization": f"{json_data["tokenType"]} {json_data["accessToken"]}"}

response2 = httpx.get(
    url="http://localhost:8000/api/v1/users/me",
    headers=header)

print(response2.json(), response2.status_code, sep="\n")