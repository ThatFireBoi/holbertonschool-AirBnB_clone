#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from tests.test_models.test_base_model import test_basemodel
import models
from datetime import datetime
from models.base_model import Base
from models.base_model import BaseModel

import unittest
from models.amenity import Amenity

"""
Unittest Module for Amenity class
"""


class TestAmenity(unittest.TestCase):
    """ Unittest for Amenity class """

    def test_object_Instantiation(self):
        """ instantiates class """
        self.amenity = Amenity()

    def setUp(self):
        self.amenity = Amenity()

    def testattr(self):
        """ test Class: Amenity attributes """
        self.amenity = Amenity()
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertFalse(hasattr(self.amenity, "random_attr"))
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertEqual(self.amenity.__class__.__name__, "Amenity")

    def testsave(self):
        """ testing method: save """
        self.amenity = Amenity()
        self.amenity.save()
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def teststr(self):
        """ testing __str__ return format of Amenity """
        self.amenity = Amenity()
        s = "[{}] ({}) {}".format(self.amenity.__class__.__name__,
                                  str(self.amenity.id), self.amenity.__dict__)
        self.assertEqual(print(s), print(self.amenity))

    def test_inheritance(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_methods(self):
        self.assertTrue(hasattr(Review, "save"))
        self.assertTrue(hasattr(Review, "to_dict"))

    def test_datetime_attributes(self):
        self.assertIsInstance(self.my_review.created_at, datetime)
        self.assertIsInstance(self.my_review.updated_at, datetime)

    def test_attribute_existence(self):
        self.assertTrue(hasattr(self.my_review, "place_id"))
        self.assertTrue(hasattr(self.my_review, "user_id"))
        self.assertTrue(hasattr(self.my_review, "text"))


if __name__ == '__main__':
    unittest.main()
