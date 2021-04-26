import unittest
import numpy as np
import matplotlib.pyplot as plt
import lmfit
from xrd2021.curve_pre import curve

class TestCurve(unittest.TestCase):
    def test_values(self):
        self.assertRaises(ValueError, curve, "lala","data/too_short.txt")
