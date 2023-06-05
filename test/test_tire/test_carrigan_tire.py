import unittest
from tire.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear = [0, 0, 0, 1]
        tire = CarriganTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear = [0, 0, 0, 0]
        tire = CarriganTire(tire_wear)
        self.assertFalse(tire.needs_service())  
