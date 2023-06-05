from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from factory.model.calliope import Calliope
from factory.model.thovex import Thovex
from model.glissade import Glissade
from model.palindrome import Palindrome
from model.rorschach import Rorschach


class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        # Capulet Engine + Spindler Battery
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        return Calliope(capulet_engine, spindler_battery)

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        # Willoughby Engine + Spindler Battery
        willoughby_engine = WilloughbyEngine(
            last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        return Glissade(willoughby_engine, spindler_battery)

    def create_palindrome(current_date, last_service_date, warning_light_on):
        # Sternman Engine + Spindler Battery
        sternman_engine = SternmanEngine(warning_light_on)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        return Palindrome(sternman_engine, spindler_battery)

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        # Willoughby Engine + Nubbin Battery
        willoughby_engine = WilloughbyEngine(
            last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        return Rorschach(willoughby_engine, nubbin_battery)

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        # Capulet Engine + Nubbin Battery
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        return Thovex(capulet_engine, nubbin_battery)
