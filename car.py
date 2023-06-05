from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, tire=[0, 0, 0, 0]):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service() or self.tire.needs_service()
