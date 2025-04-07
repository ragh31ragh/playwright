import pytest
from pytest_bdd import given, when, then, parsers,  scenarios

from PageObjects.login import LoginPage

from utils.api_base2 import APIUtils2

scenarios('features/orderTransaction1.feature')

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('place the item order with {username} and {password}'))
def place_item_order(playwright,username,password,shared_data):
    user_creds = {
        "userEmail":username,
        "password": password
    }
    apiUtils2 =APIUtils2()
    orderId = apiUtils2.createOrder(playwright,user_creds)
    shared_data['order_id']=orderId


@given('user is on landing page')
def user_on_Landing_Page(browserInstance,shared_data):
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    shared_data['login_page'] = loginPage

@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username,password,shared_data):
    loginPage = shared_data['login_page']
    dashboardPage = loginPage.login(username, password)
    shared_data['dashboard_page'] = dashboardPage

@when('Navigate to order page')
def navigate_to_orders_page(shared_data):
    dashboardPage =  shared_data['dashboard_page']
    ordersHistoryPage = dashboardPage.seletOrderNavigationLink()
    shared_data['ordersHistory_page'] = ordersHistoryPage


@when('Select the OrderId')
def select_order_id(shared_data):
    ordersHistoryPage = shared_data['ordersHistory_page']
    orderId = shared_data['order_id']
    orderDetails = ordersHistoryPage.selectOrder(orderId)
    shared_data['order_Details'] = orderDetails

@then('Order message is successfully displayed')
def order_message_displayed(shared_data):
    orderDetails = shared_data['order_Details']
    orderDetails.verifyOrderMessage()