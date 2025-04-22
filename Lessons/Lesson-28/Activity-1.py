class My_class:
    __privateVar=27

    def privMeth(self):
        print("I am inside my class")

    def hello(self):
        print("Private Variable Value:",My_class.__privateVar)

foo=My_class()
foo.hello()
foo.privMeth()



