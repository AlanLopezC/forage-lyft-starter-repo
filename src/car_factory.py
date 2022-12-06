
from src.car import Car
from src.battery.models.nubbin_battery import NubbinBattery
from src.battery.models.splinder_battery import SplinderBattery
from src.engine.models.capulet_engine import CapuletEngine
from src.engine.models.sternman_engine import SternmanEngine
from src.engine.models.willoughby_engine import WilloughbyEngine


class CarFactory():

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:

        battery = SplinderBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        return Car(battery, engine)

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:

        battery = SplinderBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        return Car(battery, engine)

    def create_palindrome(self, current_date, last_service_date, warning_light_on) -> Car:

        battery = SplinderBattery(current_date, last_service_date)
        engine = SternmanEngine(warning_light_on)

        return Car(battery, engine)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:

        battery = NubbinBattery(current_date, last_service_date)
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        return Car(battery, engine)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage) -> Car:

        battery = NubbinBattery(current_date, last_service_date)
        engine = CapuletEngine(current_mileage, last_service_mileage)

        return Car(battery, engine)
