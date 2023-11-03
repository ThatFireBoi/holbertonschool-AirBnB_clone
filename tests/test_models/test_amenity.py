#!/usr/bin/python3
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

    def test_attribute_values(self):
        self.assertEqual(self.amenity.name, "")

    def test_attribute_assignment(self):
        self.amenity.name = "Pool"
        self.assertEqual(self.amenity.name, "Pool")

    def test_save(self):
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)


if __name__ == '__main__':
    unittest.main()
