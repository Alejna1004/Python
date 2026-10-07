class MyClass:
    def __init__(self):
        self._protected_variable =  " This is a protected_variable"

    def _protected_method(self):
        print("This is a protected_method")


my_class = MyClass()
print(my_class._protected_variable)
my_class._protected_method()