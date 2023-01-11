from typing import Union

from fastapi import APIRouter, Request

from utils.validators import convert_dict_values_to_type

router = APIRouter()


@router.post(
    path="/get_form",
    summary="Поиск подходящего шаблона",
    tags=["forms"],
    status_code=200,
)
async def find_form(request: Request) -> Union[str, dict]:
    params = dict(request.query_params)
    input_form = convert_dict_values_to_type(params)

    suitable_form_name = await request.app.db_service.find_suitable_form_template_task(input_form)
    if suitable_form_name:
        return_data = {
            'msg': 'Suitable form template was found!',
            'Form template name': suitable_form_name,
        }
    else:
        return_data = {
            'msg': 'Suitable form template was not found!',
            'input_form': input_form,
        }

    return return_data
