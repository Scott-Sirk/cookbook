
import pandas as pd
import unittest
from cookbook.collect.web import Indiana_Web_API

class Test_Indiana_Web_API(unittest.TestCase):
    '''
    test classes/methods in cookbook.collect
    '''
    def setUp(self):
        self.api = Indiana_Web_API()

    def test_query_data(self):
        '''
        cookbook.collect.web.Indiana_Web_API.query_data
        '''
        #json_to_dataframe called as part of this
        ##so that function is not tested indivdually
        data_id = '8787939c-a268-4570-8f53-1ae50c85dc16'
        df = self.api.query_data(data_id)
        self.assertIsInstance(df, pd.DataFrame)

    def tearDown(self):
        pass
