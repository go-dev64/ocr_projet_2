import category
import book
import export
import interface


def main():

    url_chosen = interface.user_choice()
    category.creating_folders_by_categories()
    """Creating Data directory and folder categories
    in the current work directory"""

    list_category = category.category()
    # get list of categories.

    list_of_book = book.all_dictionnary(url=url_chosen)
    # get list of data of books or one book.

    export.export(categories=list_category, books=list_of_book)
    # export data


if __name__ == "__main__":
    main()
