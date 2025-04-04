class bird:
    def __init__(self):
        print("Bird is ready")

    def who_is_this(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

class penguin(bird):
    
    def __init__(self):
        super().__init__()
        print("Penguin")

    def run(self):
        print("Run faster")

peggy=penguin()
peggy.who_is_this()
peggy.swim()
peggy.run()



