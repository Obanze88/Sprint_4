import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Властелин колец')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize(
        'name',
        [
            '',
            'А' * 41
        ]
    )
    def test_add_new_book_invalid_name_book_not_added(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert name not in collector.get_books_genre()

    def test_set_book_genre_genre_is_set(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')

        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_book_genre('Оно') == 'Ужасы'

    def test_get_books_with_specific_genre_returns_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Оно')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер']

    def test_get_books_genre_returns_books_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')

        assert collector.get_books_genre() == {'Гарри Поттер': 'Фантастика'}

    def test_get_books_for_children_excludes_age_rating_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Оно')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_books_for_children() == ['Гарри Поттер']

    def test_add_book_in_favorites_book_is_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')

        collector.add_book_in_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == ['Гарри Поттер']

    def test_delete_book_from_favorites_book_is_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')

        collector.delete_book_from_favorites('Гарри Поттер')

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Властелин колец')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_book_in_favorites('Властелин колец')

        assert collector.get_list_of_favorites_books() == [
            'Гарри Поттер',
            'Властелин колец'
        ]