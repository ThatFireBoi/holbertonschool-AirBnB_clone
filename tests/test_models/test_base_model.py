#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
"""
Unittest Module for BaseModel class
"""


class TestUser(unittest.TestCase):
    """Unittest for BaseModel class"""

    def setUp(self):
        """ sets up an instance of BaseModel """
        self.base_model = BaseModel()

    def setup(self):
        """ sets up an instance of BaseModel """
        self.base_model = BaseModel()
        self.base_model.name = "My First Base Model"
        self.base_model.my_number = 89

    def test_object_Instantiation(self):
        """ instantiates class """
        self.base_model = BaseModel()

    def test_checking_for_functions(self):
        """ checks if docstring exist """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def testattr(self):
        """ test Class: User attributes """
        self.base_model = BaseModel()
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))
        self.assertFalse(hasattr(self.base_model, "random_attr"))
        self.assertFalse(hasattr(self.base_model, "name"))
        self.assertTrue(hasattr(self.base_model, "id"))
        self.base_model.name = "A"
        self.base_model.age = "89"
        self.assertTrue(hasattr(self.base_model, "name"))
        self.assertTrue(hasattr(self.base_model, "age"))
        delattr(self.base_model, "name")
        self.assertFalse(hasattr(self.base_model, "name"))
        delattr(self.base_model, "age")
        self.assertFalse(hasattr(self.base_model, "age"))
        self.assertEqual(self.base_model.__class__.__name__, "BaseModel")

    def testsave(self):
        """ testing method: save """
        self.base_model = BaseModel()
        self.base_model.save()
        self.assertTrue(hasattr(self.base_model, "updated_at"))

    def teststr(self):
        """ testing __str__ return format of BaseModel """
        self.base_model = BaseModel()
        s = "[{}] ({}) {}".format(self.base_model.__class__.__name__,
                                  str(self.base_model.id),
                                  self.base_model.__dict__)
        self.assertEqual(print(s), print(self.base_model))

    def test_to_dict(self):
        """ testing to_dict method"""
        base1 = BaseModel()
        base1_dict = base1.to_dict()
        self.assertEqual(base1.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base1_dict['created_at'], str)
        self.assertIsInstance(base1_dict['updated_at'], str)

    def test_init_no_kwargs(self):
        """ testing init without kwargs """
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_id(self):
        """ testing id """
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_created_at(self):
        """ testing created_at """
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)

    def test_updated_at(self):
        """ testing updated_at """
        bm = BaseModel()
        self.assertIsInstance(bm.updated_at, datetime)

    def test_attribute_existence(self):
        self.assertTrue(hasattr(self, "id"))
        self.assertTrue(hasattr(self, "created_at"))
        self.assertTrue(hasattr(self, "updated_at"))

    def test_attribute_values(self):
        self.assertIsInstance(self.id, str)
        self.assertIsInstance(self.created_at, datetime)
        self.assertIsInstance(self.updated_at, datetime)

    def test_methods(self):
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_str(self):
        self.assertEqual(str(self.base_model),
                         "[BaseModel] ({}) {}".format(self.base_model.id,
                                                      self.base_model.__dict__))


if __name__ == '__main__':
    unittest.main()
