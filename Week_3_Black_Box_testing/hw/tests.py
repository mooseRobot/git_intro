import unittest
from credit_card_validator import credit_card_validator


class CreditCardTest(unittest.TestCase):
    def test1(self):
        """
        Verifies if check sum is correct
        """
        print(credit_card_validator(4000000000000002))
        self.assertTrue(credit_card_validator(4000000000000002))

    def test2(self):
        """
        Verify if credit_card_validator accurately identifies invalid cc prefixes.
        """
        self.assertFalse(credit_card_validator(3000000000000002))
        
    def test3(self):
        self.assertTrue(credit_card_validator('340000f00000000'))
        


if __name__ == '__main__':
    unittest.main()
    
    