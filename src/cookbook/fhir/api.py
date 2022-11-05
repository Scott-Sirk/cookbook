
import pprint
import requests

class Api():
    '''
    base class with general utils for FHIR api

    Attributes:
        <pprint.PrettyPrinter> pp: instance of python's pretty printer
            can be useful for reading JSON objects
    '''
    def __init__(self):
        '''
        create an instance of the Api class

        Args:
            None

        Returns:
            <cookbook.fhir.api.Api>: instance of class

        Raises:
            N/A
        '''
        self.pp = pprint.PrettyPrinter(indent=2)

class ApiOpenSandbox(Api):
    '''
    class to test with the API available at https://fhirsandbox.healthit.gov/open/r4/fhir
    inherits utils from the cookbook.fhir.api.Api class

    Attributes:
        <str> _base_url: base url for sandbox FHIR api
        <dict> _base_params: general params used across API requests
    '''
    def __init__(self):
        '''
        create an instance of the ApiOpenSandbox class

        Args:
            None

        Returns:
            <cookbook.fhir.api.ApiOpenSandbox>: instance of class

        Raises:
            N/A
        '''
        super().__init__()
        self._base_url = 'https://fhirsandbox.healthit.gov/open/r4/fhir'
        self._base_params = {'_format':'json'}

    def yield_patients(self):
        '''
        yield patients from the sandbox env.

        Args:
            None

        Returns:
            <generator>: iterable where each item is a dict
                of data from 'GET [base]/Patient'

        Raises:
            N/A
        '''
        #build url for GET request
        url = f'{self._base_url}/Patient'
        #get data from FHIR
        response = requests.get(url, params=self._base_params)
        patients = response.json().get('entry')
        #if request was successful
        if patients:
            #for each patient yield the results 1 at a time
            for patient in patients:
                yield patient.get('resource', {})

    def get_patient(self, pat_id):
        '''
        get a single patient given a patient ID

        Args:
            <str> pat_id: patient ID

        Returns:
            <dict>: data from 'GET [base]/Patient/[patient-id]'

        Raises:
            N/A
        '''
        #build url for GET request
        url = f'{self._base_url}/Patient/{pat_id}'
        #get data and return response
        response = requests.get(url, params=self._base_params)
        return response.json()

if __name__ == '__main__':

    api = ApiOpenSandbox()
    #api.get_patient('123d41e1-0f71-4e9f-8eb2-d1b1330201a6')
    patients = api.yield_patients()
    for p in patients:
        print(p['id'], p['name'])


