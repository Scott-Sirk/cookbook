
import argparse
import os
from cookbook.ml.text_classifier import Text_Classifier

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #location of pickle file with model and bag-of-words vocab
    parser.add_argument('--model-file')
    #location of file to load text and make predictions against
    parser.add_argument('--data-file', action='append')
    #flag to display the predictions made
    parser.add_argument('--show', action='store_true', default=False)
    #flag to use predict_proba instead of predict
    parser.add_argument('--proba', action='store_true', default=False)
    #save preds to a file?
    ##parser.add_argument('--save', nargs='?', default='')
    args = parser.parse_args()
    print(args)
    #make instance of the text classifier
    tc = Text_Classifier()
    #load the model and vocab into memory
    model_obj = tc.file.load_from_pickle(args.model_file)
    classifier = model_obj['model']
    vocab = model_obj['vocab']
    #convert data into bag-of-words with vocab expected by the model
    words = tc.get_words(args.data_file, '.dummy.txt')
    X, vectorizer = tc.convert_to_bow(words, binary=True, vocab=vocab)
    #make predictions given our features
    if args.proba:
        preds = classifier.predict_proba(X)
    else:
        preds = classifier.predict(X)
    #show preds if requested
    if args.show:
        print(preds)
    #delete the dummy "answers" file that was created as part of loading the data
    if os.path.isfile('.dummy.txt'):
        os.remove('.dummy.txt')
        

    
