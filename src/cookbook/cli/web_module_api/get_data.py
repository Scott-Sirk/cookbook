
import argparse
import os
from cookbook.collect.web import Indiana_Web_API

if __name__ == '__main__':
    print('Find data source ids here: https://hub.mph.in.gov/dataset\n')
    parser = argparse.ArgumentParser()
    #id to collect from for the indiana web api
    parser.add_argument('--data-id', action='append')
    parser.add_argument('--data-folder', nargs='?', default='.')
    args = parser.parse_args()
    print(args)
    #make instance of our api class to collect from indiana website
    api = Indiana_Web_API()
    #for each id collect data into a dataframe and save it to a csv
    for i in args.data_id:
        df = api.query_data(i)
        #build filename/path to save data to
        filename = f'{i}.csv'
        file = os.path.join(args.data_folder, filename)
        #save data
        df.to_csv(file)
        print(f'Data saved to: {file}')
            
    
