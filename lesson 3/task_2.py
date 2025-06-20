import json
import re
from collections import defaultdict

def extract_emails_by_inn(json_path, output_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    email_dict = defaultdict(set) 

    for entry in data:
        publisher_inn = entry.get("publisher_inn")
        if not publisher_inn:
            continue
        msg_text = entry.get("msg_text", "")
        
        emails = set(email_pattern.findall(msg_text))
        if emails:
            email_dict[publisher_inn].update(emails)

    serializable_dict = {k: list(v) for k, v in email_dict.items()}

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(serializable_dict, f, ensure_ascii=False, indent=2)

    return email_dict 

def load_emails_as_sets(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return {k: set(v) for k, v in data.items()}

def main():
    input_json = 'decoded.json'   
    output_json = 'emails.json' 

    emails_dict = extract_emails_by_inn(input_json, output_json)

    print("Извлечённые email-адреса (в виде множеств):")
    for inn, emails in emails_dict.items():
        print(f"{inn}: {emails}")

   
    loaded_emails = load_emails_as_sets(output_json)
    print("\nЗагруженные email-адреса из файла (множества):")
    for inn, emails in loaded_emails.items():
        print(f"{inn}: {emails}")

if __name__ == "__main__":
    main()

