class vehicle:

    def __int__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class Bus(vehicle):
    pass

school_bus= Bus("School Volvo",180,12)
print("Vehicle name:", school_bus.name,"Speed:",school_bus.max_speed,"Mileage:",school_bus.mileage)
