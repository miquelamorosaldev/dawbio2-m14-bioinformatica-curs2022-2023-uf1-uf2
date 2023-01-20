import inspect


# URL: https://stackoverflow.com/questions/2675028/list-attributes-of-an-object
# -----------------------------------------------------------------------------
def explore(obj: object) -> None:

    # 1. Get all members
    member_list = inspect.getmembers(obj)

    # 2. Convert to dict for ease of use
    member_dict = { member[0]:member[1] for member in member_list }

    # 3. Remove private members
    public_member_dict = { key:value for key, value in member_dict.items() if not key.startswith('_') }

    # 4. Remove methods
    public_attribute_dict = { key:value for key, value in public_member_dict.items() if not inspect.ismethod(value) }
    
    # Return
    return public_attribute_dict

# -----------------------------------------------------------------------------

