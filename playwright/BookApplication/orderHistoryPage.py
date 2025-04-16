class OrdersHistoryPage:
    def __init__(self,page):
        self.page =page

    def selectOrder(self,orderId):
        row_item = self.page.locator("tr").filter(has_text=orderId)
        row_item.get_by_role("button", name="View").click()
        print("#######Clicked on View Button##########")
        #OrderDetails= OrderDetails(self.page)
        #orderDetails = newOrderDetails(self.page)
        #return orderDetails