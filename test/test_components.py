import unittest
from datetime import datetime
from src.battery.models.nubbin_battery import NubbinBattery
from src.battery.models.splinder_battery import SplinderBattery

from src.engine.models.capulet_engine import CapuletEngine
from src.engine.models.sternman_engine import SternmanEngine
from src.engine.models.willoughby_engine import WilloughbyEngine


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        battery = NubbinBattery(
            today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_dont_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = NubbinBattery(
            today, last_service_date)
        self.assertFalse(battery.needs_service())


class TestSplinderBattery(unittest.TestCase):
    def test_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)

        battery = SplinderBattery(
            today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_dont_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        battery = SplinderBattery(
            today, last_service_date)
        self.assertFalse(battery.needs_service())


class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(
            current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_dont_needs_service(self):
        current_mileage = 0
        last_service_mileage = 0

        engine = CapuletEngine(
            current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(
            current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_dont_needs_service(self):
        current_mileage = 0
        last_service_mileage = 0

        engine = WilloughbyEngine(
            current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_dont_needs_service(self):
        warning_light_is_on = False

        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
