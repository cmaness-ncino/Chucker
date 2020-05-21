import src.WoodChuckExecutorFinal
import os
import unittest
from mock import Mock, patch

class TestWoodChuckExecutorFinal(unittest.TestCase):

    def test_estimate_chucking_distance(self):
        result = src.WoodChuckExecutorFinal.estimate_chucking_distance(wind_direction=360, temp=80, humidity=0.059, water_distance_in_kilometers=99, chucker_id=1)
        self.assertEqual(result, 5.680472727993916)

    def test_estimate_chucking_distance_wind_direction_out_of_bounds(self):
        self.assertRaises(Exception, src.WoodChuckExecutorFinal.estimate_chucking_distance, {"wind_direction":361, "temp":80, "humidity":0.059, "water_distance_in_kilometers":99, "chucker_id":1})

    def test_estimate_chucking_distance_humidity_out_of_bounds(self):
        self.assertRaises(Exception, src.WoodChuckExecutorFinal.estimate_chucking_distance, {"wind_direction":360, "temp":80, "humidity":2, "water_distance_in_kilometers":99, "chucker_id":1})

