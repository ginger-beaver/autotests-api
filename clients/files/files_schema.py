from pydantic import BaseModel, HttpUrl, Field
from tools.camel_model import CamelModel


class FileSchema(CamelModel):
    """
    Описание структуры файла.
    """
    id: str
    url: HttpUrl
    filename: str
    directory: str


class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename: str
    directory: str
    upload_file: str = Field(alias=None)


class CreateFileResponseSchema(CamelModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema
