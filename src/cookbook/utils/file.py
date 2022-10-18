
import pickle

class File():
    '''
    general utils to work with files

    Attributes:
        None
    '''
    def __init__(self):
        '''
        return instance of File class

        Args:
            None

        Returns:
            <cookbook.utils.file.File>: instance of the class

        Raises:
            N/A
        '''
        pass

    def yield_lines(self, file):
        '''
        given a large file yield it's contents 1 line at a time

        Args:
            <str> file: path to file

        Returns:
            <generator>: iterator of strings where each item is a line from the file

        Raises:
            N/A
        '''
        with open(file, 'r') as f:
            for line in f:
                yield line

    def save_to_pickle(self, obj, file):
        '''
        save python object to pickle file

        Args:
            <object> obj: any python object
            <str> file: file to save object to

        Returns:
            None - write data to a file

        Raises:
            N/A
        '''
        with open(file, 'wb') as f:
            pickle.dump(obj, f)

    def load_from_pickle(self, file):
        '''
        load a pickle file's object into memory

        Args:
            <str> file: pickle file to load data from

        Returns:
            <object>: python object

        Raises:
            N/A
        '''
        with open(file, 'rb') as f:
            obj = pickle.load(f)
        return obj

    
