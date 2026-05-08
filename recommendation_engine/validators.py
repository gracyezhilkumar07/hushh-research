def validate_query(query):

    if not query:
        return False

    if len(query) < 3:
        return False

    return True