from typing import Union
from fastapi import APIRouter, Request

from utils.validators import convert_value_to_type

router = APIRouter()

@router.post(
    path="/get_form",
    summary="Поиск подходящего шаблона",
    tags=["forms"]
)
async def find_form(request: Request) -> Union[str, dict]:
    params = dict(request.query_params)
    for key in params:
        params[key] = convert_value_to_type(params[key])

    form_templates = []


    #нельзя сравнивать на равенство, именно включение
    for template in form_templates:
        if dict(template) == params:
            return 'template_name'
    return params
