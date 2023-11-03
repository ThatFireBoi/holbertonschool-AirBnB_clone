#!/usr/bin/python3
import unittest
from models.place import Place
"""
Unittest Module for Place
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Unittest for Place class """

    def setUp(self):
        """ sets up an instance of Place """
        self.my_place = Place()

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

    def test_to_dict(self):
        """ test that to_dict method returns a dictionary"""
        place_dict = self.my_place.to_dict()
        self.assertEqual(type(place_dict), dict)
        self.assertTrue('id' in place_dict)
        self.assertTrue('created_at' in place_dict)
        self.assertTrue('updated_at' in place_dict)
        self.assertTrue('__class__' in place_dict)

    def test_attribute_values(self):
        """ test that all class attributes are empty strings or 0"""
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

    def test_attribute_types(self):
        """ test that all class attributes have correct types"""
        self.assertEqual(type(self.my_place.name), str)
        self.assertEqual(type(self.my_place.description), str)
        self.assertEqual(type(self.my_place.number_rooms), int)
        self.assertEqual(type(self.my_place.number_bathrooms), int)
        self.assertEqual(type(self.my_place.max_guest), int)
        self.assertEqual(type(self.my_place.price_by_night), int)
        self.assertEqual(type(self.my_place.latitude), float)
        self.assertEqual(type(self.my_place.longitude), float)
        self.assertEqual(type(self.my_place.amenity_ids), list)

    def test_methods(self):
        """ test that class Place has the required methods"""
        self.assertTrue(hasattr(Place, "save"))
        self.assertTrue(hasattr(Place, "to_dict"))

    def test_str(self):
        """ test that the str method has the correct output """
        self.assertEqual(str(self.my_place),
                         "[Place] ({}) {}".format(self.my_place.id,
                                                  self.my_place.__dict__))

    def test_save(self):
        """ test that the save method updates updated_at """
        old_updated_at = self.my_place.updated_at
        self.my_place.save()
        self.assertNotEqual(old_updated_at, self.my_place.updated_at)

    def test_instance_creation(self):
        """ test that an instance of Place successfully created"""
        self.assertIsInstance(self.my_place, Place)
        self.assertTrue(hasattr(self.my_place, "id"))
        self.assertTrue(hasattr(self.my_place, "created_at"))
        self.assertTrue(hasattr(self.my_place, "updated_at"))


if __name__ == '__main__':
    unittest.main()
