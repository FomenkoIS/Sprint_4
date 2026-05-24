from main import BooksCollector
import pytest

books_for_testing = {
    'Сияние': 'Ужасы',
    'Оно': 'Ужасы',
    'Двенадцать стульев': 'Комедии',
    'Трое в лодке, не считая собаки': 'Комедии',
    '1984': 'Фантастика',
    'Убийство в Восточном экспрессе': 'Детективы'
}

@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def collector_with_books(collector):
    for name, genre in books_for_testing.items():
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
    return collector
t
class TestBooksCollector:
  
    def test_add_new_book_add_two_books(self, collector):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('book_name', [
        'A',
        'AbcdeAbcdeAbcdeAdcde',
        'AbcdeAbcdeAbcdeAdcdeAdcdeAdcdeAdcdeAdcd',
        'AbcdeAbcdeAbcdeAdcdeAdcdeAdcdeAdcdeAdcde'
    ])

    def test_add_new_book_valid_name_length_added(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

    @pytest.mark.parametrize('book_name', [
        '',
        'AbcdeAbcdeAbcdeAdcdeAdcdeAdcdeAdcdeAdcdeA'
    ])

    def test_add_new_book_not_valid_name_length_not_added(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    def test_add_new_book_duplicate_not_added(self, collector):
        collector.add_new_book('Сияние')
        collector.add_new_book('Сияние')
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_empty_genre_added(self, collector):

        collector.add_new_book('Сияние')
        assert collector.books_genre['Сияние'] == ''

    @pytest.mark.parametrize('book_name, genre', books_for_testing.items())
    def test_set_book_genre_sets_correct_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        assert collector.get_book_genre(book_name) == genre
 
    @pytest.mark.parametrize('book_name, genre', books_for_testing.items())
    def test_get_book_genre_get_genre_name(self, collector_with_books, book_name, genre):
        
        assert  collector_with_books.get_book_genre(book_name) == genre

    @pytest.mark.parametrize('genre, expected_books', [
        ('Ужасы', ['Сияние', 'Оно']),
        ('Комедии', ['Двенадцать стульев', 'Трое в лодке, не считая собаки']),
        ('Фантастика', ['1984']),
        ('Детективы', ['Убийство в Восточном экспрессе']),
        ('Мультфильмы', [])
    ])
    def test_get_books_with_specific_genre(self, collector_with_books, genre, expected_books):
        assert collector_with_books.get_books_with_specific_genre(genre) == expected_books

    def test_get_books_for_children_adult_book_not_added(self, collector_with_books):
       
        child_books = collector_with_books.get_books_for_children()

        for book in child_books:
            assert collector_with_books.get_book_genre(book) not in collector_with_books.genre_age_rating

    def test_get_books_for_children_books_with_nonexistent_genre_not_added(self, collector):
    
        book_name = 'Хроники Нарнии'
        nonexistent_genre = 'Сказка'
    
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, nonexistent_genre)
    
        child_books = collector.get_books_for_children()
    
        assert book_name not in child_books

    @pytest.mark.parametrize('book_name', books_for_testing.keys())
    def test_add_book_in_favorites_favorite_books_added(self, book_name, collector_with_books):

        collector_with_books.add_book_in_favorites(book_name)
        assert book_name in collector_with_books.favorites

    @pytest.mark.parametrize('book_name', books_for_testing.keys())
    def test_delete_book_from_favorites_favorite_books_remove(self, book_name, collector_with_books):

        collector_with_books.add_book_in_favorites(book_name)
        collector_with_books.delete_book_from_favorites(book_name)
        assert book_name not in collector_with_books.favorites

    def test_get_list_of_favorites_books_get_list_with_favorite_books(self, collector_with_books):

        all_books = list(collector_with_books.get_books_genre().keys())

        for book in all_books:
            collector_with_books.add_book_in_favorites(book)
        favorites = collector_with_books.get_list_of_favorites_books()

        assert favorites == all_books