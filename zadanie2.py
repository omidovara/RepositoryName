# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    try:
        # Считываем содержимое CSV файла
        with open(INPUT_FILENAME, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

        # Сериализуем данные в JSON файл с отступами равными 4
        with open(OUTPUT_FILENAME, 'w') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)  # ensure_ascii=False для поддержки unicode
    except FileNotFoundError:
        print(f"Файл {INPUT_FILENAME} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    task()