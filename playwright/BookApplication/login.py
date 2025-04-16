class LoginPage:
    def __init__(self,page):
        self.page = page
        print("Login Constructor executed successfully")
    def Navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def Login(self,userEmail, userPassword):
        self.page.get_by_placeholder("email@example.com").fill(userEmail)
        self.page.get_by_placeholder("enter your passsword").fill(userPassword)
        self.page.get_by_role("button", name="Login").click()
        print("###########LoginCompleted#######")