class StringClass:

    def __init__(self):
        self.name = "334455"

    def print_Name(self):
        print(len(self.name))
        print(list(self.name))
        converting = self.name.split(" ")
        print(converting)

object = StringClass()
object.print_Name()





