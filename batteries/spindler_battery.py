from datetime import datetime
from batteries.battery import Battery


class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        """
        Returns true if -> 3 years has passed
        """
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        return service_threshold_date < datetime.today().date()

