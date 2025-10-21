from pydantic import BaseModel, HttpUrl, Field, FilePath

from tools.camel_model import CamelModel
from tools.fake_data_generator import fake


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
    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    directory: str = Field(default="tests")
    upload_file: FilePath = Field(alias=None)


class CreateFileResponseSchema(CamelModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema


class GetFileResponseSchema(CamelModel):
    """
    Описание структуры ответа получение файла.
    """
    file: FileSchema
