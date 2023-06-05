from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        # Capulet Engine + Spindler Battery + Carrigan Tire
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        carrigan_tire = CarriganTire(tire_wear)
        return Car(capulet_engine, spindler_battery, carrigan_tire)

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        # Willoughby Engine + Spindler Battery + Carrigan Tire
        willoughby_engine = WilloughbyEngine(
            last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        carrigan_tire = CarriganTire(tire_wear)
        return Car(willoughby_engine, spindler_battery, carrigan_tire)

    def create_palindrome(current_date, last_service_date, warning_light_on, tire_wear):
        # Sternman Engine + Spindler Battery + Carrigan Tire
        sternman_engine = SternmanEngine(warning_light_on)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        carrigan_tire = CarriganTire(tire_wear)
        return Car(sternman_engine, spindler_battery, carrigan_tire)

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        # Willoughby Engine + Nubbin Battery + Octoprime Tire
        willoughby_engine = WilloughbyEngine(
            last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        octoprime_tire = OctoprimeTire(tire_wear)
        return Car(willoughby_engine, nubbin_battery, octoprime_tire)

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire_wear):
        # Capulet Engine + Nubbin Battery + Octoprime Tire
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        octoprime_tire = OctoprimeTire(tire_wear)
        return Car(capulet_engine, nubbin_battery, octoprime_tire)
