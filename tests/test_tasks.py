# -*- coding: UTF-8 -*-
"""
A suite of tests for the functions in tasks.py
"""
import unittest
from unittest.mock import patch, MagicMock

from vlab_icap_api.lib.worker import tasks


class TestTasks(unittest.TestCase):
    """A set of test cases for tasks.py"""
    @patch.object(tasks, 'vmware')
    def test_show_ok(self, fake_vmware):
        """``show`` returns a dictionary when everything works as expected"""
        fake_vmware.show_icap.return_value = {'worked': True}

        output = tasks.show(username='bob')
        expected = {'content' : {'worked': True}, 'error': None, 'params': {}}

        self.assertEqual(output, expected)

    @patch.object(tasks, 'vmware')
    def test_show_value_error(self, fake_vmware):
        """``show`` sets the error in the dictionary to the ValueError message"""
        fake_vmware.show_icap.side_effect = [ValueError("testing")]

        output = tasks.show(username='bob')
        expected = {'content' : {}, 'error': 'testing', 'params': {}}

        self.assertEqual(output, expected)

    @patch.object(tasks, 'vmware')
    def test_create_ok(self, fake_vmware):
        """``create`` returns a dictionary when everything works as expected"""
        fake_vmware.create_icap.return_value = {'worked': True}

        output = tasks.create(username='bob',
                              machine_name='icapBox',
                              image='0.0.1',
                              network='someLAN')
        expected = {'content' : {'worked': True}, 'error': None, 'params': {}}

        self.assertEqual(output, expected)

    @patch.object(tasks, 'vmware')
    def test_create_value_error(self, fake_vmware):
        """``create`` sets the error in the dictionary to the ValueError message"""
        fake_vmware.create_icap.side_effect = [ValueError("testing")]

        output = tasks.create(username='bob',
                              machine_name='icapBox',
                              image='0.0.1',
                              network='someLAN')
        expected = {'content' : {}, 'error': 'testing', 'params': {}}

        self.assertEqual(output, expected)

    @patch.object(tasks, 'vmware')
    def test_delete_ok(self, fake_vmware):
        """``delete`` returns a dictionary when everything works as expected"""
        fake_vmware.delete_icap.return_value = {'worked': True}

        output = tasks.delete(username='bob', machine_name='icapBox')
        expected = {'content' : {}, 'error': None, 'params': {}}

        self.assertEqual(output, expected)

    @patch.object(tasks, 'vmware')
    def test_delete_value_error(self, fake_vmware):
        """``delete`` sets the error in the dictionary to the ValueError message"""
        fake_vmware.delete_icap.side_effect = [ValueError("testing")]

        output = tasks.delete(username='bob', machine_name='icapBox')
        expected = {'content' : {}, 'error': 'testing', 'params': {}}

        self.assertEqual(output, expected)


    @patch.object(tasks, 'vmware')
    def test_image(self, fake_vmware):
        """``image`` returns a dictionary when everything works as expected"""
        fake_vmware.list_images.return_value = ['1.0.0']

        output = tasks.image()
        expected = {'content' : {'image' : ['1.0.0']}, 'error': None, 'params' : {}}

        self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()