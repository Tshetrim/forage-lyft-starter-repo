from datetime import datetime
from batteries import Battery


class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return service_threshold_date < datetime.today().date()

