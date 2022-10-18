
from sklearn.model_selection import cross_validate
from cookbook.utils.file import File

class Core():
    '''
    general functionality shared across machine learning projects

    Attributes:
        <cookbook.utils.file.File> file: instance of the file class
    '''
    def __init__(self):
        '''
        save an instance of the file class to the Core class
        and return an instance of Core

        Args:
            None

        Returns:
            <cookbook.ml.core.Core>: instance of Core class

        Raises:
            N/A
        '''
        self.file = File()

    def validate(self, model, X, answer_file, cv=5, show=True):
        '''
        call sklearn's cross_validation utility
        only major difference is this method will read targets from
            the answer_file instead of already expecting them
            to be in an array

        Args:
            <object> model: trained sklearn model
            <scipy.csr_matrix> X: matrix of features
            <str> answer_file: path to file where each line is an answer
            <int> cv(5): number of cross-folds to validate with
            <bool> show(True): if True print test_score results

        Returns:
            <dict>: dict of lists returned by sklearn.model_selection.cross_validate

        Raises:
            N/A
        '''
        #read answers into memory as a list
        with open(answer_file, 'r') as f:
            y = f.readlines()
        #validate, and show results if requested
        results = cross_validate(model, X, y, cv=cv)
        if show:
            print(results['test_score'])
        return results
