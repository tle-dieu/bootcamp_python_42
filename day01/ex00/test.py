from book import Book
from recipe import Recipe


def main():
    tourte = Recipe('tourte', 5, 10, ['asd', 'egg'], 'Une tourte.', 'starter')
    tourte2 = Recipe('tourte', 5, 10, ['asd', 'egg'], 'Une tourte.', 'dessert')
    tourte3 = Recipe('test3', 5, 10, ['asd', 'egg'], 'Une tourte.', 'dessert')
    # print(tourte)

    book = Book('Livre')
    book.add_recipe(tourte)
    book.add_recipe(tourte2)
    book.add_recipe(tourte3)
    print(book.get_recipe_by_name('tourte'))
    print(book.get_recipe_by_name('tourte'))
    print(book.get_recipe_by_name('test3'))
    # print(book.get_recipes_by_types('starter'))
    # print(book.get_recipes_by_types('dessert'))


main()
