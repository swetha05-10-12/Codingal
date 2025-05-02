class vehicle:
    def __init__ (self,sc):
        self.sc=sc

    def fare(self):
        return self.sc*100
    
class bus(vehicle):
    def fare(self):
        standard_fare=super().fare()
        maintenance=0.10*standard_fare
        return standard_fare+maintenance

bus=bus(50)
print("Total Bus Fare: INR ",bus.fare())
