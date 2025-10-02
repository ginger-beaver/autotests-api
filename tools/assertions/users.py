from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    :raises AttributeError: Если хотя бы одного поля не существует.
    """
    fields = ('email', 'last_name', 'first_name', 'middle_name')
    for field_name in fields:
        assert_equal(
            actual=getattr(request, field_name),
            expected=getattr(response.user, field_name),
            name=field_name
        )


def assert_get_user_response(get_user_response: UserSchema, create_user_response: UserSchema):
    assert_user(get_user_response, create_user_response)


def assert_user(actual: UserSchema, expected: UserSchema):
    fields = UserSchema.model_fields.keys()

    for field_name in fields:
        assert_equal(
            actual=getattr(actual, field_name),
            expected=getattr(expected, field_name),
            name=field_name
        )
