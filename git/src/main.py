import json
import os


def load_books(filename='library.json'):
    """Загрузка списка книг из JSON-файла."""
    if not os.path.isfile(filename):
        return []
    with open(filename, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def saving_books(books, filename='library.json'):
    """Сохранение списка книг в JSON-файл."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)
