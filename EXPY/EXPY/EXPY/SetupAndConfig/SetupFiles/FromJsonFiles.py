import json
import sys,os

class JsonFile:

    file1 = sys.argv[1]

    @staticmethod
    def read_json(a,b,c):
        '''
        This method is used to read from the json config file, which takes the user input.

        '''
        json_file = os.path.join('../ConfigSuite', JsonFile.file1)
        with  open(json_file) as config_json:
            config_data = json.load(config_json)

        script_detail = config_data[a][b][c]
        return script_detail

