import unittest
from credit_card_validator import credit_card_validator


class CreditCardTest(unittest.TestCase):
    def test1(self):
        """
        Verifies if accurately identifies Visa cards
        """
        self.assertFalse(credit_card_validator('4000000000000002'))

    def test2(self):
        """
        Verify if credit_card_validator accurately identifies invalid credit card prefixes.
        and incorrect check sums
        """
        self.assertTrue(credit_card_validator('3000000000000002'))

    def test3(self):
        """
        Verify credit_card_validator accurately identifies blank credit card numbers
        """
        self.assertFalse(credit_card_validator(''))

    def test4(self):
        """
        Verify if accurately verifies incorrect Visa length (short)
        """
        self.assertTrue(credit_card_validator('435467356254371'))

    def test5(self):
        """
        Verify if accurately verifies incorrect Visa length (long)
        """
        self.assertFalse(credit_card_validator('44124235343534626'))

    def test6(self):
        """
        Verify credit_card_validator identifies short amex credit card numbers
        """
        self.assertFalse(credit_card_validator('34124235354626'))

    def test8(self):
        """
        Verify accurately identifies mastercard cards, (inclusive 51)
        """
        self.assertTrue(credit_card_validator('5142536334324564'))

    def test9(self):
        """
        Verify accurately identifies amex cards
        """
        self.assertFalse(credit_card_validator('343463456554464'))

    def test10(self):
        """
        Verify mastercard has incorrect checksum
        """
        self.assertFalse(credit_card_validator('5265465432264563'))

    def test11(self):
        """
        Verify if accurately identifies MasterCard length (short) and incorrect check sum
        """
        self.assertFalse(credit_card_validator('500000000000000'))

    def test12(self):
        """
        Verify if accurately identifies incorrect Visa check sum
        """
        self.assertFalse(credit_card_validator('4000000000000000'))

    def test13(self):
        """
        Verify if accurately MasterCard prefix range is correct 51-55 (lower bound exclusive)
        """
        self.assertFalse(credit_card_validator('5000000000000009'))

    def test14(self):
        """
        Verify if accurately MasterCard prefix range is correct 51-55 (upper bound inclusive)
        """
        self.assertFalse(credit_card_validator('5500000000000004'))

    def test15(self):
        """
        Verify if accurately MasterCard prefix range is correct 51-55 (upper bound exclusive)
        """
        self.assertFalse(credit_card_validator('5600000000000003'))

    def test16(self):
        """
        Verify if accurately MasterCard prefix range is correct 2221-2720 (lower bound exclusive)
        """
        self.assertFalse(credit_card_validator('2220000000000000'))

    def test17(self):
        """
        Verify if accurately MasterCard prefix range is correct 2221-2720 (lower bound inclusive)
        """
        self.assertFalse(credit_card_validator('2221000000000009'))

    def test18(self):
        """
        Verify if accurately MasterCard prefix range is correct 2221-2720 (upper bound inclusive)
        """
        self.assertFalse(credit_card_validator('2720000000000005'))

    def test19(self):
        """
        Verify if accurately MasterCard prefix range is correct 2221-2720 (upper bound exclusive)
        """
        self.assertFalse(credit_card_validator('2721000000000004'))

    def test20(self):
        """
        Verify if accurately identifies amex credit card
        """
        self.assertFalse(credit_card_validator('370000000000002'))


if __name__ == '__main__':
    unittest.main()
