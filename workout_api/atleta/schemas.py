from typing import Annotated
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema
class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', exemple='Joao', max_lenght=50)]
    cpf: Annotated[str, Field(description='Cpf do atleta', exemple='12345678900', max_lenght=11)]
    idade: Annotated[int, Field(description='Idade do atleta', exemple=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do atleta', exemple=75.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', exemple=1.70)]
    sexo: Annotated[str, Field(description='Sexo do atleta', exemple='M', max_lenght=1)]

                     