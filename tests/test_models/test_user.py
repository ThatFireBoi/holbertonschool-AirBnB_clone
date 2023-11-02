#!/usr/bin/python3

import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.my_user = User()
        cls.my_user.first_name = "Betty"
        cls.my_user.last_name = "Bar"
        cls.my_user.email = "airbnb@mail.com"
        cls.my_user.password = "root"

    @classmethod
    def tearDownClass(cls):
        del cls.my_user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def setUp(self):
        """set up for testing"""
        self.my_user = User()

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.my_user.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(User.__doc__)

    def test_has_attributes(self):
        self.assertTrue('email' in self.my_user.__dict__)
        self.assertTrue('id' in self.my_user.__dict__)
        self.assertTrue('created_at' in self.my_user.__dict__)
        self.assertTrue('updated_at' in self.my_user.__dict__)
        self.assertTrue('password' in self.my_user.__dict__)
        self.assertTrue('first_name' in self.my_user.__dict__)
        self.assertTrue('last_name' in self.my_user.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.my_user.email), str)
        self.assertEqual(type(self.my_user.password), str)
        self.assertEqual(type(self.my_user.first_name), str)
        self.assertEqual(type(self.my_user.first_name), str)

    def test_save(self):
        self.my_user.save()
        self.assertNotEqual(self.my_user.created_at, self.my_user.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.my_user), True)

    def test_attribute_values(self):
        self.assertEqual(self.my_user.email, "")
        self.assertEqual(self.my_user.password, "")
        self.assertEqual(self.my_user.first_name, "")
        self.assertEqual(self.my_user.last_name, "")

    def test_attribute_assignment(self):
        self.my_user.email = "test@email.com"
        self.my_user.password = "password123"
        self.my_user.first_name = "John"
        self.my_user.last_name = "Doe"
        self.assertEqual(self.my_user.email, "test@email.com")
        self.assertEqual(self.my_user.password, "password123")
        self.assertEqual(self.my_user.first_name, "John")
        self.assertEqual(self.my_user.last_name, "Doe")

    def test_inheritance(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_methods(self):
        self.assertTrue(hasattr(User, "save"))
        self.assertTrue(hasattr(User, "to_dict"))

    def test_str(self):
        self.assertEqual(str(self.my_user),
                         "[User] ({}) {}".format(self.my_user.id,
                                                 self.my_user.__dict__))


def test_attribute_values(self):
    self.assertEqual(self.my_city.name, "")
    self.assertEqual(self.my_city.state_id, "")


def test_str(self):
    self.assertEqual(str(self.my_city), "[City] ({}) {}".format(
        self.my_city.id, self.my_city.__dict__))


def test_save(self):
    old_updated_at = self.my_city.updated_at
    self.my_city.save()
    self.assertNotEqual(old_updated_at, self.my_city.updated_at)


if __name__ == "__main__":
    unittest.main()
