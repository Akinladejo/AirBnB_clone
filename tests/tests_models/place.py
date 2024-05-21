#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlaceInstantiation
    TestPlaceSave
    TestPlaceToDict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlaceInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_instantiation_with_no_args(self):
        """Test instantiation with no arguments."""
        self.assertEqual(Place, type(Place()))

    def test_instance_stored_in_objects(self):
        """Test if the new instance is stored in objects."""
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_str(self):
        """Test if id attribute is of type string."""
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_datetime(self):
        """Test if created_at attribute is of type datetime."""
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_datetime(self):
        """Test if updated_at attribute is of type datetime."""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_default_values(self):
        """Test if default values are set correctly."""
        self.assertEqual("", Place.city_id)
        self.assertEqual("", Place.user_id)
        self.assertEqual("", Place.name)
        self.assertEqual("", Place.description)
        self.assertEqual(0, Place.number_rooms)
        self.assertEqual(0, Place.number_bathrooms)
        self.assertEqual(0, Place.max_guest)
        self.assertEqual(0, Place.price_by_night)
        self.assertEqual(0.0, Place.latitude)
        self.assertEqual(0.0, Place.longitude)
        self.assertEqual([], Place.amenity_ids)

    def test_unique_ids(self):
        """Test if two instances have unique ids."""
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    # Add more tests for other attributes...


class TestPlaceSave(unittest.TestCase):
    """Unittests for testing save method of the Place class."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except FileNotFoundError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp", "file.json")
        except FileNotFoundError:
            pass

    def test_save_updates_updated_at(self):
        """Test if save method updates updated_at."""
        place = Place()
        sleep(0.05)
        first_updated_at = place.updated_at
        place.save()
        self.assertLess(first_updated_at, place.updated_at)

    # Add more tests for save method...


class TestPlaceToDict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_to_dict_type(self):
        """Test if the output of to_dict is of type dictionary."""
        self.assertTrue(isinstance(Place().to_dict(), dict))

    def test_to_dict_keys(self):
        """Test if the output of to_dict contains correct keys."""
        place_dict = Place().to_dict()
        self.assertIn("id", place_dict)
        self.assertIn("created_at", place_dict)
        self.assertIn("updated_at", place_dict)
        self.assertIn("__class__", place_dict)

    # Add more tests for to_dict method...


if __name__ == "__main__":
    unittest.main()
