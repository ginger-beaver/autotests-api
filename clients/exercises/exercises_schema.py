from pydantic import Field

from tools.camel_model import CamelModel
from tools.fake_data_generator import fake


class ExerciseSchema(CamelModel):
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
    exercises: list[ExerciseSchema]


class GetExerciseResponseSchema(CamelModel):
    """
    Описание структуры ответа на получение упражнения.
    """
    exercise: ExerciseSchema


class GetExercisesQuerySchema(CamelModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    course_id: str


class CreateExerciseRequestSchema(CamelModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(default_factory=fake.uuid4)
    max_score: int = Field(default_factory=fake.max_score)
    min_score: int = Field(default_factory=fake.min_score)
    order_index: int = Field(default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(default_factory=fake.estimated_time)


class CreateExerciseResponseSchema(CamelModel):
    """
    Описание структуры ответа на создание упражнения.
    """
    exercise: ExerciseSchema


class UpdateExerciseRequestSchema(CamelModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(default_factory=fake.max_score)
    min_score: int | None = Field(default_factory=fake.min_score)
    order_index: int | None = Field(default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(default_factory=fake.estimated_time)


class UpdateExerciseResponseSchema(CamelModel):
    """
    Описание структуры ответа на обновление упражнения.
    """
    exercise: ExerciseSchema
