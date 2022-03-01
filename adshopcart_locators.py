from faker import Faker

fake = Faker(locale='en_CA')
adshopcart_url = 'https://advantageonlineshopping.com/#/'
adshopcart_username = fake.user_name()
adshopcart_email = fake.email()
adshopcart_password = fake.password()
adshopcart_firstname = fake.first_name()
adshopcart_lastname = fake.last_name()
adshopcart_phonenumber = fake.phone_number()
