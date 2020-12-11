import unittest
from models.merchant import Merchant

class TestMerchant(unittest.TestCase):
    def setUp(self):
        self.merchant_1 = Merchant("Tesco")

    def test_merchant_has_name(self):
        self.assertEqual("Tesco", self.merchant_1.name)