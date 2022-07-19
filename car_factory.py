from datetime import date

from car import Car

from batteries.nubbin_battery import NubbinBattery
from batteries.spindler_battery import SpindlerBattery

from engines.capulet_engine import CapuletEngine
from engines.sternman_engine import SternmanEngine
from engines.willoughby_engine import WilloughbyEngine

from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class CarFactory:
        @staticmethod
        def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, listTires: list) -> Car:
                engine = CapuletEngine(last_service_mileage, current_mileage)
                battery = SpindlerBattery(last_service_date, current_date)
                tires = CarriganTires(listTires)
                return Car(engine, battery, tires)

        @staticmethod
        def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, listTires: list) -> Car:
                engine = WilloughbyEngine(last_service_mileage, current_mileage)
                battery = SpindlerBattery(last_service_date, current_date)
                tires = CarriganTires(listTires)
                return Car(engine, battery, tires)

        @staticmethod
        def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool, listTires: list) -> Car:
                engine = SternmanEngine(warning_light_on)
                battery = SpindlerBattery(last_service_date, current_date)
                tires = CarriganTires(listTires)
                return Car(engine, battery, tires)

        @staticmethod
        def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, listTires: list) -> Car:
                engine = WilloughbyEngine(last_service_mileage, current_mileage)
                battery = NubbinBattery(last_service_date, current_date)
                tires = OctoprimeTires(listTires)
                return Car(engine, battery, tires)

        @staticmethod
        def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, listTires: list)-> Car:
                engine = CapuletEngine(last_service_mileage, current_mileage)
                battery = NubbinBattery(last_service_date, current_date)
                tires = OctoprimeTires(listTires)
                return Car(engine, battery, tires)
