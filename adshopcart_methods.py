import sys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import adshopcart_locators as locators
from selenium import webdriver
from time import sleep
import datetime

s = Service('C:/Users/User/PycharmProjects/si/advantage_shopping_cart/chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    if driver is not None:
        print(f'Test started at: {datetime.datetime.now()}')
        print(f'--------------------------------------')

    driver.maximize_window()

    driver.implicitly_wait(30)

    driver.get(locators.adshopcart_url)

    if driver.current_url == locators.adshopcart_url:
        print(f'We\'re at the Advantage Shopping homepage -- {driver.title}')
    else:
        print(f'We\'re not at the Advantage Shopping homepage. Check your code!')
    try:
        assert 'Advantage Shopping' in driver.title
        print(f'Title is good!')
    except Exception as e:
        print(f'Title is not matching, check code please')

def createnewaccount():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(.5)
    driver.find_element(By.XPATH, "//a[text()='CREATE NEW ACCOUNT']").click()
    sleep(.5)
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.adshopcart_username)
    sleep(.5)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.adshopcart_email)
    sleep(.5)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.adshopcart_password)
    sleep(.5)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.adshopcart_password)
    sleep(.5)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.adshopcart_firstname)
    sleep(.5)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.adshopcart_lastname)
    sleep(.5)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.adshopcart_phonenumber)
    sleep(.5)
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(.5)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(1)

def myaccount():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='loginMiniTitle']//label[text()='My account']").click()
    sleep(.5)
    if driver.find_element(By.XPATH, "//*[@id='myAccountContainer']/div/div/div/label").is_displayed():
        print(f'The user with the name {locators.adshopcart_firstname} {locators.adshopcart_lastname} is displayed. Test passed.')
    sleep(.5)


def shoppingcart():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='loginMiniTitle']//label[text()='My orders']").click()
    sleep(1)
    if driver.find_element(By.XPATH, "//*[contains(@class, 'bigEmptyOrder')]//*[contains(@class, 'roboto-bold')]").is_displayed():
        print(f'You currently do not have any orders!')
    sleep(.5)

def signout():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='loginMiniTitle']//label[text()='Sign out']").click()
    sleep(1)

def logger():
    old_instance = sys.stdout
    log_file = open('message.log', 'w')
    sys.stdout = log_file
    print(f'Username {locators.adshopcart_username} \nPassword: {locators.adshopcart_password}')
    sys.stdout = old_instance
    log_file.close()

def signin():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(.5)
    driver.find_element(By.NAME, 'username').send_keys(locators.adshopcart_username)
    sleep(.5)
    driver.find_element(By.NAME, 'password').send_keys(locators.adshopcart_password)
    sleep(.5)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(.5)

def deleteuser():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='loginMiniTitle']//label[text()='My account']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//div[text()='Delete Account']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//div[text()='yes']").click()
    sleep(10)

def checkifuserisdeleted():
    driver.find_element(By.ID, 'hrefUserIcon').click()
    sleep(.5)
    driver.find_element(By.NAME, 'username').send_keys(locators.adshopcart_username)
    sleep(.5)
    driver.find_element(By.NAME, 'password').send_keys(locators.adshopcart_password)
    sleep(.5)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(.5)
    if driver.find_element(By.ID, 'signInResultMessage').is_displayed():
        print(f'You have successfully deleted the account.')


def tearDown():
    if driver is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()





setUp()
createnewaccount()
myaccount()
shoppingcart()
signout()
signin()
deleteuser()
checkifuserisdeleted()
logger()
tearDown()
