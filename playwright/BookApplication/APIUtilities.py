
from playwright.sync_api import Playwright

ordersPayload = {"orders": [{"country": "India", "productOrderedId" : "67a8df1ac0d3e6622a297ccb"}]}
class apiUtilities:
    def getToken(self,playwright : Playwright, user_creds):
        user_email = user_creds["userEmail"]
        user_password = user_creds["password"]
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                 data = {  "userEmail": user_email,  "userPassword": user_password}
                                 )
        assert  response.ok
        responseBody = response.json()
        return responseBody["token"]


    def createOrder(self,playwright : Playwright, user_creds):
        token = self.getToken(playwright,user_creds)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data=ordersPayload,
                                            headers={"Authorization": token,
                                                     "Content-Type": "application/json"})
        response_body = response.json()
        orderId = response_body["orders"][0]
        return orderId
