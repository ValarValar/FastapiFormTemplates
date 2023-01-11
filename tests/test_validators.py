import unittest

from utils.validators import convert_value_to_type


class ConvertionToTypeTestCase(unittest.TestCase):

    def test_email_convert(self):
        type_email = 'email'
        self.assertEqual(convert_value_to_type('hi@mail.ru'), type_email)
        self.assertEqual(convert_value_to_type('79897026268@mail.ru'), type_email)
        self.assertEqual(convert_value_to_type('1@mail.ru'), type_email)
        self.assertEqual(convert_value_to_type('28.12.2020@google.com'), type_email)

        self.assertNotEqual(convert_value_to_type('hi@'), type_email)
        self.assertNotEqual(convert_value_to_type('79897026268@mail'), type_email)
        self.assertNotEqual(convert_value_to_type('28.12.2020'), type_email)

    def test_phone_number_convert(self):
        phone = 'phone'

        self.assertEqual(convert_value_to_type('+79897026268'), phone)
        self.assertEqual(convert_value_to_type('+7 989 702 62 68'), phone)

        self.assertNotEqual(convert_value_to_type('+995 543 12 12'), phone)
        self.assertNotEqual(convert_value_to_type('79897026268@mail.ru'), phone)
        self.assertNotEqual(convert_value_to_type('7 989 702 62 68'), phone)
        self.assertNotEqual(convert_value_to_type('8 989 702 62 68'), phone)
        self.assertNotEqual(convert_value_to_type('+798970262681'), phone)

    def test_date_convert(self):
        date = 'date'

        self.assertEqual(convert_value_to_type('24.02.2021'), date)
        self.assertEqual(convert_value_to_type('2021-02-24'), date)
        self.assertEqual(convert_value_to_type('1.1.2021'), date)

        self.assertNotEqual(convert_value_to_type('02.24.2021'), date)
        self.assertNotEqual(convert_value_to_type('24.02.21'), date)
        self.assertNotEqual(convert_value_to_type('02.24.2021'), date)
        self.assertNotEqual(convert_value_to_type('24-02-2021'), date)
