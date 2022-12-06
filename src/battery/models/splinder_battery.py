
from src.battery.battery import Battery


class SplinderBattery(Battery):
    YEARS_TO_SERVICE = 2

    def needs_service(self):
        return self.last_service_date.replace(self.last_service_date.year + self.YEARS_TO_SERVICE) < self.current_date
