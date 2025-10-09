from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from tools.assertions.base import assert_equal


def assert_create_exercise_response(request: CreateExerciseRequestSchema, response: CreateExerciseResponseSchema):
    """
    Проверяет, что ответ на создание упражнения соответствует запросу.

    :param request: Исходный запрос на создание упражнения.
    :param response: Ответ API с данными упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    request_field_names = CreateExerciseRequestSchema.model_fields.keys()

    for field_name in request_field_names:
        assert_equal(
            actual=getattr(request, field_name),
            expected=getattr(response.exercise, field_name),
            name=field_name
        )
