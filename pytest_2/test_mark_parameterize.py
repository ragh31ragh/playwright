import pytest



@pytest.mark.parametrize("username,password",[
    ("Selenium","Webdriver"),
    ("Python","Pytest"),
    ("Java","TestNG"),
])
def test_login(username,password):
    print(username)
    print(password)

