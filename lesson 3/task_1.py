import json
import csv

def load_inn_list(txt_file_path):
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        inn_list = [line.strip() for line in file if line.strip()]
    return set(inn_list)

def load_json(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def filter_by_inn(data, inn_set):
    return [entry for entry in data if entry.get('inn') in inn_set]

def save_to_csv(filtered_data, output_file_path):
    if not filtered_data:
        print("Нет данных для записи в CSV.")
        return
    fieldnames = filtered_data[0].keys()
    with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(filtered_data)

if __name__ == '__main__':
    inn_file = 'traders.txt'
    json_file = 'traders.json'
    output_csv = 'output.csv'

    inn_set = load_inn_list(inn_file)
    data = load_json(json_file)
    filtered_data = filter_by_inn(data, inn_set)
    save_to_csv(filtered_data, output_csv)

    print(f"Готово! Найдено и записано: {len(filtered_data)} записей.")
