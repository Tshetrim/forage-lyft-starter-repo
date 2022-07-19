from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tiresList):
        super().__init__()
        self.tires = tiresList
    

    def needs_service(self) -> bool:
        """
        Returns true if -> any tire has greater than [service_threshold] wear 
        """
        service_threshold = 0.9
        for tire in self.tires:
            if tire >= service_threshold:
                return True
        return False