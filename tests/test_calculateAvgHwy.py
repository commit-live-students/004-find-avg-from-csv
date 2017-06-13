from unittest import TestCase
from errors import no_function_found, incorrect_output, succeed


class TestCalculateAvgHwy(TestCase):
    def test_calculateAvgHwy(self):
        try:
            from hwy_mpg import calculateAvgHwy
            result = calculateAvgHwy("./files/mpg.csv") # result => A dict object -> {'pickup':16.78, 'suv':'18.1290','minivan':22.363, ...}

            self.assertAlmostEqual(16.87878787878788, result["pickup"], places=3)

            self.assertAlmostEqual(18.129032258064516, result["suv"], places=3)

            self.assertAlmostEqual(22.363636363636363, result["minivan"], places=3)

            self.assertAlmostEqual(24.8, result["2seater"], places=3)

            self.assertAlmostEqual(27.29268292682927, result["midsize"], places=3)

            self.assertAlmostEqual(28.142857142857142, result["subcompact"], places=3)

            self.assertAlmostEqual(28.29787234042553, result["compact"], places=3)

            self.assertTrue(succeed("calculateAvgHwy"))
        except ImportError:
            self.assertFalse(no_function_found("calculateAvgHwy"))
        except AssertionError:
            self.assertFalse(incorrect_output())
