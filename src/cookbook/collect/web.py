
import requests
import pandas as pd

class Web():
    def __init__(self):
        pass

class Indiana_Web_API(Web):
    def __init__(self):
        super().__init__()

    def json_to_dataframe(self, response):
        '''
        Take the JSON response from hub.mph.in.gov GET request
            and format the raw response into a dataframe

        Args:
            <dict> response: JSON GET response from hub.mph.in.gov

        Returns:
            <pandas.DataFrame>: tabular data formatted from GET response

        Raises:
            N/A
        '''
        #build column names from the /result/fields section of the response
        columns = [d.get('id') for d in response.get('result', {}).get('fields', [])]
        #build the dataframe using expected data at /result/records section of the response
        df = pd.DataFrame(
            response.get('result', {}).get('records', [])
            , columns=columns
            )
        return df

    def query_data(self, data_id):
        '''
        Download state unemployment data returned as a DataFrame
            url and id for the GET request are hardcoded in the function

        Args:
            <str> data_id: ID of the table/page to pull from
                for example "8787939c-a268-4570-8f53-1ae50c85dc16"
                full URL: https://hub.mph.in.gov/dataset/equity-portal-dwd-unemployment-claimants/resource/8787939c-a268-4570-8f53-1ae50c85dc16

        Returns:
            <pandas.DataFrame>: formatted unemployment data

        Raises:
            N/A
        '''
        #build url to query data
        ##source: https://hub.mph.in.gov/dataset/equity-portal-dwd-unemployment-claimants/resource/8787939c-a268-4570-8f53-1ae50c85dc16
        ##documentation: https://hub.mph.in.gov/api/1/util/snippet/api_info.html?resource_id=8787939c-a268-4570-8f53-1ae50c85dc16
        base_url = 'https://hub.mph.in.gov/api/3/action/datastore_search_sql'
        sql = f'SELECT * FROM "{data_id}"'
        url = f'{base_url}?sql={sql}'
        #GET request
        response = requests.get(url)
        #load respose to dict
        json = response.json()
        #convert response from indiana api to dataframe
        df = self.json_to_dataframe(json)
        return df
