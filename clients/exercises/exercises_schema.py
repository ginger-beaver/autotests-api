from tools.camel_model import CamelModel

class Exercise(CamelModel):
    """
    Описание структуры упражнения.
    """
    id: str
    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str


class GetExercisesResponseSchema(CamelModel):
    """
    Описание структуры ответа на получение списка упражнений.
    """
    exercises: list[Exercise]


class ExerciseResponseSchema(CamelModel):
    """
    Описание структуры ответа на получение упражнения.
    """
    exercise: Exercise


class GetExercisesQuerySchema(CamelModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    course_id: str


class CreateExerciseRequestSchema(CamelModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str
    course_id: str
    max_score: int
    min_score: int
    order_index: int
    description: str
    estimated_time: str


class UpdateExerciseRequestSchema(CamelModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title: str | None
    max_score: int | None
    min_score: int | None
    order_index: int | None
    description: str | None
    estimated_time: str | None