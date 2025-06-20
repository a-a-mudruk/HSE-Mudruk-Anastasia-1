PLAINTIFF = {
    'name': 'Петров Иван Сергеевич',
    'inn': '123456789012',
    'ogrnip': '123456789012345',
    'address': '123456, г. Москва, ул. Примерная, д. 1, кв. 10'
}

courts = {
    'А40': {
        'court_name': 'Арбитражный суд города Москвы',
        'court_address': '115225, г. Москва, ул. Б. Тульская, 17'
    },
    'А33': {
        'court_name': 'Арбитражный суд Красноярского края',
        'court_address': '660021, г. Красноярск, ул. Ленина, 18'
    },
    'А41': {
        'court_name': 'Арбитражный суд Московской области',
        'court_address': '143402, г. Красногорск, ул. Речная, 8'
    }
}

respondents = [
    {
        'full_name': 'ООО "ПРОДСЕРВИС"',
        'short_name': 'ООО "ПРОДСЕРВИС"',
        'inn': '2465081302',
        'ogrn': '1042402640125',
        'address': '660020, г. Красноярск, ул. 7-й км Енисейского тракта',
        'case_number': 'А33-2794/2011'
    },
    {
        'full_name': 'ООО "ШОМРАТ ХАУС"',
        'short_name': 'ООО "ШОМРАТ ХАУС"',
        'inn': '7732005842',
        'ogrn': '1037700179857',
        'address': '119634, г. Москва, ул. Шолохова, д. 13',
        'case_number': 'А40-123456/2023'
    }
]

def generate_court_header(respondent: dict, case_number: str) -> str:
    required_fields = ['short_name', 'inn', 'ogrn', 'address']
    for field in required_fields:
        if field not in respondent:
            raise ValueError(f"Отсутствует поле {field} у ответчика")
    court_code = case_number.split('-')[0]
    if court_code not in courts:
        raise ValueError(f"Суд с кодом {court_code} не найден")
    
    court = courts[court_code]

    return f"""В {court['court_name']}
Адрес: {court['court_address']}

Истец: {PLAINTIFF['name']}
ИНН {PLAINTIFF['inn']} ОГРНИП {PLAINTIFF['ogrnip']}
Адрес: {PLAINTIFF['address']}

Ответчик: {respondent['short_name']}
ИНН {respondent['inn']} ОГРН {respondent['ogrn']}
Адрес: {respondent['address']}

Номер дела: {case_number}"""

def process_all_respondents(respondents_list: list[dict]) -> None:
    for idx, respondent in enumerate(respondents_list, 1):
        try:
            case_num = respondent['case_number']
            header = generate_court_header(respondent, case_num)
            print(f"\nДокумент №{idx}")
            print("-" * 50)
            print(header)
            print("-" * 50)
        except Exception as e:
            print(f"Ошибка при обработке ответчика №{idx}: {str(e)}")

if __name__ == "__main__":
    print("=== Тест для ответчика ===")
    test_case = respondents[0]
    print(generate_court_header(test_case, test_case['case_number']))
    
    print("\n=== Обработка всех ответчиков ===")
    process_all_respondents(respondents)