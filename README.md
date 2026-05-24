# qa_python
Тесты для BooksCollector

Всего тестов:41
Покрытие кода: 100%
Файл с тестами: `tests.py`

Фикстуры
`collector` Создает пустой экземпляр `BooksCollector`
`collector_with_books` Создает коллекцию с 6 предустановленными книгами и жанрами

Тестовые данные:
books_for_testing = {
    'Сияние': 'Ужасы',
    'Оно': 'Ужасы',
    'Двенадцать стульев': 'Комедии',
    'Трое в лодке, не считая собаки': 'Комедии',
    '1984': 'Фантастика',
    'Убийство в Восточном экспрессе': 'Детективы',
}

Список тестов:
1. add_new_book — добавление новой книги

test_add_new_book_valid_name_length_added - Книга добавляется при длине имени 1, 20, 39, 40 символов
test_add_new_book_not_valid_name_length_not_added - Книга НЕ добавляется при длине 0 и 41 символ
test_add_new_book_empty_genre - Новая книга добавляется с пустым значением жанра
test_add_new_book_two_similar_books_not_added - Дубликат книги не добавляется

2. set_book_genre — устанавливает жанр книги

test_set_book_genre_sets_correct_genre - Установка жанра для всех книг из books_for_testing
test_set_book_genre_invalid_genre_not_set - Недопустимый жанр не устанавливается

3. get_book_genre — получение жанра

test_get_book_genre_returns_correct_genre - Получение жанра для всех книг из books_for_testing
test_get_book_genre_nonexistent_book_returns_none - Для несуществующей книги возвращается None

4. get_books_with_specific_genre — поиск книг по жанру

test_get_books_with_specific_genre_returns_correct_list - Поиск книг для жанров: Ужасы, Комедии, Фантастика, Детективы
test_get_books_with_specific_genre_empty_result - Для жанра без книг возвращается пустой список

5. get_books_for_children — список детских книг

test_get_books_for_children_adult_book_not_added - У всех детских книг жанр не из genre_age_rating
test_get_books_for_children_books_with_nonexistent_genre_not_added - Книги с несуществующим жанром не попадают в список

6. add_book_in_favorites — добавление в избранное

test_add_book_in_favorites_favorite_books_added - Книга успешно добавляется в избранное (для всех книг)

7. delete_book_from_favorites — удаление из избранного

test_delete_book_from_favorites_favorite_books_remove - Книга успешно удаляется из избранного (для всех книг)
test_delete_book_from_favorites_other_books_remain - При удалении одной книги остальные сохраняются

8. get_list_of_favorites_books — список избранных книг

test_get_list_of_favorites_books_returns_all_favorites - Метод возвращает список всех избранных книг


Запуск тестов:
pytest tests.py --cov=main

Результат:
text
Name      Stmts   Miss  Cover
-----------------------------
main.py      38      0   100%
-----------------------------
TOTAL        38      0   100%

================= 41 passed in 0.10s =================
