import pytest


@pytest.fixture(scope="function")
def prework():
    print("This is prework")
    return "fail"

@pytest.fixture(scope="function")
def secondwork():
    print("Set up ")
    yield
    print("Tear down")

def test_initialCheck(prework,secondwork):
    print("This is first test")
    assert  prework == "fail"

def test_secondCheck(prework,secondwork):
    print("This is second test")