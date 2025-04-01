import pytest


@pytest.fixture(scope="function")
def presetup():
    print("I set up Browser Instance")