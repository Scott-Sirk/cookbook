
import argparse
import os
from cookbook.ml.text_classifier import Text_Classifier

#CLI to interact with cookbook.ml.text_classifier.Text_Classifier

if __name__ == '__main__':
    #make an instance of arguments parser
    parser = argparse.ArgumentParser()
    #take any number of files to read into the model as raw data
    parser.add_argument('--in-file', action='append')
    #file to save model to
    parser.add_argument('--save-as')
    args = parser.parse_args()
    #show arguments returned
    print(args)
    #create an instance of the Text_Classifier class
    tc = Text_Classifier()
    #convert files into a Bag-of-Words
    ##and write answers(where a answer is the file it was read from)
    ##to a local file named answers.txt
    words = tc.get_words(args.in_file, 'answers.txt')
    X, vectorizer = tc.convert_to_bow(words, binary=True)
    #train a model and use stratified kfold validation to eval the model
    model = tc.model(X, 'answers.txt')
    kfold_val = tc.validate(model, X, 'answers.txt')
    #save completed model for future use
    data = {
        'model':model
        , 'vocab':vectorizer.get_feature_names_out()
        }
    tc.file.save_to_pickle(data, args.save_as)
    #delete the answers.txt file, now that we shouldn't need it anymore
    if os.path.isfile('answers.txt'):
        os.remove('answers.txt')
