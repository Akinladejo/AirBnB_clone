#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""

import os
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenityInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        del self.amenity

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(self.amenity))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(self.amenity, Amenity.instances)

    def test_id_is_public_str(self):
        self.assertEqual(str, type(self.amenity.id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(self.amenity.created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(self.amenity.updated_at))

    def test_name_is_public_class_attribute(self):
        self.assertTrue(hasattr(Amenity, 'name'))
        self.assertFalse(hasattr(self.amenity, 'name'))

    def test_two_amenities_unique_ids(self):
        other_amenity = Amenity()
        self.assertNotEqual(self.amenity.id, other_amenity.id)

    def test_two_amenities_different_created_at(self):
        other_amenity = Amenity()
        sleep(0.05)
        self.assertLess(self.amenity.created_at, other_amenity.created_at)

    def test_two_amenities_different_updated_at(self):
        other_amenity = Amenity()
        sleep(0.05)
        self.assertLess(self.amenity.updated_at, other_amenity.updated_at)

    def test_str_representation(self):
        dt_repr = self.amenity.created_at.isoformat()
        self.assertEqual(
            str(self.amenity),
            "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__))

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dt = datetime.today()
        self.amenity = Amenity(id="345", created_at=dt, updated_at=dt)
        self.assertEqual(self.amenity.id, "345")
        self.assertEqual(self.amenity.created_at, dt)
        self.assertEqual(self.amenity.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenitySave(unittest.TestCase):
    """Unittests for testing save method of the Amenity class."""

    @classmethod
    def setUpClass(cls):
        cls.amenity = Amenity()

    @classmethod
    def tearDownClass(cls):
        del cls.amenity

    def test_one_save(self):
        first_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertLess(first_updated_at, self.amenity.updated_at)

    def test_two_saves(self):
        first_updated_at = self.amenity.updated_at
        self.amenity.save()
        second_updated_at = self.amenity.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        self.amenity.save()
        self.assertLess(second_updated_at, self.amenity.updated_at)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            self.amenity.save(None)

    def test_save_updates_file(self):
        amid = "Amenity." + self.amenity.id
        self.amenity.save()
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenityToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        del self.amenity

    def test_to_dict_type(self):
        self.assertTrue(dict, type(self.amenity.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        am_dict = self.amenity.to_dict()
        self.assertIn("id", am_dict)
        self.assertIn("created_at", am_dict)
        self.assertIn("updated_at", am_dict)
        self.assertIn("__class__", am_dict)

    def test_to_dict_contains_added_attributes(self):
        self.amenity.middle_name = "Holberton"
        self.amenity.my_number = 98
        am_dict = self.amenity.to_dict()
        self.assertEqual("Holberton", am_dict["middle_name"])
        self.assertIn("my_number", am_dict)

    def test_to_dict_datetime_attributes_are_strs(self):
        am_dict = self.amenity.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        self.amenity.id = "123456"
        self.amenity.created_at = dt
        self.amenity.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(self.amenity.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        self.assertNotEqual(self.amenity.to_dict(), self.amenity.__dict__)

    def test_to_dict_with_arg(self):
        with self.assertRaises(TypeError):
            self.amenity.to_dict(None)


if __name__ == "__main__":
    unittest.main()
