import unittest
from datetime import datetime
from src.battery.nubbin_battery import NubbinBattery
from src.battery.splinder_battery import SplinderBattery

from src.engine.capulet_engine import CapuletEngine
from src.engine.sternman_engine import SternmanEngine
from src.engine.willoughby_engine import WilloughbyEngine
from src.tires.carrigan_tires import CarriganTires
from src.tires.octoprime_tires import OctoprimeTires


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
        last_service_date = today.replace(year=today.year - 4)

        battery = SplinderBattery(
            today, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_dont_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

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


class TestCarriganTires(unittest.TestCase):
    def test_needs_service(self):
        tires_worned = [0.1, 0.8, 0.95, 0.8]

        tires = CarriganTires(tires_worned)
        self.assertTrue(tires.needs_service())

    def test_dont_needs_service(self):
        tires_worned = [0, 0, 0, 0]

        tires = CarriganTires(tires_worned)
        self.assertFalse(tires.needs_service())


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service(self):
        tires_worned = [0.8, 0.8, 0.8, 0.8]

        tires = OctoprimeTires(tires_worned)
        self.assertTrue(tires.needs_service())

    def test_dont_needs_service(self):
        tires_worned = [0, 0, 0, 0]

        tires = OctoprimeTires(tires_worned)
        self.assertFalse(tires.needs_service())


if __name__ == '__main__':
    unittest.main()
