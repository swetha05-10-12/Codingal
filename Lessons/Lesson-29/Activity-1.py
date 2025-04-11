from abc import ABC , abstractmethod

class Absclass(ABC):

    def print(self,x):
        print("Passed Value:",x)

    @abstractmethod
    def task(self):
        print("We are inside the Absclass task")


class test_class(Absclass):
    def task(self):
        print("We are inside the test_class task")


test_obj=test_class()
test_obj.task()
test_obj.print(100)


