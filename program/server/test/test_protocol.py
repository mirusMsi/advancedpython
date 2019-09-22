import pytest
from datetime import datetime
from protocol import validate_request, make_response, make_200, make_400, make_404, make_500


CODE = 200

TIME = datetime.now().timestamp()

ACTION = 'test'

DATA = 'some client data'

REQUEST = {
    'action': ACTION,
    'time': TIME,
    'data': DATA
}


def test_action_make_response():
    response = make_response(REQUEST, CODE, DATA, date=TIME)
    action = response.get('action')
    assert action == ACTION


def test_code_make_response():
    response = make_response(REQUEST, CODE, DATA, date=TIME)
    code = response.get('code')
    assert code == CODE


def test_time_make_response():
    response = make_response(REQUEST, CODE, DATA, date=TIME)
    time = response.get('time')
    assert time == TIME


def test_data_make_response():
    response = make_response(REQUEST, CODE, DATA, date=TIME)
    data = response.get('data')
    assert data == DATA


def test_invalid_make_response():
    with pytest.raises(AttributeError):
        response = make_response(None, CODE)


def test_not_action_validate_request():
    check = validate_request({'time': TIME})
    assert check == False


def test_not_time_validate_request():
    check = validate_request({'action': ACTION})
    assert check == False


def test_action_make_200():
    response = make_200(REQUEST, DATA, date=TIME)
    action = response.get('action')
    assert action == ACTION


def test_code_make_200():
    response = make_200(REQUEST, DATA, date=TIME)
    code = response.get('code')
    assert code == 200


def test_time_make_200():
    response = make_200(REQUEST, DATA, date=TIME)
    time = response.get('time')
    assert time == TIME


def test_data_make_200():
    response = make_200(REQUEST, DATA, date=TIME)
    data = response.get('data')
    assert data == DATA


def test_action_make_400():
    response = make_400(REQUEST, DATA, date=TIME)
    action = response.get('action')
    assert action == ACTION


def test_code_make_400():
    response = make_400(REQUEST, DATA, date=TIME)
    code = response.get('code')
    assert code == 400


def test_time_make_400():
    response = make_400(REQUEST, DATA, date=TIME)
    time = response.get('time')
    assert time == TIME


def test_data_make_400():
    response = make_400(REQUEST, DATA, date=TIME)
    data = response.get('data')
    assert data == DATA


def test_code_make_404():
    response = make_404(REQUEST, date=TIME)
    code = response.get('code')
    assert code == 404


def test_time_make_404():
    response = make_404(REQUEST, date=TIME)
    time = response.get('time')
    assert time == TIME


def test_data_make_404():
    response = make_404(REQUEST, date=TIME)
    data = response.get('data')
    assert data == f'Action "{REQUEST.get("action")}" not found'


def test_code_make_500():
    response = make_500(REQUEST, date=TIME)
    code = response.get('code')
    assert code == 500


def test_time_make_500():
    response = make_500(REQUEST, date=TIME)
    time = response.get('time')
    assert time == TIME


def test_data_make_500():
    response = make_500(REQUEST, date=TIME)
    data = response.get('data')
    assert data == 'Internal server error'