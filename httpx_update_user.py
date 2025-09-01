import httpx
from faker import Faker
from tools.fake_data_generator import fake

fake = Faker('ru_RU')

user_data = {
    "email": fake.email(),
    "password": fake.password(),
    "lastName": fake.last_name(),
    "firstName": fake.first_name(),
    "middleName": fake.middle_name()
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=user_data)

user = {"email": user_data["email"], "password": user_data["password"]}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=user)

token_json = login_response.json()["token"]
header = {"Authorization": f"{token_json["tokenType"]} {token_json["accessToken"]}"}

user_id = create_user_response.json()["user"]["id"]
user_new_date = {
    "email": fake.email(),
    "lastName": fake.last_name(),
    "firstName": fake.first_name(),
    "middleName": fake.middle_name()
}

update_user_response = httpx.patch(
    url=f"http://127.0.0.1:8000/api/v1/users/{user_id}",
    headers=header,
    json=user_new_date
)

print(update_user_response.status_code)






