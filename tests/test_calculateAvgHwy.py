from unittest import TestCase
from errors import no_function_found, incorrect_output, succeed


class TestCalculateAvgHwy(TestCase):
    def test_calculateAvgHwy(self):
        try:
            from hwy_mpg import calculateAvgHwy
            result = calculateAvgHwy("../files/mpg.csv")
            self.assertEqual(16.87878787878788, result[0][1])
            self.assertEqual("pickup", result[0][0])

            self.assertEqual(18.129032258064516, result[1][1])
            self.assertEqual("suv", result[1][0])

            self.assertEqual(22.363636363636363, result[2][1])
            self.assertEqual("minivan", result[2][0])

            self.assertEqual(24.8, result[3][1])
            self.assertEqual("2seater", result[3][0])

            self.assertEqual(27.29268292682927, result[4][1])
            self.assertEqual("midsize", result[4][0])

            self.assertEqual(28.142857142857142, result[5][1])
            self.assertEqual("subcompact", result[5][0])

            self.assertEqual(28.29787234042553, result[6][1])
            self.assertEqual("compact", result[6][0])
            self.assertTrue(succeed("calculateAvgHwy"))
        except ImportError:
            self.assertFalse(no_function_found("calculateAvgHwy"))
        except AssertionError:
            self.assertFalse(incorrect_output())