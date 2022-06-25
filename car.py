from servicable import servicable



class Car(servicable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    #overriding from servicable
    def needs_service(self) -> bool:
        for a in dir(Car):
            if getattr(Car, a).needs_service():
                    return True
        return False


