
import requests
import csv
from datetime import datetime

def get_json_from_url(url):
    headers = {
        "Accept" : "application/json"
    }
    response = requests.get(url=url, headers=headers)
    
    return response.json()

def save_json_to_csv_file(file_path='Data/', file_name='', json={}):
    column_names = json.keys()
    
    with open(file=f'{file_path}{file_name}', mode='w', encoding='utf-8', newline='\n') as _file:
        writer = csv.writer(_file)
        writer.writerow(column_names)
        for row in json.values():
            for col in row:
                writer.writerow([col])
    
    print(f'File {file_path}{file_name} was successfully saved!')

def main():
    json_data = get_json_from_url(url='https://www.randomlists.com/data/words.json')
    dt = datetime.now().strftime("%Y_%m_%d")
    file_name = f'{dt}.csv'
    save_json_to_csv_file(file_name = file_name, json=json_data)

if __name__ == "__main__":
    main()