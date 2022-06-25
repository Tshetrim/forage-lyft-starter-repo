from datetime import date

from battery.nubbin_battery import NubbinBattery
from car import Car

from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory:
    def __init__(self):
        pass

    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
            engine = CapuletEngine(last_service_mileage, current_mileage)
            battery = SpindlerBattery(last_service_date, current_date)
            return Car(engine, battery)

    def create_glissade(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
            engine = WilloughbyEngine(last_service_mileage, current_mileage)
            battery = SpindlerBattery(last_service_date, current_date)
            return Car(engine, battery)

    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
            engine = SternmanEngine(warning_light_on)
            battery = SpindlerBattery(last_service_date, current_date)
            return Car(engine, battery)

    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
            engine = WilloughbyEngine(last_service_mileage, current_mileage)
            battery = NubbinBattery(last_service_date, current_date)
            return Car(engine, battery)

    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int)-> Car:
            engine = CapuletEngine(last_service_mileage, current_mileage)
            battery = NubbinBattery(last_service_date, current_date)
            return Car(engine, battery)
