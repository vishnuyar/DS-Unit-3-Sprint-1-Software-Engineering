import unittest
from acme import Product
from acme_report import generate_products,ADJECTIVES,NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are being generated as expected"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        """Test default product flammability being 0.5"""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_default_product_stealability(self):
        """Test default product stealabilty being Kinda stealable"""
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), "Kinda stealable.")

    def test_default_product_flamability(self):
        """Test default product explode is ...boom!"""
        prod = Product('Test Product')
        self.assertEqual(prod.explode(), "...boom!")

class AcmeReportTests(unittest.TestCase):
    """ Testing the Acme Reports to ensure they are upto the expectations """

    def test_default_num_products(self):
        """ Testign for defualt numer of products being 30 """
        self.products = generate_products()
        self.assertEqual(len(self.products),30)

    def test_legal_names(self):
        """ Testing for legal names of names generated from default products"""
        #Generating one product
        self.products = generate_products(1)
        #Splitting the name into adjective and noun
        self.adjective,self.noun = self.products[0].name.split(' ')
        #checking for adjective in ADJECTIVES
        self.assertIn(self.adjective,ADJECTIVES)
        #checking for noun in NOUNS
        self.assertIn(self.noun,NOUNS)


    


if __name__ == '__main__':
    unittest.main()