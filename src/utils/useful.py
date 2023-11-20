def truncate_string(input_str: str, length: int = 12, username: bool = False):
    """ Truncate string to length characters"""
    if username:
        length = 15
        if len(input_str) > length:
            input_str = input_str[:length] + '...'  # Adding those sweet ellipses!
            return input_str
        else:
            return input_str  
    else:
        if len(input_str) > length:
            input_str = input_str[:length] + '...'  # Adding those sweet ellipses!
            return input_str
        else:
            return input_str  
    

