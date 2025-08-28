from tools.camel_model import CamelModel
from clients.users.users_schema import UserSchema
from clients.files.files_schema import FileSchema

class Course(CamelModel):
    """
    Описание структуры курса.
    """
    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    preview_file: FileSchema
    estimated_time: str
    created_by_user: UserSchema


class GetCoursesQuerySchema(CamelModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    user_id: str


class CreateCourseRequestSchema(CamelModel):
    """
    Описание структуры запроса на создание курса.
    """
    title: str
    max_score: int
    min_score: int
    description: str
    estimated_time: str
    preview_file_id: str
    created_by_user_id: str


class CreateCourseResponseSchema(CamelModel):
    """
    Описание структуры ответа создания курса.
    """
    course: Course


class UpdateCourseRequestSchema(CamelModel):
    """
    Описание структуры запроса на обновление курса.
    """
    title: str | None
    max_score: int | None
    min_score: int | None
    description: str | None
    estimated_time: str | None