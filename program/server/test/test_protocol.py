import pytest
from datetime import datetime
from protocol import validate_request, make_response, make_200, make_400, make_404, make_500


@pytest.fixture
def expected_code():
    return 200

@pytest.fixture
def expected_action():
    return 'test'

@pytest.fixture
def expected_time():
    return datetime.now().timestamp()

@pytest.fixture
def expected_data():
    return 'some client data'

@pytest.fixture
def initial_request(expected_action, expected_time, expected_data):
    return {
        'action': expected_action,
        'time': expected_time,
        'data': expected_data
    }

@pytest.fixture
def invalid_request(expected_data):
    return {
        'data': expected_data
    }


def test_action_make_response(initial_request, expected_code, expected_action, expected_time, expected_data):
    response = make_response(initial_request, expected_code, expected_data, date=expected_time)
    action = response.get('action')
    assert action == expected_action


def test_code_make_response(initial_request, expected_code, expected_time, expected_data):
    response = make_response(initial_request, expected_code, expected_data, date=expected_time)
    code = response.get('code')
    assert code == expected_code


def test_time_make_response(initial_request, expected_code, expected_time, expected_data):
    response = make_response(initial_request, expected_code, expected_data, date=expected_time)
    time = response.get('time')
    assert time == expected_time


def test_data_make_response(initial_request, expected_code, expected_time, expected_data):
    response = make_response(initial_request, expected_code, expected_data, date=expected_time)
    data = response.get('data')
    assert data == expected_data


def test_invalid_make_response(expected_code):
    with pytest.raises(AttributeError):
        response = make_response(None, expected_code)


def test_valid_validate_request(initial_request):
    assert validate_request(initial_request)


def test_invalid_validate_request(invalid_request):
    assert validate_request(invalid_request) == False


def test_action_make_200(initial_request, expected_action, expected_time, expected_data):
    response = make_200(initial_request, expected_data, date=expected_time)
    action = response.get('action')
    assert action == expected_action


def test_code_make_200(initial_request, expected_time, expected_data):
    response = make_200(initial_request, expected_data, date=expected_time)
    code = response.get('code')
    assert code == 200


def test_time_make_200(initial_request, expected_time, expected_data):
    response = make_200(initial_request, expected_data, date=expected_time)
    time = response.get('time')
    assert time == expected_time


def test_data_make_200(initial_request, expected_time, expected_data):
    response = make_200(initial_request, expected_data, date=expected_time)
    data = response.get('data')
    assert data == expected_data


def test_action_make_400(initial_request, expected_action, expected_time, expected_data):
    response = make_400(initial_request, expected_data, date=expected_time)
    action = response.get('action')
    assert action == expected_action


def test_code_make_400(initial_request, expected_time, expected_data):
    response = make_400(initial_request, expected_data, date=expected_time)
    code = response.get('code')
    assert code == 400


def test_time_make_400(initial_request, expected_time, expected_data):
    response = make_400(initial_request, expected_data, date=expected_time)
    time = response.get('time')
    assert time == expected_time


def test_data_make_400(initial_request, expected_time, expected_data):
    response = make_400(initial_request, expected_data, date=expected_time)
    data = response.get('data')
    assert data == expected_data


def test_code_make_404(initial_request, expected_time):
    response = make_404(initial_request, date=expected_time)
    code = response.get('code')
    assert code == 404


def test_time_make_404(initial_request, expected_time):
    response = make_404(initial_request, date=expected_time)
    time = response.get('time')
    assert time == expected_time


def test_data_make_404(initial_request, expected_time):
    response = make_404(initial_request, date=expected_time)
    data = response.get('data')
    assert data == f'Action "{initial_request.get("action")}" not found'


def test_code_make_500(initial_request, expected_time):
    response = make_500(initial_request, date=expected_time)
    code = response.get('code')
    assert code == 500


def test_time_make_500(initial_request, expected_time):
    response = make_500(initial_request, date=expected_time)
    time = response.get('time')
    assert time == expected_time


def test_data_make_500(initial_request, expected_time):
    response = make_500(initial_request, date=expected_time)
    data = response.get('data')
    assert data == 'Internal server error'