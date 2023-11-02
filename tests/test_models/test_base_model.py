#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
"""
Unittest Module for BaseModel class
"""


class TestUser(unittest.TestCase):
    """Unittest for BaseModel class"""

    def setup(self):
        """ sets up an instance of BaseModel """
        self.basemodel = BaseModel()
        self.basemodel.name = "My First Base Model"
        self.basemodel.my_number = 89

    def test_object_Instantiation(self):
        """ instantiates class """
        self.basemodel = BaseModel()

    def test_checking_for_functions(self):
        """ checks if docstring exist """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def testattr(self):
        """ test Class: User attributes """
        self.basemodel = BaseModel()
        self.assertTrue(hasattr(self.basemodel, "created_at"))
        self.assertTrue(hasattr(self.basemodel, "updated_at"))
        self.assertFalse(hasattr(self.basemodel, "random_attr"))
        self.assertFalse(hasattr(self.basemodel, "name"))
        self.assertTrue(hasattr(self.basemodel, "id"))
        self.basemodel.name = "A"
        self.basemodel.age = "89"
        self.assertTrue(hasattr(self.basemodel, "name"))
        self.assertTrue(hasattr(self.basemodel, "age"))
        delattr(self.basemodel, "name")
        self.assertFalse(hasattr(self.basemodel, "name"))
        delattr(self.basemodel, "age")
        self.assertFalse(hasattr(self.basemodel, "age"))
        self.assertEqual(self.basemodel.__class__.__name__, "BaseModel")

    def testsave(self):
        """ testing method: save """
        self.basemodel = BaseModel()
        self.basemodel.save()
        self.assertTrue(hasattr(self.basemodel, "updated_at"))

    def teststr(self):
        """ testing __str__ return format of BaseModel """
        self.basemodel = BaseModel()
        s = "[{}] ({}) {}".format(self.basemodel.__class__.__name__,
                                  str(self.basemodel.id),
                                  self.basemodel.__dict__)
        self.assertEqual(print(s), print(self.basemodel))

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

    def tearDown(self):
        """ tears down instance of BaseModel"""
        del self.basemodel


if __name__ == '__main__':
    unittest.main()
