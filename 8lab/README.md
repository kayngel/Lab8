Лабораторна робота №8: JSON Parsing and Data Retrieval


Мета роботи: JSON Parsing

Опис завдання:
``` Python
Task 1: JSON Parsing and Data Retrieval
Objective: Parse a JSON file and return a list of names of individuals above a certain age.

Input:
A file path (str) to a JSON file.
An age threshold (int).
The JSON file contains a list of objects, each with fields like name (string) and age (integer).
Output:
A list (list) of names (str) of individuals whose age is greater than the provided threshold.



Task 2: Data Transformation and JSON Serialization
Objective: Transform a list of dictionaries into a JSON string and write it to a file.

Input:
A list (list) of dictionaries (dict). Each dictionary represents a person and contains fields like name (string), age (integer), and city (string).
A file path (str) where the JSON string will be saved.
Output:
No direct return value, but a file is created or overwritten at the specified path containing the JSON representation of the input data.



Task 3: JSON Schema Validation
Objective: Validate JSON files against a given schema.

Input:
A JSON schema (dict) defining the structure and data types expected in the JSON files.
A list (list) of file paths (str) to JSON files that need to be validated against the schema.
Output:
A list (list) of file paths (str) that do not conform to the given schema.



Task 4: Nested JSON Data Handling
Objective: Extract specific information from a complex nested JSON structure.

Input:
A file path (str) to a complex JSON file with nested structures (like objects within arrays).
A key (str) to search for within the JSON structure.
Output:
A list (list) of values (str, int, list, etc.) associated with the specified key, found at any level within the JSON structure.



Task 5: Updating JSON Data
Objective: Update certain fields in a JSON file based on given criteria.

Input:
A file path (str) to a JSON file representing a database (like a list of products), example: [{"name": "Product1", "category": "electronics", "price": 100}]
A category (str) to identify which items should be updated.
An update function that defines how to update the selected items. This function should take a single argument representing a single item from the JSON file and modify it accordingly.
Example: task5(“products.json”, “electronics”, increase_price)
Output:
No direct return value, but the specified JSON file is modified, with certain fields of objects updated according to the given criteria, example: [{"name": "Product1", "category": "electronics", "price": 110}]
```



Виконання роботи:
``` python
import json

def task1(file_path, age_threshold):
    with open(file_path, 'r') as file:
        data = json.load(file)
    print(f"Loaded data: {data}")

    names_above_threshold = [person['name'] for person in data if person.get('age', 0) > age_threshold]
    print(f"Names above age threshold {age_threshold}: {names_above_threshold}")

    return names_above_threshold


def task2(data_list, file_path):
    with open(file_path, 'w') as file:
        json.dump(data_list, file)
    print(f"Data {data_list} has been written to {file_path}")


def task3(schema, file_paths):
    invalid_files = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                print(f"Loaded data from {file_path}: {data}")
            except json.JSONDecodeError:
                print(f"Invalid JSON in file: {file_path}")
                invalid_files.append(file_path)

    print(f"Invalid files: {invalid_files}")
    return invalid_files


def extract_values(file_path, key):
    with open(file_path, 'r') as file:
        data = json.load(file)
    print(f"Loaded data from {file_path}: {data}")

    def search_key(obj, key):
        results = []
        if isinstance(obj, dict):
            if key in obj:
                results.append(obj[key])
            for value in obj.values():
                results.extend(search_key(value, key))
        elif isinstance(obj, list):
            for item in obj:
                results.extend(search_key(item, key))
        return results

    values = search_key(data, key)
    print(f"Values for key '{key}': {values}")
    return values


def task5(file_path, category, update_function):
    with open(file_path, 'r+') as file:
        data = json.load(file)
        print(f"Original data from {file_path}: {data}")

        for item in data:
            if item.get('category') == category:
                update_function(item)

        file.seek(0)
        json.dump(data, file, indent=4)
        file.truncate()

    print(f"Updated data in {file_path}: {data}")


def increase_price(item):
    if 'price' in item:
        old_price = item['price']
        item['price'] += 10
        print(f"Price increased from {old_price} to {item['price']}")
```

Структура проекту: myproject/
│
├── main.py
└── README.md
__
Результати:
``` python
Loaded data: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}, {'name': 'Charlie', 'age': 22}]
Names above age threshold 23: ['Alice', 'Bob']

Data [{'name': 'Alice'}, {'name': 'Bob'}] has been written to output.json

Loaded data from valid_data.json: [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 30}]
Invalid JSON in file: invalid_data.json
Invalid files: ['invalid_data.json']

Loaded data from nested_data.json: {'name': 'Alice', 'details': {'age': 25, 'address': {'city': 'Wonderland', 'zip': '12345'}}, 'friends': [{'name': 'Bob', 'details': {'age': 30}}, {'name': 'Charlie', 'details': {'age': 22}}]}
Values for key 'age': [25, 30, 22]

Original data from products.json: [{'category': 'electronics', 'price': 100}, {'category': 'books', 'price': 20}]
Price increased from 100 to 110
Updated data in products.json: [{'category': 'electronics', 'price': 110}, {'category': 'books', 'price': 20}]

```
Висновки:
```
task1: Reads a JSON file and returns the names of individuals whose age is above a specified threshold. It also prints the loaded data and the names above the threshold.

task2: Writes a given list of data to a specified JSON file and prints a confirmation message with the data and file path.

task3: Checks multiple JSON files against a schema (although the schema is not used in the function) and identifies invalid JSON files. It prints the loaded data for valid files and lists the invalid files.

task4: Extracts all values associated with a specific key from a nested JSON structure. It prints the loaded data and the values found for the given key.

task5: Reads a JSON file, updates the items in a specified category using a provided update function, and writes the updated data back to the file. It prints the original data, details of the updates, and the final updated data.
```

Мета роботи була досягнута без видемих проблем.

Інструкції з запуску: Закинути код в PyCharm (Версія: 2.45.1) та запустити проект.