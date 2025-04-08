import pytest


@pytest.fixture
def sample_data():
    print("\n Setup : Creating Test Data ") #Runs before the test
    data = {"name" : "Alice","age" :30 }
    yield data # Provides data to the test
    print ("cleaning up test data ")

def test_example(sample_data):
    assert sample_data["name"] == "Alice"
    assert sample_data["age"] == 30
    print ("Test Executed Successfully")