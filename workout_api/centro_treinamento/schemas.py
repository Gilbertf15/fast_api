from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    name: Annotated[str, Field(description='Nome da centro de treinamento', exemple='CT king', max_lenght=20)]
    endereço: Annotated[str, Field(description='endereço do centro de treinamento', exemple='Rua Y  QO5', max_lenght=60)]
    proprietario: Annotated[str, Field(description='proprietario do centro de treinamento', exemple='Marcos', max_lenght=30)]