from tools.camel_model import CamelModel


class TokenSchema(CamelModel):
    """
    Описание структуры аутентификационных токенов.
    """
    token_type: str
    access_token: str
    refresh_token: str


class LoginRequestSchema(CamelModel):
    """
    Описание структуры запроса на аутентификацию.
    """
    email: str
    password: str


class LoginResponseSchema(CamelModel):
    """
    Описание структуры ответа аутентификации.
    """
    token: TokenSchema


class RefreshRequestSchema(CamelModel):
    """
    Описание структуры запроса для обновления токена.
    """
    refresh_token: str
