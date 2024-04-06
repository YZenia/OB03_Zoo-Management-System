import pandas as pd
import json


def load_json_to_dataframe(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # Проверяем, что ключи 'animals' и 'staff' существуют и являются списками
        if 'animals' in data and isinstance(data['animals'], list) and 'staff' in data and isinstance(data['staff'],
                                                                                                      list):
            # Создание DataFrame из списка словарей для животных
            animals_df = pd.DataFrame(data['animals'])
            # Создание DataFrame из списка словарей для сотрудников
            staff_df = pd.DataFrame(data['staff'])
            return animals_df, staff_df
        else:
            print("Неверная структура данных в JSON.")
            return None, None
    except FileNotFoundError:
        print("Файл не найден")
        return None, None
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON")
        return None, None
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return None, None


# Использование функции
animals_df, staff_df = load_json_to_dataframe('zoo_data.json')

# Проверка, если DataFrame были успешно созданы
if animals_df is not None and staff_df is not None:
    print("Таблица животных:")
    print(animals_df)
    print("\nТаблица сотрудников:")
    print(staff_df)
else:
    print("Не удалось создать таблицы из данных.")
