def import_func_from_string(string_name):
    ''' Given a string like 'mod.mod2.funcname' which refers to a function,
        return that function so it can be called
    '''
    mod_name, func_name = string_name.rsplit('.', 1)

    # from http://docs.python.org/faq/programming.html?highlight=importlib#import-x-y-z-returns-module-x-how-do-i-get-z
    mod = __import__(mod_name)
    for i in mod_name.split('.')[1:]:
        mod = getattr(mod, i)

    return getattr(mod, func_name)
