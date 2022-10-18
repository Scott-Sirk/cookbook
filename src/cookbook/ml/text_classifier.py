
import os
import xml.etree.ElementTree as ET
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from cookbook.ml.core import Core as ml_core

class Text_Classifier(ml_core):
    '''
    create text classification model(comes from original "medical_text_classifier" model)

    Attributes:
        <cookbook.utils.file.File> file: instace of the File class
            inherited from cookbook.ml.core.Core
    '''
    def __init__(self):
        '''
        inherit attributes from cookbook.ml.core.Core
        and return an instance of the Text_Classifier class

        Args:
            None

        Returns:
            <cookbook.ml.text_classifier.Text_Classifier>: instance of the class

        Raises:
            N/A
        '''
        super().__init__()
    
    def get_words_from_flat_file(self, file):
        '''
        given a file yield each word
        where a word is defined as a string seperated by a single space

        Args:
            <str> file: path to file

        Returns:
            <generator>: iterable where each item is a string

        Raises:
            N/A
        '''
        #file File class to yield lines from large file
        gen = self.file.yield_lines(file)
        for line in gen:
            for word in line.split(' '):
                yield word

    def get_words_from_xml_file(self, file):
        '''
        given a file yield each word
        Note: the XML parse is expected to match the CDC ICD-10 XML file download
            just any old XML file probably won't work

        Args:
            <str> file: path to file to read

        Returns:
            <generator>: iterable where each item is a string

        Raises:
            N/A
        '''
        #use etree to get the root of the XML doc
        tree = ET.parse(file)
        root = tree.getroot()
        #for every item at the ./chapter/section/diag/diag path
        for element in root.findall('./chapter/section/diag/diag'):
            #get the name and description of each ICD-10 code in the file
            name = element.find('./name').text
            desc = element.find('./desc').text
            #combine name and description into a single string
            string = name + ' ' + desc
            #split and yield each word
            for word in string.split(' '):
                yield word

    def get_words(self, file_list, answer_file):
        '''
        given a list of files, and a file to write targets/answers to
        yield all words and write a line to the answer file for each word

        Args:
            <list> file_list: list of file paths to read from
            <str> answer_file: local file to write answers to
                for training the model
                Note: the file names are used of the "answer"

        Returns:
            <generator>: iterable where each item is a string(word)
                Note: a file will also be written at the "answer_file" location

        Raises:
            Exception: If an unknown file type(determined by extension)
                is passed execution will stop
        '''
        #open the answer file up top, so we don't constantly open/close the file
        with open(answer_file, 'w') as f:
            #for each file to process
            for file in file_list:
                file_path, ext = os.path.splitext(file)
                #based on the extension alias the function to process the data
                if ext == '.txt':
                    words_func = self.get_words_from_flat_file
                elif ext == '.xml':
                    words_func = self.get_words_from_xml_file
                #if the extension is not supported raise an error
                else:
                    print(os.path.splitext(file))
                    msg = 'Error Unsupported File Type'
                    msg += f'\n\tFile: {file}'
                    msg += f'\n\tExtension Split: "{file_path}" "{ext}"'
                    raise Exception(msg)
                #call our aliased function
                ##yield each word, and write an entry in our answer file
                for word in words_func(file):
                    f.write(file_path+'\n')
                    yield word

    def convert_to_bow(self, gen, vocab=None, min_df=25, binary=False):
        '''
        given a generator of strings convert the text data into a Bag-of-Words

        Args:
            <generator>: iterable of string yielded by something like get_words()
            <list> vocab(None): list of vocab for the Bag-of-Words to use
                by default will create a vocab as the matrix is created
            <int> min_df(25): minimum number of times to see a token
                before it is included in the Bag-of-Words
            <bool> binary(False): If True values in the Bag-of-Words will
                be 0/1 instead of a count of how many times the word
                appeared in the document(item in iterable)

        Returns:
            <scipy.csr_matrix> X: Bag-of-Words
            <sklean.feature_extraction.text.CountVectorizer>: instance of vectorizer that created the Bag-of-Words

        Raise:
            N/A
        '''
        #convert iterator of strings to bag-of-words
        cv = CountVectorizer(
            stop_words='english'
            , min_df=min_df
            , max_df=1.0
            , vocabulary=vocab
            , binary=binary
            )
        X = cv.fit_transform(gen)
        return X, cv

    def model(self, X, answer_file):
        '''
        create and return a SVM model for text-classification

        Args:
            <scipy.csr_matrix> X: feature matrix
            <str> answer_file: path to file with answers

        Returns:
            <sklearn.svm.svc.SVC>: instace of fitted model

        Raises:
            N/A
        '''
        #read answer file into array
        with open(answer_file, 'r') as f:
            y = f.readlines()
        #train and return model
        svc = SVC(probability=True)
        model = svc.fit(X, y)
        return model
