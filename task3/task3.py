import json

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def fill_report_structure(tests_structure, values):
    for test in tests_structure:
        if isinstance(test, dict):
            test_id = test.get('id')
            if test_id is None:
                continue
            
            if isinstance(values, list):
                test['value'] = next((item['value'] for item in values if item['id'] == test_id), "")

            if 'values' in test:
                if isinstance(test['values'], list): 
                    fill_report_structure(test['values'], values)

def save_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    values_file = 'values.json'
    tests_file = 'tests.json'
    report_file = 'report.json'

    values = load_json(values_file)
    tests_structure = load_json(tests_file)

    fill_report_structure(tests_structure, values)

    save_json(report_file, tests_structure)

if __name__ == "__main__":
    main()
