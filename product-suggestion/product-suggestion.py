import unittest

def product_suggestion(products, search_word):
    products.sort()

    res = []
    for i in range(len(search_word)):
        prefix = search_word[:i+1]

        suggested = []
        for product in products:
            if product.startswith(prefix):
                suggested.append(product)
            if len(suggested) >= 3:
                break
        res.append(suggested)
    return res

class Tests(unittest.TestCase):
    def test1(self):
        products = ["mobile","mouse","moneypot","monitor","mousepad"]
        search_word = "mouse"
        expected = [
            ["mobile","moneypot","monitor"],
            ["mobile","moneypot","monitor"],
            ["mouse","mousepad"],
            ["mouse","mousepad"],
            ["mouse","mousepad"]
        ]
        self.assertEqual(product_suggestion(products, search_word), expected)

    def test2(self):
        products = ["havana"]
        search_word = "havana"
        expected = [["havana"]] * len("havana")
        self.assertEqual(product_suggestion(products, search_word), expected)

    def test3(self):
        products = ["bags","baggage","banner","box","cloths"]
        search_word = "bags"
        expected = [
            ["baggage", "bags", "banner"],
            ["baggage", "bags", "banner"],
            ["baggage", "bags"],
            ["bags"]
        ]
        self.assertEqual(product_suggestion(products, search_word), expected)
    
    def test4(self):
        products = ["havana"]
        search_word = "tatiana"
        expected = [[]] * len("tatiana")
        self.assertEqual(product_suggestion(products, search_word), expected)


if __name__ == '__main__':
    unittest.main()