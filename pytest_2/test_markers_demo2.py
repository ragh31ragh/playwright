import pytest



@pytest.mark.skip
def test_login():
    print("Test Login function ")


def test_addproduct():
    print("This is for adding product")

@pytest.mark.xfail
def test_logout():
    assert Fail
    print("This is for logout")