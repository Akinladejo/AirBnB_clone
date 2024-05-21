#!/usr/bin/python3
"""Defines unittests for models/city.py."""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCityInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args_instantiates(self):
        """Test instantiation of City class with no arguments."""
        self.assertIsInstance(City(), City)

    def test_new_instance_stored_in_objects(self):
        """Test if a new instance is stored in objects."""
        city_instance = City()
        self.assertIn(city_instance, models.storage.all().values())

    def test_attributes_types(self):
        """Test types of attributes."""
        city_instance = City()
        self.assertIsInstance(city_instance.id, str)
        self.assertIsInstance(city_instance.created_at, datetime)
        self.assertIsInstance(city_instance.updated_at, datetime)
        self.assertIsInstance(City.state_id, str)
        self.assertIsInstance(City.name, str)

    def test_two_cities_unique_ids(self):
        """Test if two City instances have unique IDs."""
        city_instance1 = City()
        city_instance2 = City()
        self.assertNotEqual(city_instance1.id, city_instance2.id)

    def test_two_cities_different_created_at(self):
        """Test if two City instances have different created_at times."""
        city_instance1 = City()
        sleep(0.05)
        city_instance2 = City()
        self.assertLess(city_instance1.created_at, city_instance2.created_at)

    def test_two_cities_different_updated_at(self):
        """Test if two City instances have different updated_at times."""
        city_instance1 = City()
        sleep(0.05)
        city_instance2 = City()
        self.assertLess(city_instance1.updated_at, city_instance2.updated_at)

    def test_str_representation(self):
        """Test if str representation is formatted correctly."""
        city_instance = City()
        dt = datetime.today()
        city_instance.id = "123456"
        city_instance.created_at = city_instance.updated_at = dt
        city_str = str(city_instance)
        self.assertIn("[City] (123456)", city_str)
        self.assertIn("'id': '123456'", city_str)
        self.assertIn("'created_at': " + repr(dt), city_str)
        self.assertIn("'updated_at': " + repr(dt), city_str)

    def test_instantiation_with_kwargs(self):
        """Test instantiation of City with kwargs."""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        city_instance = City(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(city_instance.id, "345")
        self.assertEqual(city_instance.created_at, dt)
        self.assertEqual(city_instance.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """Test instantiation of City with None kwargs."""
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCitySave(unittest.TestCase):
    """Unittests for testing save method of the City class."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """Test if save method updates the updated_at attribute."""
        city_instance = City()
        sleep(0.05)
        first_updated_at = city_instance.updated_at
        city_instance.save()
        self.assertLess(first_updated_at, city_instance.updated_at)

    def test_two_saves(self):
        """Test if two consecutive saves update updated_at."""
        city_instance = City()
        sleep(0.05)
        first_updated_at = city_instance.updated_at
        city_instance.save()
        second_updated_at = city_instance.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        city_instance.save()
        self.assertLess(second_updated_at, city_instance.updated_at)

    def test_save_updates_file(self):
        """Test if save method updates the file."""
        city_instance = City()
        city_instance.save()
        city_id = "City." + city_instance.id
        with open("file.json", "r") as f:
            self.assertIn(city_id, f.read())


class TestCityToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_to_dict_type(self):
        """Test type of to_dict method output."""
        self.assertIsInstance(City().to_dict(), dict)

    def test_to_dict_contains_correct_keys(self):
        """Test if to_dict method contains correct keys."""
        city_instance = City()
        city_dict = city_instance.to_dict()
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertIn("__class__", city_dict)

    def test_to_dict_contains_added_attributes(self):
        """Test if to_dict method contains added attributes."""
        city_instance = City()
        city_instance.middle_name = "Holberton"
        city_instance.my_number = 98
        city_dict = city_instance.to_dict()
        self.assertIn("middle_name", city_dict)
        self.assertIn("my_number", city_dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if datetime attributes in to_dict are strings."""
        city_instance = City()
        city_dict = city_instance.to_dict()
        self.assertIsInstance(city_dict["id"], str)
        self.assertIsInstance(city_dict["created_at"], str)
        self.assertIsInstance(city_dict["updated_at"], str)

    def test_to_dict_output(self):
        """Test output of to_dict method."""
        dt = datetime.today()
        city_instance = City()
        city_instance.id = "123456"
        city_instance.created_at = city_instance.updated_at = dt
        city_dict = city_instance.to_dict()
        expected_dict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(city_dict, expected_dict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test if to_dict method output differs from __dict__."""
        city_instance = City()
        self.assertNotEqual(city_instance.to_dict(), city_instance.__dict__)

    def test_to_dict_with_arg(self):
        """Test to_dict method with arguments."""
        city_instance = City()
        with self.assertRaises(TypeError):
            city_instance.to_dict(None)


if __name__ == "__main__":
    unittest.main()
