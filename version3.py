# %%
def _is_member_eligible_for_lending(member_id):
    max_books_to_lend = 2
    is_eligible = False

    if _is_library_member(member_id):
        books_lent_todate = _get_books_lent_todate(member_id)
        if len(books_lent_todate) < max_books_to_lend :
            is_eligible = True
        else:
            print("User not eligible : Cannot lend more than 2 books")
    else:
        print("User not eligible : User is not a member")
    return is_eligible




# %%
