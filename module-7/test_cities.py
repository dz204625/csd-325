import unittest
from city_functions import city_country

class test_city_country(unittest.TestCase):
    def test_city_country(self):
        city_country_results = city_country("shenyang", "china")

        print(city_country_results)
        self.assertEqual("Shenyang, China", city_country_results)

if __name__ == '__main__':
       unittest.main()