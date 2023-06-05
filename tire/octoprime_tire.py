from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, tire_wear=[]):
        self.tire_wear = tire_wear

    def needs_service(self):
        # sum of all values in the tire wear array is greater than or equal to 3.
        sum_of_value = sum(self.tire_wear)
        return sum_of_value >= 3
