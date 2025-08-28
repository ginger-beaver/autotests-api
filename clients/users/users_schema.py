from pydantic import EmailStr
from tools.camel_model import CamelModel

class UserSchema(CamelModel):
    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str


class CreateUserRequestSchema(CamelModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: EmailStr
    password: str
    last_name: str
    first_name: str
    middle_name: str


class CreateUserResponseSchema(CamelModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema


class UpdateUserRequestSchema(CamelModel):
    """
    Описание структуры запроса на обновление пользователя.
    """
    email: EmailStr | None
    last_name: str | None
    first_name: str | None
    middle_name: str | None


class UpdateUserResponseSchema(CamelModel):
    """
    Описание структуры ответа обновления пользователя.
    """
    user: UserSchema


class GetUserResponseSchema(CamelModel):
    """
    Описание структуры запроса получения пользователя.
    """
    user: UserSchema
