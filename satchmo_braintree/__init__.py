def import_func_from_string(string_name):
    ''' Given a string like 'mod.mod2.funcname' which refers to a function,
        return that function so it can be called
    '''
    parts = string_name.rsplit('.', 1)
    mod = __import__(parts[0], globals(), locals(), [parts[1]], -1)
    return getattr(mod, parts[1])
