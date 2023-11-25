#!/usr/bin/python3
""" test for place"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import unittest


class test_Place(test_basemodel):
    """ place test"""

    def __init__(self, *args, **kwargs):
        """ initialize"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ city id"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)
        self.assertTrue(hasattr(new, 'city_id'))

    def test_user_id(self):
        """ user id"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)
        self.assertTrue(hasattr(new, 'user_id'))

    def test_name(self):
        """ name """
        new = self.value()
        self.assertEqual(type(new.name), str)
        self.assertTrue(hasattr(new, 'name'))

    def test_description(self):
        """ description"""
        new = self.value()
        self.assertEqual(type(new.description), str)
        self.assertTrue(hasattr(new, 'description'))

    def test_number_rooms(self):
        """ bumr rooms"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)
        self.assertEqual(new.number_rooms, 0)

    def test_number_bathrooms(self):
        """ bathroom no"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)
        self.assertEqual(new.number_bathrooms, 0)

    def test_max_guest(self):
        """ max guest """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)
        self.assertEqual(new.max_guest, 0)

    def test_price_by_night(self):
        """ price by night"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)
        self.assertEqual(new.price_by_night, 0)

    def test_latitude(self):
        """ latitude """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """ longitude"""
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        """test id """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
