import unittest
from test_mydict import MyDict


class TestMydict(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')


    def test_init(self):
        d = MyDict(name="ffl")
        self.assertEqual(d.name, 'ffl')
        self.assertIsInstance(d, dict)

    def test_key(self):
        d = MyDict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
        # self.assertEqual(d.key, 'value')

    def test_keyerror(self):
        d = MyDict()
        with self.assertRaises(KeyError):
            value = d["empty"]
        # with self.assertRaises(KeyError):
        # value = d['empty']

# if __name__ == '__main__':


unittest.main()