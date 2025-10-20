import allure

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema, \
    ExerciseSchema, GetExerciseResponseSchema, UpdateExerciseRequestSchema, UpdateExerciseResponseSchema, \
    GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response


@allure.step("Check create exercise response")
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


@allure.step("Check exercise")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные упражнения соответствуют ожидаемым.

    :param actual: Фактические данные упражнения.
    :param expected: Ожидаемые данные упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    field_names = ExerciseSchema.model_fields.keys()

    for field_name in field_names:
        assert_equal(
            actual=getattr(actual, field_name),
            expected=getattr(expected, field_name),
            name=field_name
        )


@allure.step("Check get course response")
def assert_get_exercise_response(
        get_exercise_response: GetExerciseResponseSchema,
        create_exercise_response: CreateExerciseResponseSchema,
):
    """
    Проверяет, что ответ на получение упражнения соответствует ответу на его создание.

    :param get_exercise_response: Ответ API при запросе упражнения по его id.
    :param create_exercise_response: Ответ API при создании упражнения.
    :raises AssertionError: Если данные упражнений не совпадают.
    """
    assert_exercise(
        actual=get_exercise_response.exercise,
        expected=create_exercise_response.exercise
    )


@allure.step("Check update course response")
def assert_update_exercise_response(request: UpdateExerciseRequestSchema, response: UpdateExerciseResponseSchema):
    """
    Проверяет, что ответ на обновление упражнения соответствует данным из запроса.

    :param request: Исходный запрос на обновление упражнения.
    :param response: Ответ API с обновленными данными упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    request_field_names = UpdateExerciseRequestSchema.model_fields.keys()

    for field_name in request_field_names:
        assert_equal(
            actual=getattr(request, field_name),
            expected=getattr(response.exercise, field_name),
            name=field_name
        )


@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual: InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если упражнение не найдено на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "Exercise not found"
    """
    expected = InternalErrorResponseSchema(
        details="Exercise not found"
    )
    assert_internal_error_response(actual, expected)


@allure.step("Check get exercises response")
def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercise_responses: list[CreateExerciseResponseSchema]
):
    """
    Проверяет, что ответ на получение списка упражнений соответствует ответам на их создание.

    :param get_exercises_response: Ответ API при запросе списка упражнений.
    :param create_exercise_responses: Список API ответов при создании упражнений.
    :raises AssertionError: Если данные упражнений не совпадают.
    """
    assert_length(get_exercises_response.exercises, create_exercise_responses, "exercises")

    for index, create_response in enumerate(create_exercise_responses):
        assert_exercise(create_response.exercise, get_exercises_response.exercises[index])
