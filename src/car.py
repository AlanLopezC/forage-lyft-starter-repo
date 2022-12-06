
from src.battery.battery import Battery
from src.engine.engine import Engine
from src.serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
