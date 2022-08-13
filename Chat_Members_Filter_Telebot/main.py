from telebotHandler import TelebotHandler as TH
#import telebotHandler as TH
import json
import os

def get_token_from_settings(file_name:str = '') -> str:
    
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, file_name)
    
    with open(filename,'r', encoding='UTF-8') as _file:
            obj = json.loads(_file.read())

    return obj.get('bot').get('token')


def main():
    
    token = get_token_from_settings('settings.json')
    handler = TH(token=token)
    handler.start_bot()
    print(handler)
    print(token)
        
if __name__ == "__main__":
    main()
    
    