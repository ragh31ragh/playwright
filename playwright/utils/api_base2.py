from playwright.sync_api import Playwright

ordersPayload = {"orders": [{"country": "India", "productOrderedId" : "67a8df1ac0d3e6622a297ccb"}]}
class APIUtils2:

    def getToken(self,playwright:Playwright,user_creds):
        userEmail = user_creds["userEmail"];
        userPassword = user_creds["password"];
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                 data = {  "userEmail": userEmail,  "userPassword": userPassword}
                                 )
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]

    def createOrder(self,playwright:Playwright,user_creds):
        token = self.getToken(playwright,user_creds)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                 data = ordersPayload,
                                 headers={"Authorization" : token,
                                          "Content-Type" : "application/json"})
        print(response.json())
        response_body = response.json()
        orderId = response_body["orders"][0]
        return orderId