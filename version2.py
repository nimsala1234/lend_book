
from datetime import datetime


def lend_book(member_id, book_id):
    max_books_to_lend = 2
    lend_time_period = 14

    #lend book if only eligible
    if _is_library_member(member_id):
        books_lent_todate = _get_books_lent_todate(member_id)
        if len(books_lent_todate) < max_books_to_lend:
            if _is_book_available(book_id):
                current_date = date.today()
                return_date = current_date + datetime.timedelta(days=lend_time_period)
                _checkout_book(book_id,member_id,return_date)
                print("Book lent for member successfully")
            else:
                print("Book not available")
        else:
            print("Cannot lend more than 2 books")
    else:
        print("Member does not exit")

