from datetime import datetime
from car import Car

from engine.sternman_engine import SternmanEngine


class Palindrome(Car):
    def __init__(self, engine, battery):
        super().__init__(engine, battery)
