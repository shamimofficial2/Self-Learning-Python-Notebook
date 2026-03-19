# match-case is used to compare a value against multiple patterns and execute the matched block.

def web_status(status):

    match status: # match → the value or variable that will be checked.

        case 200: # se → the pattern or value that Python tries to match against the match value.
            return "OK"
        
        case 404: # se → the pattern or value that Python tries to match against the match value.
            return "Not Found"
        
        case 500: # se → the pattern or value that Python tries to match against the match value.
            return "Internal Server Error"
        
        case _: # _ → the default case (runs if none of the other cases match).
            return "Unknown status"
        
print(web_status(200)) # OK
print(web_status(404)) # Not Found
print(web_status(500)) # Internal Server Error
print(web_status(106)) # Unknown status