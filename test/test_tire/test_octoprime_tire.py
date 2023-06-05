import unittest
from tire.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tire_wear = [0, 1, 1, 1]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tire_wear = [0, 0, 0, 0]
        tire = OctoprimeTire(tire_wear)
        self.assertFalse(tire.needs_service())  
