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