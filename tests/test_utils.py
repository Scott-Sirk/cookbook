
import os
import unittest
from cookbook.utils.file import File

class Test_File(unittest.TestCase):
    '''
    test classes/methods in the cookbook.utils module
    '''
    def setUp(self):
        self.file = File()

    def test_yield_lines(self):
        '''
        cookbook.utils.file.File.yield_lines
        '''
        gen = self.file.yield_lines(__file__)
        val = next(gen)
        #not sure what kind of assertion to make
        self.assertEqual('\n', val)

    def test_save_to_pickle(self):
        '''
        cookbook.utils.file.File.save_to_pickle
        '''
        data = [1, 2, 3]
        self.file.save_to_pickle(data, '.test.pkl')
        flag = os.path.isfile('.test.pkl')
        self.assertTrue(flag)

    def test_load_from_pickle(self):
        '''
        cookbook.utils.file.File.load_from_pickle
        '''
        data = [1, 2, 3]
        self.file.save_to_pickle(data, '.test.pkl')
        new_data = self.file.load_from_pickle('.test.pkl')
        self.assertEqual(data, new_data)

    def tearDown(self):
        if os.path.isfile('.test.pkl'):
            os.remove('.test.pkl')
