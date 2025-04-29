import json


def task() -> float:
    try:
        # Читаем данные из файла
        with open('input.json', 'r') as file:
            data = json.load(file)

        # Суммируем произведения "score" * "weight" для каждого словаря
        total = sum(item.get("score", 0) * item.get("weight", 0) for item in data)

        # Округляем результат до 3 знаков после запятой
        return round(total, 3)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка при работе с файлом: {e}")
        return 0.0


print(task())