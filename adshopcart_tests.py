import unittest
import adshopcart_methods as methods



class AdshopcartPositiveTestCases(unittest.TestCase):

    @staticmethod
    def adshopcarttest():
        methods.setUp()
        methods.createnewaccount()
        methods.myaccount()
        methods.shoppingcart()
        methods.signout()
        methods.signin()
        methods.deleteuser()
        methods.checkifuserisdeleted()
        methods.setUp()
        methods.displays()
        methods.tabs()
        methods.contactus()
        methods.tearDown()
        methods.logger()
