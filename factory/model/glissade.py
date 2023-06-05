from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine


class Glissade(WilloughbyEngine):
    def __init__(self, engine, battery):
        super().__init__(engine, battery)
