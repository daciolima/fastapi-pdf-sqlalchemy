from typing import Optional

# Base Model == O Schema do model. # Classe Schema é responsável pelo processo de serialização. Obj to Json e Json to Obj.
from pydantic import BaseModel as SChemaBaseModel


# Criação do Schema para Curso. Pode ser criado outros schemas para o mesmo model Curso. Ex: Para usar apenas duas propriedades.
# Basta só criar o schema e chamar o schema desejado la nos endpoint confdrme necessidade.
class CursoSchema(SChemaBaseModel):
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int

    class Config:
        orm_mode = True