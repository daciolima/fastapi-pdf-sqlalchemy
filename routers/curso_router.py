from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from typing import List, Optional, Any
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header
from time import sleep

from fastapi import Depends
from models.curso_model import Curso, cursos

router = APIRouter()

