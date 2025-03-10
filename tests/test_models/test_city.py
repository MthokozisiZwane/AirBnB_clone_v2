#!/usr/bin/python3
""" test for city """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pycodestyle
import unittest
import pep8
from models.base_model import BaseModel
from os import getenv
storage_t = getenv("HBNB_TYPE_STORAGE")
import inspect

class test_City(test_basemodel):
    """  test for city class"""

    def __init__(self, *args, **kwargs):
        """initiakize """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):

        """Test state"""
        new = self.value()
        if storage_t == 'db':
            # If using a database, state_id attribute should not be None
            self.assertIsNotNone(new.state_id)
            self.assertEqual(type(new.state_id), str)
        else:
            # If using FileStorage, state_id attribute should be an empty string
            self.assertEqual(new.state_id, None)

    def test_name(self):
        """Test name"""
        new = self.value()
        if storage_t == 'db':
            # If using a database, name attribute should not be None
            self.assertIsNotNone(new.name)
            self.assertEqual(type(new.name), str)
        else:
            # If using FileStorage, name attribute should be an empty string
            self.assertEqual(new.name, None)


class Test_PEP8(unittest.TestCase):
    """test User"""

    def test_pep8_user(self):
        """test pep8 style"""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestCity(unittest.TestCase):
    """ test fot City"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):
        """ tear down after test"""
        del cls.city

    def tearDown(self):
        """tear down"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_City(self):
        """checking for docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """checking if City have attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """test if City is subclass of Basemodel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_City(self):
        """test attribute type for City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_save_City(self):
        """test if the save works"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.city), True)


if __name__ == "__main__":
    unittest.main()
