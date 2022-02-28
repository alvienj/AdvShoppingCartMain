from selenium.webdriver.chrome.service import Service
import adshopcart_locators as locators
from selenium import webdriver
import datetime

s = Service('C:/Users/User/PycharmProjects/si/advantage_shopping_cart/chromedriver.exe')
driver = webdriver.Chrome(service=s)



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



    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.adshopcart_url:
        print(f'We\'re at the Advantage Shopping homepage -- {driver.title}')
    else:
        print(f'We\'re not at the Advantage Shopping homepage. Check your code!')
    try:
        assert 'Advantage Shopping' in driver.title
        print(f'Title is good!')
    except Exception as e:
        print(f'Title is not matching, check code please')



def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()


setUp()
tearDown()
