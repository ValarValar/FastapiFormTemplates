from starlette.testclient import TestClient

from main import app

base_url = '/api/forms/get_form?'


def test_empty_params():
    with TestClient(app) as client:
        response = client.post(base_url)
        assert response.status_code == 200
        expected_answer = {
            'msg': 'Suitable form template was not found!',
            'input_form': {},
        }
        assert expected_answer == response.json()


def test_ok_params():
    params_list = [
        "username=valar",
        "user_email=sos@mail.ru",
        "user_phone=+7 989 702 62 68",
        "user_registration_date=24.02.2021"
    ]
    params_str = "&".join(params_list)
    new_url = base_url + params_str

    with TestClient(app) as client:
        response = client.post(new_url)
        assert response.status_code == 200
        expected_answer = {
            'msg': 'Suitable form template was found!',
            'Form template name': 'Registration template',
        }
        assert expected_answer == response.json()


def test_multiple_ok_params():
    params_list = [
        "username=valar",
        "password=12314",
        "user_email=sos@mail.ru",
    ]
    params_str = "&".join(params_list)
    new_url = base_url + params_str
    with TestClient(app) as client:
        response = client.post(new_url)
        assert response.status_code == 200
        expected_answer = {
            'msg': 'Suitable form template was found!',
            'Form template name': 'Login template',
        }
        assert expected_answer == response.json()


def test_input_params_more_than_template():
    params_list = [
        "username=valar",
        "user_email=sos@mail.ru",
        "user_phone=+7 989 702 62 68",
        "user_registration_date=24.02.2021",
        "user_email1=sos@mail.ru",
        "user_email2=sos@mail.ru",
        "user_email3=sos@mail.ru",
    ]
    params_str = "&".join(params_list)
    new_url = base_url + params_str

    with TestClient(app) as client:
        response = client.post(new_url)
        assert response.status_code == 200
        expected_answer = {
            'msg': 'Suitable form template was found!',
            'Form template name': 'Registration template',
        }
        assert expected_answer == response.json()


def test_one_param():
    params_list = [
        "username=valar",
    ]
    params_str = "&".join(params_list)
    new_url = base_url + params_str

    with TestClient(app) as client:
        response = client.post(new_url)
        assert response.status_code == 200
        expected_answer = {
            'msg': 'Suitable form template was not found!',
            'input_form': {"username": "text"},
        }
        assert expected_answer == response.json()
