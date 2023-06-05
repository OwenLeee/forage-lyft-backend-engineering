from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_wear=[]):
        self.tire_wear = tire_wear

    def needs_service(self):
        for tire in self.tire_wear:
            # one or more of the values in the tire wear array is greater than or equal to 0.9.
            if (tire >= 0.9):
                return True
        return False
