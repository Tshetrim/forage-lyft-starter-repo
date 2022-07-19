from servicable import servicable

class Car(servicable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    #overriding from servicable
    def needs_service(self) -> bool:
        #grabs the parts in car instance, currently: engine, battery and returns true if any of the parts need to be serviced
        for part in vars(self): 
            if getattr(self, part).needs_service(): 
                    return True
        return False


