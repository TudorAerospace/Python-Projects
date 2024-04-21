#Problem 5
class handleString:
    def __init__(self):
        self.string = ""
    def get_string(self):
        self.string = str(input("Please input your string: ")).upper()
    def print_string(self):
        print(self.string.upper())
str_object = handleString()
str_object.get_string()
str_object.print_string()