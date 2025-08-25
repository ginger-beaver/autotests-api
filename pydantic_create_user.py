from pydantic import BaseModel, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel


class CamelModel(BaseModel):
    """
    Базовый класс для Pydantic моделей с поддержкой camelCase alias.
    """
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True
    )


class UserSchema(CamelModel):
    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str


class CreateUserRequestSchema(CamelModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    email: EmailStr
    password: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserResponseSchema(CamelModel):
    """
    Описание структуры ответа на создание пользователя.
    """
    user: UserSchema
