import adshopcart_locators as locators
from selenium import webdriver
import datetime


driver = webdriver.Chrome('C:/Users/User/PycharmProjects/si/advantage_shopping_cart/chromedriver.exe')

def setUp():
    if driver is not None:
        print(f'Test started at: {datetime.datetime.now()}')
        print(f'--------------------------------------')


    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser response in general
    driver.implicitly_wait(30)

    # Navigating to the Advantage Shopping website
    driver.get(locators.adshopcart_url)
    
    url_title = driver.title

    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.adshopcart_url and url_title == driver.title:
        print(f'We\'re at the Advantage Shopping Cart homepage -- {driver.title}')
        print(f'We\'re seeing title message -- "Advantage Shopping"')
    else:
        print(f'We\'re not at the Advantage Shopping homepage. Check your code!')
        driver.close()
        driver.quit()

def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()




setUp()
tearDown()
