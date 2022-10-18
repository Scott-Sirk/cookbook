
import numpy as np
import unittest
from cookbook.ml.core import Core
from cookbook.ml.text_classifier import Text_Classifier

class Test_Core(unittest.TestCase):
    #not sure of best way to test this
    ##the only current function is calling crossfold validation
    ##but that needs data and a model, so not tested currently
    pass

class Test_Text_Classifier(unittest.TestCase):
    #not sure the best way to test this
    ##it needs data to do a lot of stuff
    ##so leaving un-tested for now
    pass
