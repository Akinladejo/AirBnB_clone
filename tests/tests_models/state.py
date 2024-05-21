#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestState_instantiation
    TestState_save
    TestState_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

      def test_to_dict_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        st = State()
        self.assertIn("id", st.to_dict())
        self.assertIn("created_at", st.to_dict())
        self.assertIn("updated_at", st.to_dict())
        self.assertIn("__class__", st.to_dict())

    def test_to_dict_contains_added_attributes(self):
        st = State()
        st.middle_name = "Holberton"
        st.my_number = 98
        self.assertEqual("Holberton", st.middle_name)
        self.assertIn("my_number", st.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        st = State()
        st_dict = st.to_dict()
        self.assertEqual(str, type(st_dict["id"]))
        self.assertEqual(str, type(st_dict["created_at"]))
        self.assertEqual(str, type(st_dict["updated_at"]))

    def test_to_dict_output(self):
        dt = datetime.today()
        st = State()
        st.id = "123456"
        st.created_at = st.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(st.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        st = State()
        self.assertNotEqual(st.to_dict(), st.__dict__)

    def test_to_dict_with_arg(self):
        st = State()
        with self.assertRaises(TypeError):
            st.to_dict(None)

    def test_to_dict_includes_all_attributes(self):
        st = State()
        st.name = "California"
        st.some_other_attribute = "value"
        st_dict = st.to_dict()
        self.assertIn("name", st_dict)
        self.assertEqual(st_dict["name"], "California")
        self.assertIn("some_other_attribute", st_dict)
        self.assertEqual(st_dict["some_other_attribute"], "value")

    def test_to_dict_with_custom_attributes(self):
        st = State()
        st.custom_attr = "custom_value"
        st_dict = st.to_dict()
        self.assertIn("custom_attr", st_dict)
        self.assertEqual(st_dict["custom_attr"], "custom_value")

    def test_to_dict_with_empty_values(self):
        st = State()
        st.name = ""
        st_dict = st.to_dict()
        self.assertIn("name", st_dict)
        self.assertEqual(st_dict["name"], "")

    def test_to_dict_with_null_values(self):
        st = State()
        st.name = None
        st_dict = st.to_dict()
        self.assertIn("name", st_dict)
        self.assertIsNone(st_dict["name"])

    def test_to_dict_does_not_modify_instance(self):
        st = State()
        original_state_dict = st.__dict__.copy()
        st.to_dict()
        self.assertDictEqual(st.__dict__, original_state_dict)

        if __name__ == "__main__":
    unittest.main()
