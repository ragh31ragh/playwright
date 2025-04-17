import pytest


@pytest.mark.smoke
def test_login():
    print("Test Login function ")

@pytest.mark.regression
def test_addproduct():
    print("This is for adding product")

@pytest.mark.smoke
def test_logout():
    print("This is for logout")