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


def list_books(books):
    """Возвращает строку со списком всех книг."""
    if not books:
        return "Библиотека пуста."
    result_lines = []
    for idx, book in enumerate(books, start=1):
        result_lines.append(f"{idx}. {book['title']} | {book['author']} | {book['year']}")
    return "\n".join(result_lines)


def add_book(books, title, author, year):
    """Возвращает новый список с добавленной книгой."""
    new_book = {'title': title, 'author': author, 'year': year}
    return books + [new_book]


def remove_book(books, title):
    """Возвращает новый список без книги с указанным названием."""
    return [book for book in books if book['title'].lower() != title.lower()]


def search_books(books, keyword):
    """Поиск книг по ключевому слову в названии и авторе."""
    keyword_lower = keyword.lower()
    return [
        book for book in books
        if keyword_lower in book['title'].lower() or keyword_lower in book['author'].lower()
    ]
