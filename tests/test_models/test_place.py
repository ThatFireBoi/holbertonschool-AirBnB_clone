#!/usr/bin/python3
"""
Unittest Module for Place
"""
import unittest
from models import storage
from models.user import User
from models.base_model import BaseModel
from models.engine import file_storage
from models.engine.file_storage import FileStorage
import os
import json
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Unittest for Place class """

    def test_attribute_existence(self):
        """ test that class Place has the required attributes"""
        self.assertTrue(hasattr(self.my_place, "city_id"))
        self.assertTrue(hasattr(self.my_place, "user_id"))
        self.assertTrue(hasattr(self.my_place, "name"))
        self.assertTrue(hasattr(self.my_place, "description"))
        self.assertTrue(hasattr(self.my_place, "number_rooms"))
        self.assertTrue(hasattr(self.my_place, "number_bathrooms"))
        self.assertTrue(hasattr(self.my_place, "max_guest"))
        self.assertTrue(hasattr(self.my_place, "price_by_night"))
        self.assertTrue(hasattr(self.my_place, "latitude"))
        self.assertTrue(hasattr(self.my_place, "longitude"))
        self.assertTrue(hasattr(self.my_place, "amenity_ids"))

    def test_attribute_values(self):
        self.assertEqual(self.my_place.city_id, "")
        self.assertEqual(self.my_place.user_id, "")
        self.assertEqual(self.my_place.name, "")
        self.assertEqual(self.my_place.description, "")
        self.assertEqual(self.my_place.number_rooms, 0)
        self.assertEqual(self.my_place.number_bathrooms, 0)
        self.assertEqual(self.my_place.max_guest, 0)
        self.assertEqual(self.my_place.price_by_night, 0)
        self.assertEqual(self.my_place.latitude, 0.0)
        self.assertEqual(self.my_place.longitude, 0.0)
        self.assertEqual(self.my_place.amenity_ids, [])

    def test_methods(self):
        self.assertTrue(hasattr(Place, "save"))
        self.assertTrue(hasattr(Place, "to_dict"))

    def test_str(self):
        self.assertEqual(str(self.my_place),
                         "[Place] ({}) {}".format(self.my_place.id, self.my_place.__dict__))

    def test_save(self):
        old_updated_at = self.my_place.updated_at
        self.my_place.save()
        self.assertNotEqual(old_updated_at, self.my_place.updated_at)


if __name__ == '__main__':
    unittest.main()
