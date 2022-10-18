# Python Cookbook
-----------------

### Install
-----------
* Requirements:
	* Python3
* Instructions:
	1. download repo(git clone, etc.)
	2. `cd ./cookbook`
	3. `pip install .`

### Testing
-----------
1. Complete install instructions
2. `cd ./cookbook/tests`
3. `python -m unittest -v`


### Command Line Interface
--------------------------
* State of Indiana Data Collection
	* Save raw data to CSV
		* `python -m cookbook.cli.web_module_api.get_data --data-id=8787939c-a268-4570-8f53-1ae50c85dc16 --data-folder=./data --data-id=2e6c6eb8-834d-46ff-94cc-0703e7be5292`
			* data-id: as many ids as you want to collect from.  For more details go to https://hub.mph.in.gov/dataset
			* data-folder: folder to save csv file to.  Each data-id will create 1 csv file, named with the id
* Text Classification Model
	* Build a model
		* `python -m cookbook.cli.text_classifier_api.build_model --in-file=./data/ICD10.xml --in-file=./data/IMMUNIZATION.txt --save-as=./data/text-classifier-v2.pkl`
			* in-file: as many files as you want with raw text data to train the model with.  Note that the file name will be used as the "answers" for the model
			* save-as: file to save data to.  The pickle file includes the trained model and vocabulary of the bag-of-words
	* Use a model
		`python -m cookbook.cli.text_classifier_api.predict --model-file=./data/text-classifier-v2.pkl --data-file=./data/MANUAL_TEST.txt --show --proba`
			* model-file: locatino of pickle file created when building a model
			* data-file: location of raw data to read/make predictions against
			* show: bool flag to show results
			* proba: bool flag to show prediction probabilities(instead of just the classification)