class India():
    def capital():
        print("New Delhi is the capital of India")
    def language():
        print("Hindi is the most widely spoken language of India")
    def type():
        print("India is a developing country")

class USA():
    def capital():
        print("Washington is the capital of USA")
    def language():
        print("English is the primary language of USA")
    def type():
        print("USA is a developed country")

obj_ind=India()
obj_usa=USA()

for country in (obj_usa,obj_ind):
    country.capital()
    country.language()
    country.type()