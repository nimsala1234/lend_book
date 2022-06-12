
def _is_member_eligible_for_lending(member_id):
    max_books_to_lend = 2

    if not _is_library_member(member_id):
        print("User not eligble : User is not a member")
        return False
    books_lent_todate = _get_books_lent_todate(member_id)
    if len(books_lent_todate) == max_books_to_lend:
        print("User not eligible: Cannot lend more than 2 books")
        return False
    
    # This point would not be reached if the above conditions meet
    return True

def lend_book(member_id, book_id):
    # lend book if only eligible
    if not _is_member_eligible_for_lending(member_id):
        return
    if _is_book_available(book_id):
        return_date = _get_book_return_date()
        _checkout_book(book_id, member_id, return_date)
        print("Book lent for member successfully")
    else:
        print("Book not available")
        