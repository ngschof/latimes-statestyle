#! /usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import statestyle


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.good_postals = ['CA', 'IA', 'dc', 'iL ']
        self.bad_postals = ['XX', 'xx', 'Xx']
        self.good_names = ['Washington DC', 'California', 'Iowa', 'district of columbia', 'ILLINOIS']
        self.bad_names = ['Los Angeles', 'Cedar Rapids', 'Shaw', 'CHICAGO']
        self.good_fips = ['6', '19', 11, 17, '08']
        self.bad_fips = [-6, '190', '11x ', 0]
        self.good_ap = ['Calif.', 'Iowa', 'd.c.', 'ILL.']
        self.bad_ap = ['Cali', 'iow', 'CD', 'ILLI']


class GetTest(BaseTest):

    def test_attr(self):
        obj = statestyle.get("CA")
        self.assertEqual(obj.postal, 'CA')
        self.assertEqual(obj.fips, '6')
        self.assertEqual(obj.name, 'California')
        self.assertEqual(obj.type, 'state')
        self.assertEqual(obj.ap, 'Calif.')
        self.assertEqual(obj.stateface, 'E')
        obj.__repr__()
        obj.__str__()
        obj.__unicode__()

    def test_postals(self):
        for i in self.good_postals:
            statestyle.get(i)
        for i in self.bad_postals:
            self.assertRaises(ValueError, statestyle.get, i)

    def test_names(self):
        for i in self.good_names:
            statestyle.get(i)
        for i in self.bad_names:
            self.assertRaises(ValueError, statestyle.get, i)

    def test_fips(self):
        for i in self.good_fips:
            statestyle.get(i)
        for i in self.bad_fips:
            self.assertRaises(ValueError, statestyle.get, i)

    def test_ap(self):
        for i in self.good_ap:
            statestyle.get(i)
        for i in self.bad_ap:
            self.assertRaises(ValueError, statestyle.get, i)

    def test_dict(self):
        o = statestyle.get("IA")
        self.assertEqual(o['ap'], o.ap)
        with self.assertRaises(AttributeError):
            o['foobar']
        self.assertDictEqual(o.__dict__, o.to_dict())
        self.assertDictEqual(dict(o), o.to_dict())
        self.assertDictEqual(dict(o), o.__dict__)


if __name__ == '__main__':
    unittest.main()
