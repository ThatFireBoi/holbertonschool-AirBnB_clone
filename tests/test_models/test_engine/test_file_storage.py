#!/usr/bin/python3
"""
Unittest Module for FileStorage
"""
import unittest
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json


class TestFileStorage(unittest.TestCase):
    """ Unittest for FileStorage class """

    def setUp(self):
        """ sets up an instance of FileStorage """
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.obj.id = 999999

    def test_all(self):
        """ test all method """
        self.assertIsInstance(self.storage, FileStorage)

    def test_Instantiation(self):
        """ checks instance is of class BaseModel """
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_Access(self):
        """ test read-write access permissions """
        rd = os.access('models/engine/file_storage.py', os.R_OK)
        self.assertTrue(rd)
        wr = os.access('models/engine/file_storage.py', os.W_OK)
        self.assertTrue(wr)
        ex = os.access('models/engine/file_storage.py', os.X_OK)
        self.assertFalse(ex)

    def test_new(self):
        """
        Tests method: new (saves new object into dictionary)
        """
        m_storage = FileStorage()
        instances_dic = m_storage.all()
        Aman = User()
        Aman.id = 999999
        Aman.name = "Aman"
        m_storage.new(Aman)
        key = Aman.__class__.__name__ + "." + str(Aman.id)
        self.assertIsNotNone(instances_dic[key])

    def test_reload(self):
        """
        Tests method: reload (reloads objects from string file)
        """
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)

    def test_funcdocs(self):
        """ testing functions docstring """
        for func in dir(FileStorage):
            self.assertTrue(len(func.__doc__) > 0)

    def test_save(self):
        """ tests save method"""
        obj = FileStorage()
        new_obj = BaseModel()
        obj.new(new_obj)
        dict1 = obj.all()
        obj.save()
        obj.reload()
        dict2 = obj.all()
        for key in dict1:
            key1 = key
        for key in dict2:
            key2 = key
        self.assertEqual(dict1[key1].to_dict(), dict2[key2].to_dict())

    def test_attribute_existence(self):
        self.assertTrue(hasattr(self.my_file_storage, "__file_path"))
        self.assertTrue(hasattr(self.my_file_storage, "__objects"))

    def test_methods(self):
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))

    def test_all(self):
        self.assertEqual(self.file_storage.all(),
                         self.file_storage._FileStorage__objects)

    def test_new(self):
        new_obj = BaseModel()
        self.my_file_storage.new(new_obj)
        key = "{}.{}".format(type(new_obj).__name__, new_obj.id)
        self.assertIn(key, self.file_storage.all())

    def test_save(self):
        self.file_storage.save()
        with open(self.file_storage._FileStorage__file_path, "r") as file:
            self.assertEqual(json.load(file), self.file_storage.all())

    def test_reload(self):
        self.file_storage.reload()
        with open(self.file_storage._FileStorage__file_path, "r") as file:
            self.assertEqual(json.load(file), self.file_storage.all())


if __name__ == '__main__':
    unittest.main()
