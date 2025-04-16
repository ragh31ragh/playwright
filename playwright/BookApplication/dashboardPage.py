class DashboardPage:
    def __init__(self,page):
        self.page = page

    def selectOrderNavigationLink(self):
        self.page.get_by_role("button", name="ORDERS").click()
        #ordersHistoryPage = OrdersHistoryPage(self.page)
        #return ordersHistoryPage