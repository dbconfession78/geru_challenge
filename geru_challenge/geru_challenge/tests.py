"""
Module tests.py
"""
import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    """
    class definition for View Tests
    """
    def setUp(self):
        self.config = testing.setUp()
        import requests
        dct = requests.get("https://1c22eh3aj8.execute-api.us-east-1."
                           "amazonaws.com/challenge/quotes")
        js = dct.json()
        self.quotes = js['quotes']

    def tearDown(self):
        testing.tearDown()

    def test_get_quote_w_valid_quote_nums(self):
        """
        tests get_quote with all 19 quote numbers
        """
        from geru_challenge.views.views import RequestManager
        for i in range(1, 20):
            request = testing.DummyRequest()
            request.matchdict["quote_num"] = str(i)
            rm = RequestManager(request)
            response = rm.get_quote()
            self.assertEqual(response,
                             {'dct': {'quote': self.quotes[i-1], 'n': i}})

    def test_get_quote_w_invalid_quote_num(self):
        """
        tests that get_quote returns the proper message when an invalid quote
        number or type is passed
        """
        from geru_challenge.views.views import RequestManager
        for n in ['0', '20', 'monkey']:
            request = testing.DummyRequest()
            request.matchdict["quote_num"] = n
            rm = RequestManager(request)
            response = rm.get_quote()
            t_n = n if type(n) is not str or not n.isnumeric() else int(n)
            self.assertEqual(
                response, {
                    'dct': {'quote': ' is not a valid quote id.', 'n': t_n}})

    def test_get_quote_with_random(self):
        """
        tests get_quote/random
        """
        from geru_challenge.views.views import RequestManager
        request = testing.DummyRequest()
        request.matchdict["quote_num"] = "random"
        rm = RequestManager(request)
        r = rm.get_quote()
        quote = r.get('dct').get('quote')
        self.assertTrue(True, quote in self.quotes)

    def test_get_quotes(self):
        """
        tests that get_quotes returns all 19 dict entries
        """
        from geru_challenge.views.views import RequestManager
        request = testing.DummyRequest()
        rm = RequestManager(request)
        response = rm.get_quotes()
        print(response)
        self.assertEqual(response, {'dct': {'quotes': self.quotes}})

    # TODO: test api calls
