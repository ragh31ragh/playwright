class Parent:
    def greet(self):
        print("Hello from parent")

class Child(Parent):

    def __init__(self,title):
        self.title = title

    def greetChild(self):
        print("Hello from child " + self.title)
        #print("####Super####")
        super().greet()
        #print("####Super####")


p = Parent()
p.greet()

print("Child Related ")
c = Child("Raghavendra")
c.greetChild()
c.greet()