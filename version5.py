
def lend_book(member_id, book_id):
    #lend book if only eligible
    if _is_member_eligible_for_lending(member_id):
        if _is_book_available(book_id):
            return_date = _get_book_return_date()
            _checkout_book(book_id,member_id,return_date)
            print("Book lent for member successfully")
        else:
            print("Book not available")
