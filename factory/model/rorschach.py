from datetime import datetime
from car import Car


class Rorschach(Car):
    def __init__(self, engine, battery):
        super().__init__(engine, battery)
