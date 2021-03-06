import pytest
from better_errors import Result


@pytest.fixture
def ok_only():
    return Result("TEST", None)


@pytest.fixture
def err_only():
    return Result(None, Exception("TEST"))


@pytest.fixture
def both():
    return Result("TEST", Exception("TEST"))


@pytest.fixture
def none():
    return Result(None, None)


def test_setting_ok_only(ok_only):
    testval = "TEST"
    val = ok_only.value()
    assert val == testval


def test_setting_err_only(err_only):
    testval = Exception("TEST")
    val = err_only.value()
    assert type(val) == type(testval) and val.args == testval.args


def test_setting_ok_and_err(both):
    testval = Exception("TEST")
    val = both.value()
    assert type(val) == type(testval) and val.args == testval.args


def test_setting_none(none):
    testval = Exception("no result or error")
    val = none.value()
    assert type(val) is type(testval) and val.args == testval.args
