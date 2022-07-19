from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tiresList):
        super().__init__()
        self.tires = tiresList
    

    def needs_service(self) -> bool:
        """
        Returns true if -> the sum of all tires wear has greater than [service_threshold] wear 
        """
        service_threshold = 0.3
        sum_tire_wear = 0
        for tire in self.tires:
            sum_tire_wear += tire
        return sum_tire_wear >= service_threshold