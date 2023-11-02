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
        self.user = User()

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        self.assertIsNotNone(User.__doc__)

    def test_has_attributes(self):
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.first_name), str)

    def test_save(self):
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.user), True)

    def test_attribute_values(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_attribute_assignment(self):
        self.user.email = "test@email.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.assertEqual(self.user.email, "test@email.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_inheritance(self):
        self.assertTrue(issubclass(User, BaseModel))

    def test_methods(self):
        self.assertTrue(hasattr(User, "save"))
        self.assertTrue(hasattr(User, "to_dict"))


if __name__ == "__main__":
    unittest.main()
